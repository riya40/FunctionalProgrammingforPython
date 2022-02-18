import math
"""
Calculating the Distance Between The Point By given Input 
"""

def calculating_distance(x_value, y_value):
    print(math.sqrt((x_value * x_value) + (y_value * y_value)))


if __name__ == '__main__':
    x_value = int(input("enter the value"))
    y_value = int(input("enter the value"))
    calculating_distance(x_value, y_value)