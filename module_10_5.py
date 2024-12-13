from time import time
from multiprocessing import Pool


def read_info(name):
    all_data = list()
    with open(name) as f:
        line = f.readline()
        while line != "":
            all_data.append(line)
            line = f.readline()
    print(f"{name} readed")


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start = time()
    for fname in filenames:
        read_info(fname)
    end = time()
    print(end-start)

    start = time()
    with Pool(processes=4) as pool:
        it = pool.map(read_info, filenames)
    end = time()
    print(end-start)
