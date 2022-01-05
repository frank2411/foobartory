from .config import config
from .robots import Robot
from .stock import Stock

from random import choice


class Foobartory:

    def __init__(self, name):
        self.robots = []
        self.stock = Stock()
        self.last_assigned_activity = None
        self.factory_name = name

    def setup_robots(self):
        print("Robots are being activated.")
        return [
            self.robots.append(Robot(self)) for r in range(config["FOOBARTORY_ROBOTS"])
        ]

    def assign_activity(self, robot):
        if len(self.stock.foo) >= 6 and self.stock.euros >= 3:
            robot.buy_robot()
        elif len(self.stock.foobar) == 5:
            robot.sell_foobars()
        elif len(self.stock.foo) >= 5 and len(self.stock.bar) >= 5:
            robot.assemble_foobar()
        elif self.last_assigned_activity == "mine_foo" and len(self.stock.foo) < 10:
            robot.mine_foo()
        elif self.last_assigned_activity == "mine_bar" and len(self.stock.bar) < 10:
            robot.mine_bar()
        else:
            chosen_activity = choice([robot.mine_foo, robot.mine_bar])
            self.last_assigned_activity = chosen_activity.__name__
            chosen_activity()

    def run_factory(self):

        print("Factory is opening.")
        self.setup_robots()

        print(f"starting with {len(self.robots)} robots.")

        while len(self.robots) < 30:
            for robot in self.robots:
                self.assign_activity(robot)

        print("Reached 30 robots! Good job!")
