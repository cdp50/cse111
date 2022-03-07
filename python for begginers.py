W = float(input("Weight: "))
Qu = input("(K)g or (L)bs: ")
if "l" in Qu or "L" in Qu:
    W /= 2.2
    print("Weight in Kg:  " + str(round(W,1)))
elif "K" in Qu or "k" in Qu:
    W *= 2.2
    print("Weight in Lbs:  " + str(round(W,1)))
else: print( "Please input valid data")
