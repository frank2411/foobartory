from uuid import uuid4

from unittest.mock import patch

from src.robots import Robot


class TestRobotsActivities:

    def test_setup_robots_base(self, factory):
        factory.setup_robots()

        assert len(factory.robots) == 2

    @patch('src.foobartory.Foobartory.setup_robots')
    @patch('src.foobartory.Foobartory.assign_activity')
    def test_run_factory(self, activity_mock, setup_robots_mock, factory):

        factory.stock.foo = [
            uuid4(), uuid4(), uuid4(),
            uuid4(), uuid4(), uuid4(),
            uuid4()
        ]

        factory.stock.euros = 3

        # Force juste one cycle of run_factory starting with 29 robots
        # And simulating the last one buy
        fake_robots = []

        for x in range(0, 30):
            fake_robots.append(Robot(factory))

        factory.robots = fake_robots
        factory.run_factory()

        assert len(factory.robots) == 30

    def test_activity_buy_robot(self, factory):

        factory.stock.foo = [
            uuid4(), uuid4(), uuid4(),
            uuid4(), uuid4(), uuid4(),
            uuid4()
        ]

        factory.stock.euros = 3

        # Force juste one cycle of run_factory starting with 29 robots
        # And simulating the last one buy
        fake_robots = []

        for x in range(0, 29):
            fake_robots.append(Robot(factory))

        factory.robots = fake_robots

        assert len(factory.robots) == 29

        factory.assign_activity(fake_robots[0])

        assert len(factory.robots) == 30

    @patch('src.robots.randrange')
    def test_activity_sell_foobar(self, range_mock, factory):

        factory.stock.foobar = [
            uuid4(), uuid4(), uuid4(),
            uuid4(), uuid4(),
        ]

        range_mock.return_value = 4

        fake_robots = [Robot(factory)]
        factory.robots = fake_robots

        factory.assign_activity(fake_robots[0])

        assert len(factory.stock.foobar) == 1
        assert factory.stock.euros == 4

    @patch('src.robots.randrange')
    def test_activity_sell_foobar_all_sold(self, range_mock, factory):

        factory.stock.foobar = [
            uuid4(), uuid4(), uuid4(),
            uuid4(), uuid4(),
        ]

        range_mock.return_value = 5

        fake_robots = [Robot(factory)]
        factory.robots = fake_robots

        factory.assign_activity(fake_robots[0])

        assert len(factory.stock.foobar) == 0
        assert factory.stock.euros == 5

    @patch('src.robots.randrange')
    def test_activity_assemble_foobar(self, range_mock, factory):

        factory.stock.foo = [uuid4(), uuid4(), uuid4(), uuid4(), uuid4()]
        factory.stock.bar = [uuid4(), uuid4(), uuid4(), uuid4(), uuid4()]

        range_mock.return_value = 50

        fake_robots = [Robot(factory)]
        factory.robots = fake_robots

        factory.assign_activity(fake_robots[0])

        assert len(factory.stock.foobar) == 1
        assert len(factory.stock.foo) == 4
        assert len(factory.stock.bar) == 4

    @patch('src.robots.randrange')
    def test_activity_mine_foo(self, range_mock, factory):

        factory.stock.foo = [uuid4(), uuid4(), uuid4()]

        range_mock.return_value = 50

        fake_robots = [Robot(factory)]
        factory.robots = fake_robots

        factory.last_assigned_activity = "mine_foo"
        factory.assign_activity(fake_robots[0])

        assert len(factory.stock.foo) == 4

    @patch('src.robots.randrange')
    def test_activity_mine_bar(self, range_mock, factory):

        factory.stock.bar = [uuid4(), uuid4(), uuid4()]

        range_mock.return_value = 50

        fake_robots = [Robot(factory)]
        factory.robots = fake_robots

        factory.last_assigned_activity = "mine_bar"
        factory.assign_activity(fake_robots[0])

        assert len(factory.stock.bar) == 4

    def test_activity_random_activity(self, factory):

        fake_robots = [Robot(factory)]
        factory.robots = fake_robots

        factory.assign_activity(fake_robots[0])

        assert factory.last_assigned_activity
