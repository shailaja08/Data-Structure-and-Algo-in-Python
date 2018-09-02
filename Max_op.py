def function_op(a):
    op=0
    j=0
    max_ele=max(a)
    ind_max=a.index(max_ele)
    for i in a:
        if i !=max_ele:
            a[j]+=1
            max_ele-=1
            a[ind_max]-=1
            j+=1
            op+=1
        else:
            j+=1
    for i in a:
        if i!=max_ele:
            op=-1
            break
    print(op)
            

a = [2, 2, 3]
function_op(a)
