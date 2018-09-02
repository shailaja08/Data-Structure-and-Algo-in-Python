def postorder_from_in_pre(ino,pre,n):
    if pre[0] in ino:
        root=ino.index(pre[0])
    if root!=0:
        postorder_from_in_pre(ino[:root],pre[1:root+1],len(ino[:root]))
    if root!= n-1:
        postorder_from_in_pre(ino[root+1:],pre[root+1:],len(ino[root+1:]))
    print (pre[0])


ino = [4, 2, 5, 1, 3, 6];
pre = [1, 2, 4, 5, 3, 6];
n=len(ino)
print ("Postorder traversal")
postorder_from_in_pre(ino, pre,n)
