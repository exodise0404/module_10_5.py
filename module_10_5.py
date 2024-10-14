import multiprocessing
import datetime

start = datetime.datetime.now()
def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


if __name__ == '__main__':

    file_list = [f'./Files/file {number}.txt' for number in range(1, 5)]

    start1 = datetime.datetime.now()
    for file_name in file_list:
        read_info(file_name)
        end1 = datetime.datetime.now()
    print(end1 - start1)

    start2 = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, file_list)
        end2 = datetime.datetime.now()
    print(end2 - start2)
