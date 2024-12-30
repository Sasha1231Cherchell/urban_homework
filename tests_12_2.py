from unittest import TestCase, main, skipIf
from runner_and_tournament import Runner, Tournament


class TournamentTest(TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls) -> None:
        cls.all_results = dict()

    def setUp(self) -> None:
        self.usein = Runner("Усэйн", 10)
        self.andrei = Runner("Андрей", 9)
        self.nik = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls) -> None:
        print(cls.all_results)

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        tournament = Tournament(90, self.usein, self.nik)
        self.__class__.all_results = tournament.start()
        self.assertTrue(self.__class__.all_results[1], self.usein.name)

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        tournament = Tournament(90, self.andrei, self.nik)
        self.__class__.all_results = tournament.start()
        self.assertTrue(self.__class__.all_results[1], self.andrei.name)

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        tournament = Tournament(90, self.usein, self.andrei, self.nik)
        self.__class__.all_results = tournament.start()
        self.assertTrue(self.__class__.all_results[1], self.usein.name)


if __name__ == "__main__":
    main()
