"""
Calculating The WindChill By using The Given Input
By using the formula windchill = 35.74 + 0.6215 * t +(0.4275 * t -35.75) * v**0.16)
"""


def calculating_chill(t, v):
    if t > 50 or v > 120 or v < 3:
        print("invalid")
    else:
        windchill = 35.74 + 0.6215 * t +(0.4275 * t -35.75) * (v**0.16)
        print(windchill)


if __name__ == '__main__':
    t = int(input('enter value'))
    v = int(input('enter value'))
    calculating_chill(t,v)