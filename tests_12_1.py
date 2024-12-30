from unittest import TestCase, main
from runner import Runner


class RunnerTest(TestCase):
    def test_walk(self):
        runner = Runner("bob")
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner("martin")
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        bob = Runner("bob")
        martin = Runner("martin")
        for i in range(10):
            bob.run()
            martin.walk()
        self.assertNotEqual(bob.distance, martin.distance)


main()
