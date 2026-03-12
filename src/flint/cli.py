import typer
from rich.console import Console

from flint.commands import register_commands

app = typer.Typer(
    name="flint",
    no_args_is_help=True,
    help="Flint CLI - developer toolchain for Python projects.",
)
console = Console()


@app.callback()
def callback() -> None:
    """Main entrypoint for the CLI."""


register_commands(app)


def main() -> None:
    app()
