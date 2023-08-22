from ptest import hello

def test_print(capsys):
    hello()

    captured = capsys.readouterr()
    assert captured.out == "hello\n"