# Software testing is awesome! An introduction to `pytest`

This tutorial introduces [`pytest`](https://docs.pytest.org): a
full-featured testing framework for Python. This tutorial includes 
[slides that introduce software testing and  discuss best 
practices](./Introduction_to_pytest.pdf).  

This tutorial is expected to take ∼1.5 hours, with a short break in the
middle.

## Outline

[Example tests from Astropy]: https://github.com/astropy/astropy/blob/main/astropy/units/tests/test_physical.py

1. [Assertions and exceptions](./01_Assertions_and_exceptions.md)
2. [Floating point comparisons](./02_Floating_point_comparisons.md)
3. [Creating and running a test](./03_Creating_and_running_a_test.md)
4. [Command line options](./04_Command_line_options.md)
5. [Markers](./05_Markers.md)
6. [Parametrization](./06_Parametrization.md)
7. [Testing exceptions](./07_Testing_exceptions.md)
8. [Testing a Python module](./08_Testing_a_Python_module.md)
9. [Example tests from Astropy] (if time)
10. [Best practices for software testing](./Introduction_to_pytest.pdf)
    (if time) ← Slides 9–14

## Resources

[`tox`]: https://tox.wiki/en/latest/
[`nox`]: https://nox.thea.codes/en/stable/
[GitHub Actions]: https://github.com/features/actions
[Awesome `pytest`]: https://github.com/augustogoulart/awesome-pytest
[Python Testing with `pytest`]: https://pragprog.com/titles/bopytest2/python-testing-with-pytest-second-edition/
[Writing clean scientific software]: https://doi.org/10.5281/zenodo.3922956
[Test and code podcast]: https://testandcode.com/

* Next steps
  - Test automation with [`tox`] and/or [`nox`] ← I recommend `nox` for
    new projects since it lets us configure tests in Python, whereas 
    `tox` requires a configuration file that I find hard to edit.  
  - Running tests automagically with [GitHub Actions]
* [Awesome `pytest`]: A curated list of awesome `pytest` resources
* [Writing clean scientific software] by N. Murphy ← Updated slides from
  my CfA tutorial in 2021 
* [Python Testing with `pytest`] book and [Test and code podcast] by B.
  Okken

## Contact information

Please feel free to write me at namurphy@cfa.harvard.edu, or to set up
a meeting at this [scheduling link](https://calendly.com/namurphy).