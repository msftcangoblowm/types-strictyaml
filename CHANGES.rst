.. this will be appended to README.rst

Changelog
=========

..

   Feature request
   .................

   Known regressions
   ..................

   - strictyaml.ruamel relies on typing.Any way too much.

   - strictyaml lacks a pytest test suite. Necessitates a fork

   Commit items for NEXT VERSION
   ..............................

.. scriv-start-here

.. _changes_1-7-3-0:

Version 1.7.3.0 — 2026-06-01
------------------------------

- feat: strictyaml stubs against both mypy and pyright
- feat: initial pytest tests to confirm stubs
- ci: gh workflows
- chore: Makefile tox.ini tox-req.ini tox-test.ini pre-commit
- ci(testsuite): mypy librt doesn't support pypy
- ci: status badges for mypy pyright tests

.. scriv-end-here
