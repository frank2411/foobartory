from uuid import uuid4

from unittest.mock import patch


class TestRobotsActivities:

    def test_mine_foo(self, robot):
        robot.mine_foo()

        assert len(robot.factory.stock.foo) == 1

        robot.mine_foo()

        assert len(robot.factory.stock.foo) == 2

    def test_mine_bar(self, robot):
        robot.mine_bar()

        assert len(robot.factory.stock.bar) == 1

        robot.mine_bar()

        assert len(robot.factory.stock.bar) == 2

    @patch('src.robots.randrange')
    def test_assemble_foobar_success(self, randrange_mock, robot):
        robot.mine_bar()
        robot.mine_foo()

        randrange_mock.return_value = 50

        robot.assemble_foobar()

        assert len(robot.factory.stock.foobar) == 1

    @patch('src.robots.randrange')
    def test_assemble_foobar_error(self, randrange_mock, robot):
        robot.mine_bar()
        robot.mine_foo()

        randrange_mock.return_value = 70

        robot.assemble_foobar()

        assert len(robot.factory.stock.foobar) == 0
        assert len(robot.factory.stock.foo) == 0

    @patch('src.robots.randrange')
    def test_sell_foobar(self, randrange_mock, robot):
        robot.factory.stock.foobar = [
            uuid4(), uuid4(), uuid4()
        ]

        randrange_mock.return_value = 3

        robot.sell_foobars()

        assert len(robot.factory.stock.foobar) == 0
        assert robot.factory.stock.euros == 3

    def test_buy_robot(self, factory, robot):
        robot.factory.stock.foo = [
            uuid4(), uuid4(), uuid4(),
            uuid4(), uuid4(), uuid4(),
            uuid4(), uuid4(), uuid4()
        ]

        robot.factory.stock.euros = 3

        robot.buy_robot()

        assert len(robot.factory.stock.foo) == 3
        assert robot.factory.stock.euros == 0
        assert len(robot.factory.robots) == 2
