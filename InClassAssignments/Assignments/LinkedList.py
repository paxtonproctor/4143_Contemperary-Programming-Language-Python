class Node: 
    def __init__(self, data = None): 
        self.data = data
        self.next = None
        
    
class LinkedList:
    def __init__(self, nodes = None):
        self.head = None
        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node
            for element in nodes:
                node.next = Node(element) 
                node = Node.next


def __repr__(self):
    node = self.head
    nodes = []
    
    while node is not None:
        nodes.append(node.data)
        node = Node.next
    
    nodes.append("None")
    return "->".join(nodes)                
        

l1 = ['B', 'C', 'D', 'E']
LL1 = LinkedList(l1)
