import math


def encrypt_message(file1, file2, key):

    with open(file1, "r") as file:
        content = str(file.read())
    
    with open(file2, "w") as file:
        cols = key
        rows = math.ceil(len(content) / key)

        matrix = [[' ' for _ in range(cols)] for _ in range(rows)]

        index = 0
        for i in range(rows):
            for j in range(cols):
                if index < len(content):
                    matrix[i][j] = content[index]
                    index += 1

        transposed = transpose(matrix, [])
        
        for i in range(len(transposed)):
            for j in range(len(transposed[0])):
                file.write(transposed[i][j].strip())

    return file2


def decrypt_message(file1, file2, key):
    with open(file1, "r") as file:
        content = str(file.read())

    with open(file2, "w") as file:
        rows = key
        cols = math.ceil(len(content) / key)
        empty_spaces = rows * cols - len(content)

        matrix = [[' ' for _ in range(cols)] for _ in range(rows)]

        index = 0
        for i in range(rows):
            for j in range(cols):
                if i >= rows - empty_spaces and j >= cols - 1:
                    matrix[i][j] = ' '
                elif index < len(content):
                    matrix[i][j] = content[index]
                    index += 1

        transposed = transpose(matrix, [])
        
        for i in range(len(transposed)):
            for j in range(len(transposed[0])):
                file.write(transposed[i][j].strip())

    return file2


def transpose(matrix, m2):
    for i in range(len(matrix[0])):
        row = []
        for j in matrix:
            row.append(j[i])
        m2.append(row)
    return m2