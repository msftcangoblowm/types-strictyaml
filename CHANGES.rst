.. this will be appended to README.rst

Changelog
=========

..

   Feature request
   .................

   - [ci] add to README.rst and gh workflow
     https://github.com/all-contributors/allcontributors.org

   Known regressions
   ..................

   - strictyaml.ruamel relies on typing.Any way too much.

   - strictyaml lacks a pytest test suite. Necessitates a fork

   Commit items for NEXT VERSION
   ..............................

.. scriv-start-here

.. _changes_1-7-3-2:

Version 1.7.3.2 — 2026-08-13
------------------------------

feat: stream typing
feat: narrow typing YAMLChunk._strictparsed YAMLChunk._ruamelparsed
refactor(compound): slots and attributes
docs: commentary on typing of complicated YAMLChunk._strictparsed
tests: document strictyaml#65
tests: FixedSeq Map MapPattern MapCombined

.. _changes_1-7-3-1:

Version 1.7.3.1 — 2026-06-26
------------------------------

- tests: CommaSeparated and Enum
- chore(README.rst): add stubtest button
- ci: stubtest workflow
- fix: strictyaml.scalar.Enum (#3)

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
