class Node:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val


class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = None

    
    def addNodeInLinkedList(self, val):
        node = Node(val)

        if self.head is None:
            self.head = node
            self.tail = node
            self.size = 1
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            self.size +=1

    def removeNode(self, val):

        if self.head.val is val:
            tempNode = self.head
            self.head = tempNode.next
            self.head.prev = None
            del tempNode
        elif self.tail.val is val:
            tempNode = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            del tempNode
        else:
            tempNode = self.head
            while  tempNode is not None:
                if tempNode.val == val:
                    tempNode.prev.next = tempNode.next
                    tempNode.next.prev = tempNode.next
                    self.size -= 1
                    del tempNode
                    return

            tempNode = tempNode.next
           


    def printLinkedList(self):
        vals = []
        node = self.head
        while node is not None:
           vals.append(node.val)
           node = node.next

        return f"[{', '.join(str(val) for val in vals)}]"



if __name__ =="__main__":
    llist = LinkList()

    LinklistNum = list(map(int, input().split()))
    for i in LinklistNum:
        llist.addNodeInLinkedList(i)
    
    print(llist.printLinkedList())
    print(llist.size)

    llist.removeNode(5)

    print(llist.printLinkedList())
    print(llist.size)
