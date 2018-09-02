def palindrum(list_a):
    c=0
    for i in list_a:			 
        t = i
        rev = 0
	while t>0:
            rev = rev * 10 + t % 10
            t = t / 10
	if rev == i:
	    print (i)
	    c = c + 1



num=[10,121,133,155,141,252]
palindrum(num)
num=[111, 220, 784, 565, 498, 787, 363]
palindrum(num)
