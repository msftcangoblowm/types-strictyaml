.ONESHELL:
.DEFAULT_GOAL := help
SHELL := /bin/bash

APP_NAME := wifi_reconnect

#virtual environment. If 0 issue warning
#Not activated:0
#activated: 1
ifeq ($(VIRTUAL_ENV),)
$(warning virtualenv not activated)
is_venv =
else
is_venv = 1
VENV_BIN := $(VIRTUAL_ENV)/bin
VENV_BIN_PYTHON := python3
PY_X_Y := $(shell $(VENV_BIN_PYTHON) -c 'import platform; t_ver = platform.python_version_tuple(); print(".".join(t_ver[:2]));')
endif

#curatables dist dir: .whl and .tar.gz
PROJECT_SRC := /mnt/sda1/dev_parent/$(APP_NAME)
PROJECT_DIST := $(PROJECT_SRC)/dist

#ERR MESSAGES
MSG_ROOT_NOT := Must be root to perform this action
MSG_USER_ONLY := Run as normal Linux session user, not as root

EUID ?= $(shell id -u)

ifeq ($(is_venv),1)
  VENV_PACKAGES ?= $(shell $(VENV_BIN_PYTHON) -m pip list --disable-pip-version-check --no-python-version-warning --no-input | /bin/awk '{print $$1}')
  IS_PACKAGE ?= $(findstring $(1),$(VENV_PACKAGES))
  is_pip ?= $(call IS_PACKAGE,pip)

  #BUILD
  build_out ?= $(shell if [[ $(EUID) -eq 0 ]]; then $(VENV_BIN_PYTHON) -m build 2>/dev/null; fi)

  #pytest
  cache_prefix := pycache_prefix=/tmp/$(APP_NAME)
  cache_dir := cache_dir=/tmp/$(APP_NAME)/.pytest_cache
  sqa_warn_on := SQLALCHEMY_WARN_20=1
  # pyargs := pytest_curatable_lib
  # pytest_plugin := --nice-43c254dc6d698964


  # ifeq ($(origin pytest_package),undefined)
  # pytest_package = pytest_curatable_lib
  # endif
  # pytest_run ?= $(shell if [[ -n "$(1)" ]]; then $(sqa_warn_on) $(VENV_BIN_PYTHON) -X "$(cache_prefix)" -W always::DeprecationWarning -m pytest -o "$(cache_dir)" -r x $(pytest_plugin) --pyargs "$(pytest_package).$(1)"; fi; )

endif


##@ Helpers

# https://www.thapaliya.com/en/writings/well-documented-makefiles/
.PHONY: help
help:					## (Default) Display this help -- Always up to date
	@awk -F ':.*##' '/^[^: ]+:.*##/{printf "  \033[1m%-20s\033[m %s\n",$$1,$$2} /^##@/{printf "\n%s\n",substr($$0,5)}' $(MAKEFILE_LIST)

##@ Manage

#run all pre-commit checks
.PHONY: pre-commit
pre-commit: private target_tty = $(if $(show),1,0)
pre-commit:				## Run checks found in .pre-commit-config.yaml
	@out=$$(SKIP=pyright pre-commit run --all-files ||:)
	if [[ $(target_tty) -eq 1 ]]; then
	echo "$$out" | /bin/tee -a /tmp/out.txt
	else
	echo "$$out" > /tmp/out.txt
	fi

.PHONY: update-pre-commit
update-pre-commit:		## Bump package to latest version
	@pre-commit autoupdate

# @out=$$(pre-commit run --all-files pyright ||:)
# run against strictyaml, not types-strictyaml
.PHONY: preright
preright:				## Run pyright
	@out=$$(PYRIGHT_PYTHON_CACHE_DIR=/tmp/.cache/pyright PYRIGHT_PYTHON_FORCE_VERSION=latest pyright -p pyright-custom-config.json . ||:)
	echo "$$out" > /tmp/out.txt

.PHONY: premypy
premypy:				## Run pyright
	@out=$$(pre-commit run --all-files mypy ||:)
	echo "$$out" > /tmp/out.txt

.PHONY: check
check: private verbose_text = $(if $(v),"-vv")
check: private target_tty = $(if $(show),1,0)
check:					## Run tests -- make [v=1] [show=1] check
ifeq ($(is_venv),1)
	@if [[ $(target_tty) -eq 1 ]]; then
	$(VENV_BIN_PYTHON) -m pytest $(verbose_text) --config-file=pyproject.toml tests
	else
	$(VENV_BIN_PYTHON) -m pytest $(verbose_text) --config-file=pyproject.toml tests > /tmp/out_tests.err
	fi
endif
