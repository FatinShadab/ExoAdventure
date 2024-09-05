import uvicorn
import click

@click.group()
def cli():
    """Command-line interface for managing FastAPI app."""
    pass

@cli.command()
@click.option('--host', default='127.0.0.1', help='Host to run the server.')
@click.option('--port', default=8000, help='Port to run the server.')
@click.option('--reload', is_flag=True, help='Enable auto-reload.')
def runserver(host, port, reload):
    """Run the FastAPI server."""
    if reload:
        uvicorn.run("app.main:app", host=host, port=port, reload=reload)
    else:
        from app import APP
        uvicorn.run(APP, host=host, port=port)

@cli.command()
def test():
    """Run tests or other tasks."""
    click.echo("Running tests...")  # Add actual test code if needed


if __name__ == '__main__':
    cli()
