"""test ptest."""
from ptest import hello, hello1


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


# def test_failed():
#     """failed unit-test for testing github action workflow."""
#     assert False
