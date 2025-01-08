import logging
from unittest import TestCase, main, skipIf
from runner_and_tournament_v2 import Runner

class RunnerTest(TestCase):
    is_frozen = False

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            runner = Runner("bob", -5)
            for i in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning("Неверная скорость для Runner")

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            runner = Runner(12)
            for i in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info( '"test_run" выполнен успешно')
        except:
            logging.warning("Неверный тип данных для объекта Runner")

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        bob = Runner("bob")
        martin = Runner("martin")
        for i in range(10):
            bob.run()
            martin.walk()
        self.assertNotEqual(bob.distance, martin.distance)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="utf-8", format="%(levelname)s | %(message)s")
    main()

