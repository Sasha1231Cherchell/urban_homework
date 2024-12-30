from unittest import TestSuite, TextTestRunner, TestLoader
from tests_12_2 import TournamentTest
from tests_12_1 import RunnerTest


test_suite = TestSuite()
test_suite.addTest(TestLoader().loadTestsFromTestCase(TournamentTest))
test_suite.addTest(TestLoader().loadTestsFromTestCase(RunnerTest))

test_runner = TextTestRunner(verbosity=2)
test_runner.run(test_suite)
