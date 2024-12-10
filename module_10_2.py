from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__(target=self.run)
        self.name = name
        self.power = power
        self.start()

    def run(self):
        print(f"{self.name}, на нас напали!")
        enemies = 100
        days = 0
        while enemies > 0:
            sleep(1)
            enemies -= self.power
            days += 1
            print(f"{self.name} сражается {days}, осталось {enemies} воинов")
        print(f"{self.name} одержал победу спустя {days} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)