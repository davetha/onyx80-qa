"""Tests for stats.py."""

from stats import average


def test_average():
    assert average([1, 2, 3, 4]) == 2.5
