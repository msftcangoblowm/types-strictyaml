types-strictyaml
=================

Typing stubs for strictyaml

|  |test-status| |stubtest| |mypy| |pyright|
|  |last-commit| |downloads|
|  |license| |maturity|

.. PYVERSIONS

\* Python 3.10 through 3.14

**new in 1.7.3.2**

narrow typing YAMLChunk._strictparsed YAMLChunk._ruamelparsed;
stream typing; tests for compound;

**new in 1.7.3.1**

verify CommaSeparated and Enum (\#3);
stubtest workflow and button;

Why?
-----

``strictyaml`` is ignored by the Python community. Instead these are
promoted: TOML, Python internal yaml, pyyaml, and pydantic.

None of which strictly validate very likely malicious dangerous user input.

Feel sorry for those who have been mislead to believe, without
validating against a schema, the input files are safe.

User input validation critical security issues pop up constantly. In
Python at least, some of these can be avoided completely by choosing ``strictyaml``.

History
--------

The ``strictyaml`` author had his own ideas on how to test and document
Python packages. Regardless agree with him or not, this created a barrier
to entry to surmount for both potential contributors and maintainers.

Would argue that barrier, evidently, is too formidable for us average
diabolical albeit lazy geniuses.

Then to add insult to injury, the author ascended to another plane of
existence, leaving ``strictyaml`` unmaintained.

There exists a vacuum where there should be: stubs, pytest test suite,
coverage, and Sphinx docs.

Roadmap
---------

These stubs were created without forking ``strictyaml``. And will help
downstream authors test their packages. Hopefully lead to ``strictyaml``
acceptance by the Python community.

Static type checking performed using both mypy and pyright. With the hope
that later ``strictyaml`` is forked and pytest test suite is created. So can
prove coverage and allow pyright to find coding errors.

Projects
---------

These packages input files are strictly validated against a schema.

If have a package built that is protected by strictyaml, we'd like to
hear from you.

- `strictyamlx <https://pypi.org/project/strictyamlx>`_

- `logging-strict <https://pypi.org/project/logging-strict>`_

- `sphinx-external-toc-strict <https://pypi.org/project/sphinx-external-toc-strict>`_

strictyaml team
-----------------

`Dave Faulkmore <faulkmore@protonmail.com>`_ and
`Muneeb ur Rahman <muneebdev1@gmail.com>`_ both have made contributions
to strictyaml community. Both have skin in the game and would like to see
``strictyaml`` project status revived.

If share our passion, throw caution to the wind, say `hmm why not?`,
put the effort towards writing a message, then find the mental fortitude
to click the Send button.

Contributing
-------------

Create .venv
"""""""""""""

.. code:: shell

   pyenv versions
   mkdir .venv && cd .venv
   python -m venv .
   cd - &>/dev/null

   . .venv/bin/activate
   python -m pip install -e ".[dev]"

Run tests
""""""""""

Verbose and show output

.. code:: shell

   make v=1 show=1 check

Quiet and save output to /tmp folder

.. code:: shell

   make check

Run mypy
"""""""""

``pytest-mypy-plugins`` works only with mypy, not pyright.

.. code:: shell

   make premypy

Run pyright
""""""""""""

Against stubs

.. code:: shell

   pyright strictyaml-stubs/

Run pre-commit
"""""""""""""""

.. code:: shell

   make pre-commit

Run stubtest
"""""""""""""

Without this check, a stubs package could confidently provide incorrect
type information, leading to false positives or negatives for users.

.. code:: shell

   python -m pip install strictyaml types-strictyaml
   stubtest  --mypy-config-file=pyproject.toml --allowlist=stubtest_allowlist.txt strictyaml > /tmp/out.txt

licenses
"""""""""

Lets take legal compliance seriously to show commitment to respect and
acknowledge authors.

Creates ``NOTICE.txt``, ``licenses.json`` and ``sbom.json``

.. code:: shell

   rm -rf build/lib; cd .tox && tox --root=.. -c ../tox.ini -e notice \
   --workdir=. -vvv; cd - &>/dev/null
   rm -rf build/lib; cd .tox && tox --root=.. -c ../tox.ini -e sbom \
   --workdir=. -vvv; cd - &>/dev/null

``LICENSE`` and ``NOTICE.txt`` are essentially the same expect LICENSE is manually maintained.

.. |downloads| image:: https://img.shields.io/pypi/dm/types-strictyaml
.. |last-commit| image:: https://img.shields.io/github/last-commit/msftcangoblowm/types-strictyaml/master
    :target: https://github.com/msftcangoblowm/types-strictyaml/pulse
    :alt: last commit to gauge activity
.. |maturity| image:: https://img.shields.io/badge/status-Beta-yellow
   :target: https://pypi.org/classifiers/
   :alt: Status: Beta
.. |license| image:: https://img.shields.io/github/license/msftcangoblowm/types-strictyaml
    :target: https://github.com/msftcangoblowm/types-strictyaml/blob/master/LICENSE
    :alt: License
.. |test-status| image:: https://github.com/msftcangoblowm/types-strictyaml/actions/workflows/testsuite.yml/badge.svg
    :target: https://github.com/msftcangoblowm/types-strictyaml/actions/workflows/testsuite.yml
    :alt: test

.. |stubtest| image:: https://github.com/msftcangoblowm/types-strictyaml/actions/workflows/quality-stubtest.yml/badge.svg
   :target: https://github.com/msftcangoblowm/types-strictyaml/actions/workflows/quality-stubtest.yml
   :alt: stubtest status
.. |mypy| image:: https://github.com/msftcangoblowm/types-strictyaml/actions/workflows/quality-mypy.yml/badge.svg
   :target: https://github.com/msftcangoblowm/types-strictyaml/actions/workflows/quality-mypy.yml
   :alt: mypy status
.. |pyright| image:: https://github.com/msftcangoblowm/types-strictyaml/actions/workflows/quality-pyright.yml/badge.svg
   :target: https://github.com/msftcangoblowm/types-strictyaml/actions/workflows/quality-pyright.yml
   :alt: pyright status
