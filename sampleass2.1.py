def divisible():
    for i in range(1000,2001):
        a=i/7
        if(a%5==0):
            print(f"{i} is not divisible by 7 and is multiple of 5")
        else:
            print(f"{i} is divisible by 7 and is not multiple of 5")
divisible()