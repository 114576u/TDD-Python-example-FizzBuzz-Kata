
# note that in order to be identified as a test file, it has to end in _test.py
# under settings -> Python Integrated Tools -> Default Test Runner has to be "pytest"

# test are usual functions that must start by test_
# if test involves a class, that needs to start with Test

# if we want to run code before and/or after a test, we can use:
#   def setup_module()
#   def teardowm_module()
#   def setup_function()
#   def teardown_module()
#   def setup_class()
#   def teardown_class()
#   def setup_method()
#   def teardown_method()

import pytest

# -- below represents production code
def fizzBuzz( value ):
    if isMultiple(value, 3):
        if isMultiple(value, 5):
            return "FizzBuzz"
        return "Fizz"
    if isMultiple(value, 5):
        return "Buzz"
    return str(value)

def isMultiple(value, mod):
    return (value % mod) == 0

# -- below represents all tests listed in "Fizz Buzz Kata Use Cases" file

def checkFizzBuzz( value, expectedRetVal ):
    retVal = fizzBuzz(value)
    assert retVal == expectedRetVal

def test_returns1With1PassedIn():
    checkFizzBuzz(1, "1")

def test_returns2With2PassedId():
    checkFizzBuzz(2, "2")

def test_returnsFizzWith3PassedIn():
    checkFizzBuzz(3, "Fizz")

def test_returnsBuzzWith5PassedIn():
    checkFizzBuzz(5, "Buzz")

def test_returnsFizzWith6PassedIn():
    checkFizzBuzz(6, "Fizz")

def test_returnsBuzzWith10PassedIn():
    checkFizzBuzz(10, "Buzz")

def test_returnsFizzBuzzWith15PassedIn():
    checkFizzBuzz(15, "FizzBuzz")

def setup_function(function):
    if function == test_returnsFizzBuzzWith15PassedIn:
        print("\nSetting up test_returnsFizzBuzzWith15PassedIn")
    else:
        print("\nSetting up another test")

def teardown_function(function):
    if function == test_returnsFizzBuzzWith15PassedIn:
        print("\nTeardown test_returnsFizzBuzzWith15PassedIn")
    else:
        print("\nTeardown another test")

# exception test
from pytest import raises

def raisesValueException():
    raise ValueError

def test_exception():
    with raises(ValueError):
        raisesValueException()