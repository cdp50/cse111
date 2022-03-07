import math
from datetime import datetime


width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))
volume = round(math.pi * width ** 2 * aspect * (width * aspect + 2540 * diameter) / 10000000000, 2)
print(f"The appoximate volume is {volume} liters")

current_date_and_time = datetime.now()

if width == 185 and aspect == 60 and diameter == 13:
    print(f"The price for the size {width}/{aspect}R{diameter} is $178 ")
    buy = input("Do you want to buy them? (yes/no) ")
    if buy == "yes": ## es necesario cerrar un "if"? teno que ponerle un else? SI!
        fnumber = input("Please enter your phone number: ")
        with open("volumes.txt",mode = "at") as volumes:
            print(f"{current_date_and_time:%Y-%m-%d}, {width}, {aspect}, {diameter}, {volume}, {fnumber}", file=volumes)
    else: print("Got it! Thank you for visiting us")

elif width == 165 and aspect == 65 and diameter == 14:
    print(f"The price for the size {width}/{aspect}R{diameter} is $87 ")
    buy = input("Do you want to buy them? (yes/no) ")
    if buy == "yes":
        fnumber = input("Please enter your phone number: ")
        with open("volumes.txt",mode = "at") as volumes:
            print(f"{current_date_and_time:%Y-%m-%d}, {width}, {aspect}, {diameter}, {volume}, {fnumber}", file=volumes)
    else: print("Got it! Thank you for visiting us")

elif width == 115 and aspect == 70 and diameter == 15:
    print(f"The price for the size {width}/{aspect}R{diameter} is $112 ")
    buy = input("Do you want to buy them? (yes/no) ")
    if buy == "yes":
        fnumber = input("Please enter your phone number: ")
        with open("volumes.txt",mode = "at") as volumes:
            print(f"{current_date_and_time:%Y-%m-%d}, {width}, {aspect}, {diameter}, {volume}, {fnumber}", file=volumes)
    else: print("Got it! Thank you for visiting us")

elif width == 125 and aspect == 70 and diameter == 16:
    print(f"The price for the size {width}/{aspect}R{diameter} is $124 ")
    buy = input("Do you want to buy them? (yes/no) ")
    if buy == "yes":
        fnumber = input("Please enter your phone number: ")
        with open("volumes.txt",mode = "at") as volumes:
            print(f"{current_date_and_time:%Y-%m-%d}, {width}, {aspect}, {diameter}, {volume}, {fnumber}", file=volumes)
    else: print("Got it! Thank you for visiting us")

else: print("We don't have this size at the moment please check again tomorrow")
with open("volumes.txt",mode = "at") as volumes:
    print(f"{current_date_and_time:%Y-%m-%d}, {width}, {aspect}, {diameter}, {volume}", file=volumes)

