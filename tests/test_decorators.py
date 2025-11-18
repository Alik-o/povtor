from src.decorators import log


def test_log_print(capsys):
    @log()
    def test_log(a, b):
        return a / b

    test_log(10, 0)
    captured = capsys.readouterr()
    assert captured.out == "test_log (10, 0) {} division by zero\n"

    @log()
    def test_log(a, b):
        return a + b

    test_log(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "test_log 3\n"


def test_log_file_error():
    @log("test.log")
    def test_log(a, b):
        return a / b

    with open("test.log", "w", encoding="utf-8") as f:
        f.write("")

    test_log(8, 0)
    with open("test.log", "r", encoding="utf-8") as f:
        assert f.read() == "test_log (8, 0) {} division by zero\n"


def test_log_file():
    @log("test.log")
    def test_log(a, b):
        return a + b

    with open("test.log", "w", encoding="utf-8") as f:
        f.write("")

    test_log(1, 2)
    with open("test.log", "r", encoding="utf-8") as f:
        assert f.read() == "test_log 3\n"
