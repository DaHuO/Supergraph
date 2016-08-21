class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def addVal(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            r = self.head
            while r.next is not None:
                r = r.next
            n = Node(val)
            r.next = n

    def deleteNode(self, n):
        if n is not None:
            if self.head is n:
                self.head = self.head.next
            else:
                r = self.head
                while (r.next is not None) and (r.next is not n):
                    r = r.next
                if r is not None:
                    r.next = n.next
    def deleteMidNodeVal(self, n):
        if n.next is not None:
            n.val = n.next.val
            n.next = n.next.next
    def printVals(self):
        r = self.head
        while r is not None:
            print r.val
            r = r.next
    
    def removeDups(self):
         r = self.head
         while r is not None:
             rn = r.next
             while rn is not None:
                 if rn.val == r.val:
                     self.deleteNode(rn)
                 rn = rn.next
             r = r.next
    def removeDups2(self):
        if self.head is not None:
            pr = self.head
            r = pr.next
            valDic = {self.head.val:self.head}
            while r is not None:
                if r.val in valDic:
                    pr.next = r.next
                    r = r.next
                else:
                    r = r.next
                    pr = pr.next
    def nthToLast(self, n):
        r = self.head
        res = self.head
        c = 0
        while r.next is not None:
            r = r.next
            if c >= n:
                res = res.next
            else:
                c = c + 1
        if c == n:
            return res
        else:
            return None
def sumLinkedListNums(n1,n2):
    if n1 is None or n2 is None:
        return None
    r1 = n1.head
    r2 = n2.head
    o = 0
    res = LinkedList()
    while r1 is not None and r2 is not None:
        o, val = divmod(r1.val + r2.val + o, 10)
        res.addVal(val)
        r1 = r1.next
        r2 = r2.next
    remNode = [r2, r1] [r2 is None]

    while remNode is not None:
        o, val = divmod(remNode.val + o, 10)
        res.addVal(val)
        remNode = remNode.next
    return res

def findHeadOfCycle(l):
    if l is not None and l.head is not None and l.head.next is not None:
        lazy = l.head
        normal = lazy.next
        fast = normal.next
        while normal is not None and fast is not None:
            if fast == lazy:
                return lazy
            if normal == fast:
                lazy = lazy.next
            normal = normal.next
            fast = fast.next.next
                
n8 = Node(8)
n7 = Node(7, n8)            
n6 = Node(6, n7)
n5 = Node(5, n6)
n4 = Node(4, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)
n8.next = n4
l = LinkedList()
l.head = n1
print(findHeadOfCycle(l).val)



    
