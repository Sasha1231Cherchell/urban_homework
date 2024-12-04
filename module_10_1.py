from time import sleep, time
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, "w") as f:
        for i in range(word_count):
            f.write(f"Какое-то слово № {i + 1}")
            sleep(0.1)
        print(f"Завершилась запись в файл {file_name}")


start_time = time()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
end_time = time()
print(f"Работа потоков {end_time - start_time}")
thr = [
    Thread(target=write_words, args=(10, "example5.txt")),
    Thread(target=write_words, args=(30, "example6.txt")),
    Thread(target=write_words, args=(200, "example7.txt")),
    Thread(target=write_words, args=(100, "example8.txt"))
]
start_time = time()
for t in thr:
    t.start()
for t in thr:
    t.join()
end_time = time()
print(f"Работа потоков {end_time - start_time}")