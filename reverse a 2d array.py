original = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
            ]


def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]
    # return map(list, list_of_tuples)

print(list(rotated(original)))

# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]