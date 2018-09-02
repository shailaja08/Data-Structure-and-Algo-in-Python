from collections import deque

class Node:
    def __init__(self,value):
        self.info=value
        self.lchild=None
        self.rchild=None


class Binary:
    def __init__(self):
        self.root=None


    def is_empty(self):
        return self.root==None

    def display(self):
        self._display(self.root,0)
        print()

    def _display(self,p,level):
        if p is None:
            return
        self._display(p.rchild,level+1)
        print()
        for i in range(level):
            print("  ",end=" ")
        print(p.info)
        self._display(p.lchild,level+1)

    def preorder(self):
        self._preorder(self.root)
        #print()
    def _preorder(self,p):
        if p is None:
            return ""
        s=str(p.info)
        if p.lchild is None and p.rchild is not None:
            s+="()("+self._preorder(p.rchild)+")"
        else:
            if p.lchild is not None:
                s+="("+self._preorder(p.lchild)+")"
            if p.rchild is not None:
                s+="("+self._preorder(p.rchild)+")"
        return s

    def inorder(self):
        self._inorder(self.root)
        print()
    def _inorder(self,p):
        if p is None:
            return ()
        self._inorder(p.lchild)
        print(p.info,end=" ")
        self._inorder(p.rchild)

    def postorder(self):
        self._postorder(self.root)
        print()
    def _postorder(self,p):
        if p is None:
            return
        self._postorder(p.lchild)
        self._postorder(p.rchild)
        print(p.info,end=" ")

    def height(self):
        return self._height(self.root)
            
    def _height(self,p):
        if p is None:
            return 0
        hL=self._height(p.lchild)
        hR=self._height(p.rchild)

        if hL>hR:
            return 1+hL
        else:
            return 1+hR
        
    def create_tree(self):
        self.root=Node(5)
        self.root.lchild=Node(2)
        #self.root.lchild.lchild=Node(4)
        self.root.rchild=Node(13)


    def _findTarget(self,k):
        return self.findTarget(self.root,k)
    def findTarget(self,root, k):
        stack, table = [root], set()
        print("stack1", stack)
        while stack!=[]:
            node = stack.pop()
            print("node",node)
            if node is not None:
                if node.info in table:
                    print("node",node.info)
                    return True
                else:
                    table.add(k - node.info)
                    print("table",table)
                stack.extend([node.lchild, node.rchild])
                print("DF",stack)
        return False

    def vertical_value(self):
        m={}
        h=0
        self.vertical_value_(self.root,h,m)
        for k,v in enumerate(sorted(m)):
            for i in m[v]:
                print(i)
    def vertical_value_(self,p,h,m):
        if p is None:
            return
        if h in m.keys():
            m[h].append(p.info)
        else:
            m[h]=p.info  
        vertical_value_(self,p.lchild,h+1,m)
        vertical_value_(self,p.rchild,h-1,m)
root = Node(1)
root.lchild = Node(2)
root.rchild = Node(3)
root.lchild.lchild = Node(4)
root.lchild.rchild = Node(5)
root.rchild.lchild = Node(6)
root.rchild.rchild = Node(7)
root.rchild.lchild.rchild = Node(8)
root.rchild.rchild.rchild = Node(9)

bt=Binary()
bt.display()
print(bt.preorder())
print(bt._findTarget(2))
bt.vertical_value()
