# coding=utf-8
import sys

from even import myEven, isEven
from fifo import FIFO1, FIFO2
import time


if __name__ == '__main__':

    tic_start = time.time()
    myEven(-1000000000)
    tic_end = time.time()

    #print("Моя функция: " + str(tic_end - tic_start))

    tic_start = time.time()
    isEven(-1000000000)
    tic_end = time.time()

    #print("Не моя функция: " + str(tic_end - tic_start))

    #print('10 - чётное число: ' + str(myEven(10)))
    #print('967 - нечётное число: ' + str(myEven(967)))
    #print

    fifo = FIFO1(6)
    print(fifo.isEmpty())


    fifo.push(1)
    fifo.push(2)
    fifo.push(3)
    fifo.push(4)
    fifo.push(5)
    fifo.push(6)
    fifo.printQueue()

    print(fifo.pop())
    print(fifo.pop())
    print(fifo.pop())
    print(fifo.pop())
    #print(fifo.pop())
    #print(fifo.pop())
    print

    fifo.printQueue()
