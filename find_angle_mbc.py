from math import acos, degrees
ab = int(input())
bc = int(input())

ac = (ab ** 2 + bc ** 2) ** (1 / 2)

print(str(round(degrees(acos(bc / ac)))) + chr(176))