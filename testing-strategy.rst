What to test?
==============

``types-strictyaml`` has way too much usage of ``typing.Any``. Both
mypy and pyright don't return errors, so too late to
``find an issue`` --> ``create a test`` --> ``fix the typing``.
Rinse wash repeat.

In pyproject.toml ``[tool.mypy]`` could set ``warn_return_any = true``.
But it's nonobvious when ``Any`` is [in]appropriate.

and

Fixing ``Any`` rtype everywhere would take too long.

links
------

`strictyaml docs <https://hitchdev.com/strictyaml/using/alpha/compound/>`_

`pytest-mypy-plugins repo <https://github.com/TypedDjango/pytest-mypy-plugins>`_

Avoid
------

1. testing for runtime Exception

strategies
-----------

1. View source code and stub.
   Read source code, check class & instance attributes in stubs.

2. Positive Tests -- Valid usage infers the exact expected type
   (not just Any or a broad Union).

3. Negative Tests -- Invalid usage fails with the specific error you
   expect.

Where to Attempt Verification
------------------------------

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
