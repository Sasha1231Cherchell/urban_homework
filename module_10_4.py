from threading import Thread
from time import sleep
from random import randint
from queue import Queue


class Table:
    def __init__(self, number: int):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name: str):
        super().__init__(target=self.run)
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)

    def get_available_table(self) -> Table | None:
        for table in self.tables:
            if table.guest is None:
                return table
        return None

    def is_at_least_one_table_busy(self) -> bool:
        for table in self.tables:
            if table.guest is not None:
                return True
        return False

    def guest_arrival(self, *guests):
        for guest in guests:
            table = self.get_available_table()
            if table is not None:
                table.guest = guest
                print(f"{guest.name} сел(-а) за стол номер {table.number}")
                guest.start()
            else:
                print(f"{guest.name} в очереди")
                self.queue.put(guest)

    def discuss_guests(self):
        while not self.queue.empty() and self.is_at_least_one_table_busy():
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None
                table = self.get_available_table()
                if not self.queue.empty() and table is not None:
                    table.guest = self.queue.get()
                    print(f"{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                    table.guest.start()
                    table = self.get_available_table()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()