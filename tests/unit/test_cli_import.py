def test_can_import_cli_app() -> None:
    from flint.cli import app

    assert app.info.name == "flint"
