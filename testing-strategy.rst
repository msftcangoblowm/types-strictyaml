Testing
========

``types-strictyaml`` is a stubs package of strictyaml; a prelude to a fork.

The stubs contain commentary, along with ``stubtest_allowlist.txt``, highlights
bugs in ``strictyaml``.

Stub package test suite is only supposed to test typing, not be a complete testsuite.
Since ``strictyaml`` lacks a pytest testsuite, the testsuite is for both
``types-strictyaml`` AND ``strictyaml``.

The ``strictyaml`` author deemphasized static type
checking and emphasized runtime validation. As a consequence, the static typing
work was subpar.

The Rust community acknowledges ``strictyaml`` package as authoritative, but
since the static typing work was never done, there is a **long trail of bodies**
of porters who've **tried and died** while attempting to create a Rust port.

Their cargos are an attestment that the path to glory is paved with not only hard
work, but the right work. In strictyaml's case, that path is not a straight line.
You have to go backwards (``types-strictyaml``) then backwards again (a Python fork)
to have a chance to eventually move forwards (a Rust port).

They focused on wrong thing. Rust and not Python. Should have recognized
to port to a strongly typed language, those stubs are not optional.

``types-strictyaml`` gives these Rust porters a chance. A Python fork of
strictyaml that fixed coding errors would give a further boost.

What the Rust porters eventually hopefully learn is the ``strictyaml`` author
is much smarter, and way more devious, than us. Trying to rewrite his work from
scratch, even using ``strictyaml`` as a reference, is a fools errand.

Commands
---------

The most important test is :command:`mypy.stubtest`.

Run pytest testsuite. This is written using
`pytest-mypy-plugins repo <https://github.com/TypedDjango/pytest-mypy-plugins>`_

.. code-block:: shell

   make show=1 check

Run pre-commit. Fix the basic issues, but still need :command:`tox -e lint`

.. code-block:: shell

   make show=1 pre-commit


All gh workflow commands must be run

.. code-block:: shell

   # A stub package must run stubtest on the parent package.
   rm -rf build/lib; cd .tox && tox --root=.. -c ../tox.ini -e stubtest --workdir=. -vvv; cd - &>/dev/null
   # pyright needs to explicitly include strictyaml package.
   rm -rf build/lib; cd .tox && tox --root=.. -c ../tox.ini -e pyright --workdir=. -vvv; cd - &>/dev/null
   rm -rf build/lib; cd .tox && tox --root=.. -c ../tox.ini -e lint --workdir=. -vvv; cd - &>/dev/null
   rm -rf build/lib; cd .tox && tox --root=.. -c ../tox.ini -e rst2html5 --workdir=. -vvv; cd - &>/dev/null

Tricks of the trade
--------------------

``typing_extensions.assert_type`` is used extensively rather than ``reveal_type``.

When a command will raise an Exception, you'll need

.. code-block:: text

   expect_fail: yes
   regex: yes

When the traceback includes newlines regex will need ``[\s\S]*``, not just ``.*``

links
------

`strictyaml docs <https://hitchdev.com/strictyaml/using/alpha/compound/>`_

`pytest-mypy-plugins repo <https://github.com/TypedDjango/pytest-mypy-plugins>`_

AI agent advice
----------------

In pyproject.toml ``[tool.mypy]`` could set ``warn_return_any = true``.
But it's nonobvious when ``Any`` is [in]appropriate.

``Any`` and laziness are the enemy. Start with ``strictyaml`` then progress
to ``strictyaml.ruamel``.

strategies
"""""""""""

1. View source code and stub.
   Read source code, check class & instance attributes in stubs.

2. Positive Tests -- Valid usage infers the exact expected type
   (not just Any or a broad Union).

3. Negative Tests -- Invalid usage fails with the specific error you
   expect.

Generic Inference & Type Narrowing
"""""""""""""""""""""""""""""""""""

Check that generic parameters are correctly inferred from arguments, not defaulted to ``Any``.

- Test: Pass a str to a generic function; assert the return type is ``T[str]``, not ``T[Any]``.

Tool: ``reveal_type()`` in ``pytest-mypy-plugins``.

Overload Resolution
""""""""""""""""""""

If you use ``@overload``, verify that the correct signature is picked for specific inputs.

- Test: Call the function with arguments matching overload \#1; assert the return type matches \#1 exactly.

Risk: If the order is wrong or constraints are loose, mypy might pick a fallback signature without erroring.

Any Escapes
""""""""""""

Ensure your functions don't accidentally return Any when they should return a specific type.

- Test: Enable ``warn_return_any`` in your test config. If a function returns ``Any``, the test fails.

Negative Constraints
"""""""""""""""""""""

Crucial for Stubs

Verify that invalid code actually breaks.

- Test: Pass an int where a str is required.

Assertion: The test must produce a specific ``[arg-type]`` error.
If it passes, your stub is too permissive.
