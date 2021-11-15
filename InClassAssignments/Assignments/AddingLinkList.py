class Node:

        # Constructor to initialize the node object
        def __init__(self, data):
                self.data = data
                self.next = None


class LinkedList:

        # Function to initialize head
        def __init__(self):
                self.head = None

        # Function to insert a new node at the beginning
        def push(self, new_data):
                new_node = Node(new_data)
                new_node.next = self.head
                self.head = new_node

        # Add contents of two linked lists and return the head
        # node of resultultant list
        def addTwoLists(self, first, second):
                prev = None
                temp = None
                carry = 0

                # While both list exists
                while(first is not None or second is not None):

                        # Calculate the value of next digit in
                        # resultultant list
                        # The next digit is sum of following things
                        # (i) Carry
                        # (ii) Next digit of first list (if ther is a
                        # next digit)
                        # (iii) Next digit of second list ( if there
                        # is a next digit)
                        fdata = 0 if first is None else first.data
                        sdata = 0 if second is None else second.data
                        Sum = carry + fdata + sdata

                        # update carry for next calculation
                        carry = 1 if Sum >= 10 else 0

                        # update sum if it is greater than 10
                        Sum = Sum if Sum < 10 else Sum % 10

                        # Create a new node with sum as data
                        temp = Node(Sum)

                        # if this is the first node then set it as head
                        # of resultultant list
                        if self.head is None:
                                self.head = temp
                        else:
                                prev.next = temp

                        # Set prev for next insertion
                        prev = temp

                        # Move first and second pointers to next nodes
                        if first is not None:
                                first = first.next
                        if second is not None:
                                second = second.next

                if carry > 0:
                        temp.next = Node(carry)

        # Utility function to print the linked LinkedList
        def printList(self):
                temp = self.head
                while(temp):
                        print(temp.data)
                        temp = temp.next


# Driver code
first = LinkedList()
second = LinkedList()

# Create first list
first.push(2)
first.push(4)
first.push(3)
print("First List is ")
first.printList()

# Create second list
second.push(4)
second.push(6)
second.push(5)
print( "\nSecond List is ")
second.printList()

# Add the two lists and see resultult
result = LinkedList()
result.addTwoLists(first.head, second.head)
print("\nresultultant list is ")
result.printList()