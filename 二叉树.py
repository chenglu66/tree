# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 15:28:48 2017

@author: Lenovo-Y430p
"""
#二叉树的构造，插入，删除，遍历，最大值，最小值，判断是否为平衡树
class Node(object):
    def __init__(self,val=0):
        self.val=val
        self.left=None
        self.right=None
class tree(object):
    def __init__(self):
        pass
    def createtree(self,root,a,left,right):#递归创建树
        if left>=right:
            return None
        if left<right:
            mid=(left+right)//2
            root=Node(a[mid])
            root.left=self.createtree(root.left,a,left,mid)
            root.right=self.createtree(root.right,a,mid+1,right)
            return root
def main():
    a=[1,2,3,4,5,6,7,8,9]
    root=Node(0)
    t=tree()
    root=t.createtree(root,a=a,left=0,right=len(a))
    temp=[]
    qianxu(root,temp)
    print(temp)
    temp1=[]
    zhongxu(root,temp1)
    print(temp1)
    temp2=[]
    houxu(root,temp2)
    print(temp2)
    height=depth(root,0)
    print(height)
    numbers=getleaf(root,1)
    print(numbers-1)
    temp3=find(root,10)
    print(temp3)
    #insert(root,11)
    temp4=[]
    zhongxu(root,temp4)
    print(temp4)
    #findpaent(root,2)
    delte(root,3)
    temp5=[]
    zhongxu(root,temp5)
    print(temp5)
    
    
#前序遍历
def qianxu(root,temp):
    if root==None:
        return None
    else:
        temp.append(root.val)
        qianxu(root.left,temp)
        qianxu(root.right,temp)
#中序遍历（可获得二叉查找树的排序方式  
def zhongxu(root,temp):
    if root==None:
        return None
    else:
        zhongxu(root.left,temp)
        temp.append(root.val)
        zhongxu(root.right,temp)
#后续遍历
def houxu(root,temp):
    if root==None:
        return None
    else:
        houxu(root.left,temp)
        houxu(root.right,temp)
        temp.append(root.val)
#层次遍历
def chengxu(root):
    b=[]
    if root==None:
        return b
    for i in range(1,200):
        temp=[]
        getNode(root,i,temp)
        b.append(temp)
    return b
def getNode(root,level,temp):
    if level==1:
        temp.append(root.val)
        return 
    if root.left:
        getNode(root.left,level-1,temp)
    if root.right:
        getNode(root.right,level-1,temp)
def depth(root,height):
    if root==None:
        return height
    lheight=depth(root.left,height+1)
    rheight=depth(root.right,height+1)
    return max(lheight,rheight)
def getleaf(root,numbers):
    if root==None:
        return numbers
    lnumbers=getleaf(root.left,numbers)
    rnumbers=getleaf(root.right,numbers)
    return lnumbers+rnumbers
#查找需要的值
def find(root,value):
    if root==None:
        print(" 不能找到需要的值，可以使用插入操作")
        return -1
    if root.val==value:
        print("找到了需要的值")
        return root
    if root.val>value:
        return find(root.left,value)
    elif root.val<value:
        return find(root.right,value)
#插入需要的值,对插入值要考虑异常
def insert(root,value):
    if type(value)==type(str(11)):
        raise Exception("这不是需要的变量类型，注意格式，这里只接受数值的数据")
    if root==None:
        print("插入该节点到%s" %str(root))
        root=Node(value)
        print(root.val)
        return root
    if root.val==value:
        print("该节点以存在在树中，不需要继续插入")
        return root
    else:
        if root.val<value:
            root.right=insert(root.right,value)
        elif root.val>value:
            root.left=insert(root.left,value)
        if root.val!=value:
            return root
def findpaent(root,value):
    if root==None:
        print("树中并未出现%d并不用删除"%value)
    if root.left:
        if root.left.val==value:
            print(root.val,root.left.val)
            return root,root.left,'left'
    if root.right:
        if root.right.val==value:
            print(root.val,root.right.val)
            return root,root.right,'right'
    if root.val>value:
        findpaent(root.left,value)
    elif root.val<value:
        findpaent(root.left,value)
    else:
        return None
def delte(root,value):
    parent,root,flag=findpaent(root,value)
    if parent!=None and root!=None:
       if root.left==None and root.right==None:
           del(root)
           return 
       elif root.left==None or root.right==None:
           if root.left==None:
               if flag=='right':
                   parent.right=root.right
               else:
                   parent.left=root.right
           else:
               if flag=='right':
                   parent.right==root.left
               else:
                   parent.left==root.right
       else:
            next_time=root.left
            parent_next=next_time
            if parent_next.right==None:
                if flag=='right':
                    parent.right=next_time
                    next_time.right=root.right
                    #parent_next.right=None
                else:
                    parent.left=next_time
                    next_time.right=root.right
                    #next_time.left=root.left
                    #parent_next.right=None
            else:
                while next_time.right!=None and next_time!=None:
                    parent_next=next_time
                    next_time=next_time.right
                if flag=='right':
                    parent.right.val=next_time.val
                    parent_next.right=None
                else:
                    print(next_time.val)
                    parent.left.val=next_time.val
                    #next_time.left=root.left
                    parent_next.right=None
if __name__=='__main__':
    main()

    

        
        