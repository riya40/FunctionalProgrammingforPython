import math
"""
Calculating the Quadratic Equation By Given Input 
"""


def calculating_values(a, b, c):
    root1 = -b + (math.sqrt(((b * b) - (4 * a * c)))) / 2 * a
    root2 = -b - (math.sqrt(((b * b) - (4 * a * c)))) / 2 * a
    print(root1)
    print(root2)


if __name__ == '__main__':
    a = int(input('enter value'))
    b = int(input('enter value'))
    c = int(input('enter value'))
    calculating_values(a, b, c)
