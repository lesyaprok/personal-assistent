from project import recognize_username, greeting, modify_input
import pytest

def test_recognize_username():
  assert recognize_username("My name is Alice") == "Alice"
  assert recognize_username("Mary") == "Mary"
  assert recognize_username("I'm Alex") == "Alex"
  assert recognize_username("") == "user"


def test_greeting():
  assert greeting("Alice") == "\nHi, Alice! How can I help you?\nTo print all possible commands please type 'list'" 


def test_modify_input():
  assert modify_input("HellO") == "hello"
  assert modify_input("SEARCH CAT VIDEO") == "search cat video"
