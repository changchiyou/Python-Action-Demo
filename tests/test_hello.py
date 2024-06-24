"""test ptest."""
from ptest import hello, hello1, yellow
import pytest


def test_print(capsys):
    """test ptest.hello function."""
    hello()

    captured = capsys.readouterr()
    assert captured.out == "hello\n"


def test_print1(capsys):
    """test ptest.hello function."""
    hello1()

    captured = capsys.readouterr()
    assert captured.out == "hello1\n"

def test_yellow(capsys):
    """test ptest.hello function."""
    yellow()

    captured = capsys.readouterr()
    assert captured.out == "yellow\n"

# def test_failed():
#     """failed unit-test for testing github action workflow."""
#     assert False

@pytest.mark.webtest
def test_mark():
    """deselected unit-test for testing github action workflow."""
    assert False