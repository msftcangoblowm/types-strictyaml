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

   - ci(codeql-analysis): change path src -> strictyaml-stubs
   - ci(testsuite): mypy librt doesn't support pypy
   - ci(codeql-analysis): explicitly specify python-version
   - ci: within a job jobs.jobname.result unavailable
   - feat: strictyaml stubs against both mypy and pyright
   - feat: initial pytest tests to confirm stubs
   - ci: status badges for mypy pyright tests
   - ci: gh workflows
   - chore: requirement files sync using wreck
   - chore: Makefile tox.ini tox-req.ini tox-test.ini pre-commit

.. scriv-start-here

.. scriv-end-here
