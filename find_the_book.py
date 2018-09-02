def prime_(number):
    if number==1 or number ==0:
        print("not prime")
        return
    if number==2:
        print("prime")
        return
    i=2
    while i<number:
        if number%i==0:
            print("not prime")
            break
        else:
            i=i+1
    else:
        print("number is prime")

prime_(25)
