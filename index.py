amount= input("enter the amount : ")

amount=int(amount)
isValid=amount % 10000
if (amount <=200000 ):
    if(isValid == 0):
        num_of_50=amount // 50000
        remain_of_50=amount %50000
        if(remain_of_50 == 0):
            print(str(num_of_50) + " ta 50 thousand tuman for you")
        else:
            num_of_10=remain_of_50 // 10000
            print(str(num_of_50) + " ta 50 thousand tuman for you")
            print(str(num_of_10) + " ta 10 thousand tuman for you")
    else:
        print("your amount must be mazrab of 10 thousand")
else:
    print("your amount must be equal less than 200 thousand tuman")
