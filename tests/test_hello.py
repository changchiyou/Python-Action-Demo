"""test ptest."""
from ptest import hello


def test_print(capsys):
    """test ptest.hello function."""
    hello()

    captured = capsys.readouterr()
    assert captured.out == "hello\n"
