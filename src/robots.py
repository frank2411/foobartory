import time
from uuid import uuid4
from random import randrange
from functools import wraps


def do_activity(robot_activity):
    @wraps(robot_activity)
    def wrapper(self, *args, **kwargs):
        if self.activity and self.activity != robot_activity.__name__:
            time.sleep(0.5)
        self.activity = robot_activity.__name__
        return robot_activity(self, *args, **kwargs)

    return wrapper


class Robot:

    # 100 milliseconds == 1 test second
    # 0.1

    def __init__(self, factory):
        self.id = uuid4()
        self.activity = None
        self.factory = factory

    @do_activity
    def mine_foo(self):
        print("mine_foo")
        time.sleep(0.1)
        self.factory.stock.foo.append(uuid4())

    @do_activity
    def mine_bar(self):
        print("mine_bar")
        time.sleep(randrange(50, 200) / 1000)
        self.factory.stock.bar.append(uuid4())

    @do_activity
    def assemble_foobar(self):
        print("assemble_foobar")
        time.sleep(0.2)

        foo = self.factory.stock.foo.pop()

        if randrange(100) < 60:
            bar = self.factory.stock.bar.pop()
            self.factory.stock.foobar.append(f'{foo}{bar}')
            return

        print(f"Assembling failed. Dropping foo {foo}")

    @do_activity
    def sell_foobars(self):
        print("sell_foobars")
        time.sleep(1)

        to_sell_foobars = randrange(1, 5)
        self.factory.stock.foobar = self.factory.stock.foobar[:-to_sell_foobars]
        self.factory.stock.euros += to_sell_foobars

    @do_activity
    def buy_robot(self):
        print("Buying new robot")

        print(len(self.factory.stock.foo))
        self.factory.stock.foo = self.factory.stock.foo[:-6]
        print(len(self.factory.stock.foo))

        self.factory.stock.euros -= 3
        self.factory.robots.append(Robot(self.factory))
