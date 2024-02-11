class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        self.index = 0


class MyLinkedList:

    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:

        current = self.head

        while current:

            if current.index == index:
                return current.value

            current = current.next

        return -1

        

    def addAtHead(self, val: int) -> None:

        current = Node(val)
        temp = self.head
        self.head = current
        current.next = temp

        temp2 = self.head
        index = 0
        while temp2:
            temp2.index = index
            index += 1
            temp2 = temp2.next



        

    def addAtTail(self, val: int) -> None:

        current = self.head

        tail_node = Node(val)

        if not self.head:
            self.head = tail_node

            return

        while current.next:
            current = current.next

        current.next = tail_node
        tail_node.index = current.index + 1


        

    def addAtIndex(self, index: int, val: int) -> None:

        current = self.head

        new_node = Node(val)

        if index == 0:
            if self.head:
                temp = self.head
                self.head = new_node
                new_node.next = temp
            
                curr = self.head

                ind = 0

                while curr:
                    curr.index = ind
                    ind += 1
                    curr = curr.next

            else:
                self.head = new_node


        while current:

            if current.index == index - 1:
                temp = current.next
                current.next = new_node
                new_node.next = temp

                new_node.index = index

                curr = new_node.next

                ind = index + 1

                while curr:
                    curr.index = ind
                    ind += 1

                    curr = curr.next

            current = current.next




  

    def deleteAtIndex(self, index: int) -> None:

        current = self.head

        if self.head and index == 0:
            self.head = self.head.next
        
            curr = self.head

            ind = 0

            while curr:
                curr.index = ind
                ind += 1
                curr = curr.next


        while current:

            if current.next and current.index == index - 1:

                current.next = current.next.next

                curr = current.next

                ind = current.index + 1

                while curr:
                    curr.index = ind
                    ind += 1
                    curr = curr.next

            current = current.next















        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
