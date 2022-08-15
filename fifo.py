# coding=utf-8

"""

Данный циклический буфер реализован с использованием дополнительной переменной cursize,
 которая позволяет подсчитать количество элементов в буфере.

Были реализованы:

 1. Конструктор, который принимает размер буфера
 2. Функция конвертации буфера в строку (для дальнейшего вывода) (возвращает строку)
 3. Функция push для добавления элемента в конец очереди
 4. Функция pop для извлечения элемента из начала очереди (возвращает элемент буфера)
 5. Функция isEmpty для проверки пустого буфера (возвращается bool)
 6. Функция isFull для проверки полного буфера (возвращается bool)
 7. Функция printQueue для печати буфера
 8. Функция length для получения длины (возвращает длину буфера)
 9. Функция clear для полной очистки буфера

Переменные класса:

 1. Size - размер буфера
 2. Tail - конец очереди (индекс записи)
 3. Head - начало очереди (индекс  чтения)
 4. Cursize - размер буфера
 5. My_queue - массив данных

"""


class FIFO1(object):

    # Конструктор класса
    def __init__(self, size=5):
        self.size = size
        self.tail = -1
        self.head = 0
        self.cursize = 0
        self.my_queue = [None] * size

    # Функция преобразования в строку
    def __str__(self):
        i = self.head
        string = "["
        for j in range(self.cursize-1):
            string = string + str(self.my_queue[i]) + ", "
            i = (i + 1) % self.size
        string = string + str(self.my_queue[i]) + "]"
        return string

    # Функция добавления элемента в очередь
    def push(self, data):
        if self.isFull():
            print("Больше нет места")
        else:
            self.tail = (self.tail + 1) % self.size
            self.my_queue[self.tail] = data
            self.cursize += 1

    # Функция получения первого элемента из очереди
    def pop(self):
        if self.isEmpty():
            print("Очередь пуста!")
        else:
            data = self.my_queue[self.head]
            self.head = (self.head + 1) % self.size
            self.cursize -= 1
            return data

    # Функция проверки пустого буфера
    def isEmpty(self):
        return self.cursize == 0

    # Функция проверки полного буфера
    def isFull(self):
        return self.cursize == self.size

    # Функция печати буфера
    def printQueue(self):
        if self.isEmpty():
            print("Очередь пуста!")
        else:
            i = self.head
            for j in range(self.length()):
                print(str(self.my_queue[i]) + " "),
                i = (i + 1) % self.size
            print

    # Функция получения буфера
    def length(self):
        return self.cursize

    # Функция очистки буфера
    def clear(self):
        i = self.head
        for j in range(self.length()):
            self.my_queue[i] = None
            i = (i + 1) % self.size

        self.tail = 5
        self.head = 0
        self.cursize = 0


"""

Данный циклический буфер реализован аналогично первому, но без использования переменной текущей длины буфера cursize.

Такой способ  поможет сохранить немного памяти на создание переменной.

"""

class FIFO2(object):

    # Конструктор класса
    def __init__(self, size=5):
        self.size = size
        self.tail = 0
        self.head = 0
        self.my_queue = [None] * size

    # Функция преобразования в строку
    def __str__(self):
        i = self.head
        string = "["
        for j in range(self.length()-1):
            string = string + str(self.my_queue[i]) + ", "
            i = (i + 1) % self.size
        string = string + str(self.my_queue[i]) + "]"
        return string

    # Функция добавления элемента в очередь
    def push(self, data):
        if self.my_queue[self.tail] is not None:
            print("Больше нет места")
        else:
            self.my_queue[self.tail] = data
            self.tail = (self.tail + 1) % self.size

    # Функция получения первого элемента из очереди
    def pop(self):
        if self.head is None:
            print("Очередь пуста!")
        else:
            data = self.my_queue[self.head]
            self.my_queue[self.head] = None
            self.head = (self.head + 1) % self.size
            return data

    # Функция печати буфера
    def printQueue(self):
        i = self.head
        for j in range(self.length()):
            print(str(self.my_queue[i]) + " "),
            i = (i + 1) % self.size
        print

    # Функция получения буфера
    def length(self):
        if self.tail > self.head:
            return self.tail-self.head
        elif self.tail < self.head:
            return self.size - self.head + self.tail
        elif self.my_queue[self.tail] is not None:
            return self.size
        else:
            return 0

    # Функция очистки буфера
    def clear(self):
        i = self.head
        for j in range(self.length()):
            self.my_queue[i] = None
            i = (i + 1) % self.size

        self.tail = 0
        self.head = 0


