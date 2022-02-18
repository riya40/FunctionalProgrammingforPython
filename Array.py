"""
Printing the values in 2D array list
"""


def array_input(rows, cols):
    array = []
    for i in range(rows):
        columns = []
        for j in range(cols):
            values = int(input("enter the values:"))
            columns.append(values)
        array.append(columns)

    # For printing the matrix
    for i in range(rows):
        for j in range(cols):
            print(array[i][j], end=" ")
        print()


if __name__ == '__main__':
    rows = int(input("enter the row size"))
    cols = int(input("enter the columns sie"))
    array_input(rows, cols)
