import typer
from rich.console import Console
from rich.table import Table
from model import Todo
from datetime import datetime
from database import get_all_todos, delete_todo, insert_todo, complete_todo, update_todo, get_todos_from_category, uncomplete_todo

console = Console()

app = typer.Typer()


@app.command(short_help='adds an item')
def add(task: str, category: str):
    typer.echo(f"adding {task}, {category}")
    todo = Todo(task, category)
    insert_todo(todo)
    show()

@app.command()
def delete(position: int):
    typer.echo(f"deleting {position}")
    # indices in UI begin at 1, but in database at 0
    delete_todo(position-1)
    show()

@app.command()
def update(position: int, task: str = None, category: str = None):
    typer.echo(f"updating {position}")
    update_todo(position-1, task, category)
    show()

@app.command()
def complete(position: int):
    typer.echo(f"complete {position}")
    complete_todo(position-1)
    show()

@app.command()
def uncomplete(position: int):
    typer.echo(f"uncomplete {position}")
    uncomplete_todo(position-1)
    show()

@app.command()
def show(category: str = None):
    if not category:
        tasks = get_all_todos()
    else:
        tasks = get_todos_from_category(category)
    console.print("[bold magenta]Todos[/bold magenta]!", "💻")

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=6)
    table.add_column("Todo", min_width=20)
    table.add_column("Category", min_width=12, justify="right")
    table.add_column("Created At", min_width=12, justify="right")
    table.add_column("Done", min_width=12, justify="right")

    def get_category_color(category):
        COLORS = {'Learn': 'cyan', 'YouTube': 'red', 'Sports': 'cyan', 'Study': 'green'}
        if category in COLORS:
            return COLORS[category]
        return 'white'

    for idx, task in enumerate(tasks, start=1):
        c = get_category_color(task.category)
        is_done_str = '✅' if task.status == 2 else '❌'
        dt_obj = datetime.fromisoformat(task.date_added).strftime('%d-%m-%Y')
        table.add_row(str(idx), task.task, f'[{c}]{task.category}[/{c}]', dt_obj, is_done_str)
    console.print(table)


if __name__ == "__main__":
    app()