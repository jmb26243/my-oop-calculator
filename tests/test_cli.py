from calculator.cli import run


def test_add_and_exit(monkeypatch, capsys):
    inputs = iter([
        "add",
        "10",
        "5",
        "exit",
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run()

    output = capsys.readouterr().out

    assert "15.0" in output
    assert "Goodbye!" in output
def test_subtract_and_exit(monkeypatch, capsys):
    inputs = iter([
        "subtract",
        "20",
        "7",
        "exit",
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run()

    output = capsys.readouterr().out

    assert "13.0" in output
    assert "Goodbye!" in output
def test_history(monkeypatch, capsys):
    inputs = iter([
        "add",
        "10",
        "5",
        "history",
        "exit",
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run()

    output = capsys.readouterr().out

    assert "15.0" in output
    assert "0: 15.0" in output
def test_remove(monkeypatch, capsys):
    inputs = iter([
        "add",
        "10",
        "5",
        "remove",
        "0",
        "history",
        "exit",
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run()

    output = capsys.readouterr().out

    assert "Calculation removed." in output
