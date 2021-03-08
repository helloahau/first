"""Tests for `notebookc` package."""
from notebookc import notebookc


def test_convert(capsys):
    """Correct my_name argument prints"""
    notebookc.convert("Joe")
    captured = capsys.readouterr()
    assert "Joe" in captured.out


def test_convert_2(capsys):
    """Correct my_name argument prints"""
    notebookc.convert("Jack")
    captured = capsys.readouterr()
    assert "Jack" in captured.out
