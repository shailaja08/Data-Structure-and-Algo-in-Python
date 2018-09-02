"""def reverse_arr(x,start,end):
    while start<end:
        x[start],x[end]=x[end],x[start]
        start+=1
        end-=1
    return x

x=[1,2,3,4]
  #shailaja yadav"
print(reverse_arr(x,0,3))
"""
"""
def rev_str(x):
    str=''
    for i in range(len(x)-1,-1,-1):
        if not x[i].isalpha():
            continue
        str+=x[i]
    print(str)


rev_str("shailaja yadav")
"""
"""
def rev_str_not_special_chr(x):
    LIST=list(x)
    l=0
    r=len(x)-1
    while l<=r:
        if not isAlphabet(LIST[l]):
            l+=1
        elif not isAlphabet(LIST[r]):
            r-=1
        else:
            LIST[l],LIST[r]=LIST[r],LIST[l]
            l+=1
            r-=1
    print (tostr(LIST))

def tostr(x):
    return ''.join(x)

def isAlphabet(x):
    return x.isalpha()

x="a!!!b.c.d,e'f,ghi"
rev_str_not_special_chr(x)
"""   
def remove_space(x):
    sti=""
    for i in range(len(x)):
        if x[i]!=" ":
            sti+=x[i]
    print(sti)

x="g  eeks   for ge  eeks  "
remove_space(x)
