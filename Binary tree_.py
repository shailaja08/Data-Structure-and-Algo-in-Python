from collections import deque
class Node:
    def __init__(self,key):
        self.val=key
        self.left=None
        self.right=None

class Binary_tree:
    def __init__(self):
        self.root=None

    def create_bt(self):
        self.root=Node(1)
        self.root.left = Node(2)
        self.root.right=Node(3)
        self.root.left.left=Node(4)
        self.root.left.right=Node(5)
        #self.root.right.left=Node(6)
        #self.root.right.right = Node(7)
        #self.root.right.left.right = Node(8)
        #self.root.right.right.right = Node(9)

    def display(self):
        self.display_(self.root,0)
        print()
    

    def display_(self,p,level):
        if p is None:
            return
        self.display_(p.left,level+1)#1///2,1///4,2///None,3///none,3
        print()
        for i in range(level):
            print("  ",end=" ")
        print(p.val)
        self.display_(p.right,level+1)

    def inorder(self):
        return self.inorder_(self.root)
    def inorder_(self,p):
        if p is None:
            return
        self.inorder_(p.left)
        self.inorder_(p.right)
        print(p.val," ",end="")

    def level_order(self):
        h=self.height()
        #sprint("h=",h)
        for i in range(h):
            self.printlevelorder(self.root,i)

    def printlevelorder(self,p,level):
        if p is None:
            return
        if level==0:
            print(p.val,end=" ")
            print()
        elif level>0:
            self.printlevelorder(p.left,level-1)
            self.printlevelorder(p.right,level-1)

    def height(self):
        return self.height_(self.root)

    def height_(self,p):
        if p is None:
            return 0
        hl=self.height_(p.left)
        hr=self.height_(p.right)
        if hl>hr:
            return hl+1
        else:
            return hr+1

    def level_order(self):
        if self.root is None:
            print("tree empty")
            return
        qu=deque()
        qu.append(self.root)
        while 1:
            p=qu.popleft()
            print(p.val)
            p=qu.popleft()
            if p.left is not None:
                qu.append(p.left)
            if p.right is not None:
                qu.append(p.right)
    def vertical_value(self):
        m={}
        h=0
        self.vertical_value_(self.root,h,m)
        print(m)
        print(sorted(m))
        for k,v in enumerate(sorted(m)):
            for i in m[v]:
                print(i,end=" ")
            print()
    def vertical_value_(self,p,h,m):
        if p is None:
            return
        try:
            m[h].append(p.val)
        except:
            m[h]=[p.val]  
        self.vertical_value_(p.left,h-1,m)
        self.vertical_value_(p.right,h+1,m)

    def inorder__(self):
        p=self.root
        while p:
            if p.left is None:
                print(p.val,end=" ")
                p=p.right
            else:
                pr=p.left
                while(pr.right is not None and pr.right != p):
                    pr = pr.right
  
            # Make current as right child of its inorder predecessor
                if(pr.right is None):
                    pr.right = p
                    p = p.left
                     
                # Revert the changes made in if part to restore the 
                # original tree i.e., fix the right child of predecssor
                else:
                    pr.right = None
                    print (p.val,0end=" ")
                    p = p.right
                
bt=Binary_tree()
bt.create_bt()
#bt.display()
#bt.inorder()
print()
#print(bt.height())
#bt.level_order()
#bt.level_order()
bt.inorder__()
"""
     1
  2     3
4   6
12346
23
1
"""
