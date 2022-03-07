import math

ni = int(input("Enter the number of items: "))
nipb = int(input("Enter the number of items per box: "))
ping =  math.ceil(ni / nipb)
print(f"For {ni} items, packing {nipb} items in each box, you will need {ping} boxes.")