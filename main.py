# coding=utf-8
import random

from even import myEven, isEven
from fifo import FIFO1, FIFO2
from sort import quicksort, countingsort
import time

if __name__ == '__main__':

    print("------------------\n")
    print("\tЧётность числа\n")
    print("Проверка работы \n")

    print('10 - чётное число: ' + str(myEven(10)))
    print('967 - нечётное число: ' + str(myEven(967)))

    print("\nПроверка скорости \n")

    tic_start = time.time()
    myEven(1234567890)
    tic_end = time.time()

    print("Моя функция чётности: " + str(tic_end - tic_start))

    tic_start = time.time()
    isEven(1234567890)
    tic_end = time.time()

    print("Не моя функция чётности: " + str(tic_end - tic_start))

    print("\n\n------------------\n")
    print("\tЦиклический буфер 1\n")
    print("Проверка работы \n")

    fifo1 = FIFO1(6)

    fifo1.push(1)
    fifo1.push(2)
    fifo1.push(3)

    print("Содержимое буфера: " + str(fifo1))

    print("Pop: " + str(fifo1.pop()))

    fifo1.push(4)
    fifo1.push(5)
    fifo1.push(6)
    fifo1.push(7)

    print("Попытка добавить больше элементов, чем это позволяет размер: ")
    fifo1.push(8)

    fifo1.pop()
    fifo1.push(8)
    print("Содержимое буфера после всех манипуляций: " + str(fifo1))

    print("\n\n\tЦиклический буфер 2\n")
    print("Проверка работы \n")

    fifo2 = FIFO2(6)

    fifo2.push(1)
    fifo2.push(2)
    fifo2.push(3)

    print("Содержимое буфера: " + str(fifo2))

    print("Pop: " + str(fifo2.pop()))

    fifo2.push(4)
    fifo2.push(5)
    fifo2.push(6)
    fifo2.push(7)

    print("Попытка добавить больше элементов, чем это позволяет размер: ")
    fifo2.push(8)

    fifo2.pop()
    fifo2.push(8)
    print("Содержимое буфера после всех манипуляций: " + str(fifo2))


    print("------------------\n")
    print("\tСортировка массивов\n")
    print("Проверка скорости \n")

    arr_small_nums = []
    for i in range(50000):
        arr_small_nums.append(random.randint(0, 60000))

    arr_quick = arr_small_nums
    arr_count = arr_small_nums

    tic_start = time.time()
    quicksort(arr_quick)
    tic_end = time.time()
    print("Быстрая (маленькие числа): " + str(tic_end - tic_start))

    tic_start = time.time()
    countingsort(arr_count)
    tic_end = time.time()
    print("Подсчёт (маленькие числа): " + str(tic_end - tic_start))


    arr_large_nums = []
    for i in range(50000):
        arr_large_nums.append(random.randint(0, 6000000))

    arr_quick = arr_large_nums
    arr_count = arr_large_nums

    tic_start = time.time()
    quicksort(arr_quick)
    tic_end = time.time()
    print("\nБыстрая (большие числа): " + str(tic_end - tic_start))

    tic_start = time.time()
    countingsort(arr_count)
    tic_end = time.time()
    print("Подсчёт (большие числа): " + str(tic_end - tic_start))
