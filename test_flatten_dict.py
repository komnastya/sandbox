import pytest
from flatten_dict import flatten_dict

def test_flatten_dict():
  assert flatten_dict({}) == {}

  assert flatten_dict({
      'a': 1,
      'b': 2,
      'c': 3,
  }) == {
      'a': 1,
      'b': 2,
      'c': 3,
  }

  assert flatten_dict({
      'a': {
          'x': 1
      },
      'b': {
          'x': 2
      },
      'c': {
          'x': 3
      },
  }) == {
      'a.x': 1,
      'b.x': 2,
      'c.x': 3,
  }

  assert flatten_dict({
      'a': 1,
      'b': {
          'x': 2,
          'y': {
              'u': 3
          }
      }
  }) == {
      'a': 1,
      'b.x': 2,
      'b.y.u': 3,
  }
