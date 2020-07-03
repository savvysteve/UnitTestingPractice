# UnitTestingPractice

Helpful StackOverflow links 

- https://stackoverflow.com/questions/10253826/path-issue-with-pytest-importerror-no-module-named-yadayadayada

    I'm not sure why py.test does not add the current directory in the PYTHONPATH itself, but here's a workaround (to be executed from the root of your repository):

        python -m pytest tests/

    It works because Python adds the current directory in the PYTHONPATH for you.



- https://stackoverflow.com/questions/45210149/pytest-doesnt-run-any-test

    To determine why tests are not running, these steps are useful:

    1. Verify that all files with test cases start with 'test_' word.
    2. Verify that all test cases names also start with 'test_' word.
    3. Verify that you have created pytest.ini file in the root directory
    4. Verify that you have __init__.py file in all directories/sub-directories of the project
    5. Verify that any test classes you may use start with Test 

