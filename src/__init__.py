import click

from .foobartory import Foobartory


@click.command()
@click.option('--factory-name', 'factory_name', help='Name for factory.', default="test_foobartory")
def do_foobartorize(factory_name):
    """DOCSTRING"""
    factory = Foobartory(factory_name)
    factory.run_factory()
