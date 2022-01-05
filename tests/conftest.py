import pytest

from src.foobartory import Foobartory
from src.robots import Robot
from src.config import config


@pytest.fixture
def factory():
    factory = Foobartory("test")
    return factory


@pytest.fixture
def robot(factory):
    robot = Robot(factory)
    factory.robots.append(robot)
    return robot
