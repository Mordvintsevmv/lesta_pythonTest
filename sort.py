import random


def quicksort(arr):
    if len(arr) > 1:
        num = random.choice(arr)

        less_arr = []
        equal_arr = []
        more_arr = []

        for i in arr:
            if i < num:
                less_arr.append(i)
            elif i > num:
                more_arr.append(i)
            else:
                equal_arr.append(i)
        return quicksort(less_arr) + equal_arr + quicksort(more_arr)
    else:
        return arr


def countingsort(arr, radix=False):

    if radix:
        max_num = 9
    else:
        max_num = max(arr)

    count_arr = [0]*(max_num+1)

    for i in arr:
        count_arr[i] += 1

    sorted_arr = []

    for i in range(len(count_arr)):
        sorted_arr += [i]*count_arr[i]

    return sorted_arr


