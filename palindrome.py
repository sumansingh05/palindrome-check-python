class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    #function to check the linked list is empty or not 
    def is_empty(self):
        return self.head is None
    
    #function to add a node at the last of the linked list 
    def addLast(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode            
        else:
            self.tail.next = newNode            
        self.tail = newNode
        self.count += 1

    #function to print the linked list
    def display(self):
        current = self.head
        print("Singly Linked List is: ",end=" ")
        while current is not None:
            print(current.data,end=" ")
            current = current.next
        print()

    #function to reverse the singly linked list
    def reverseList(self):
        current = self.head
        prev = None
        next = None

        while(current):
            next = current.next
            current.next = prev
            prev = current
            current = next 

        self.tail = self.head
        self.head = prev
        self.tail.next = None

    #function to find the mid element int the linked list
    def findMid(self):
        slow = self.head
        fast = self.head

        while(fast != None  and  fast.next != None):
            slow = slow.next
            fast = fast.next.next

        return slow       

    #function to check the linked list is palidrome or not    
    def checkPalindrome(self):
        if self.head is None  or  self.head.next == None:
            return True
        # find mid node of linked list
        midNode = self.findMid() 

        # reverse second half
        prev = None
        current = midNode
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        right = prev #right half head
        left = self.head

        #check left half and right half
        while right is not None:
            if left.data is not right.data:
                return False
            left = left.next
            right = right.next

        return True 

ll = SLL()
ll.addLast(1)
ll.addLast(2)
ll.addLast(3)
ll.addLast(4)
ll.addLast(5)
ll.display()
# print(ll.checkPalindrome())
ll.reverseList()
ll.display()