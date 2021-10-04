class Node:
    """
    This class initializes an empty node
    """
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_node):
        """
        This method takes in a new node and appends to the end of the linked list
        :param new_node: 
        :return:
        """
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert(self, new_node):
        """
        This method takes in new node and inserts in to the list as the head
        :param new_node: 
        :return: 
        """
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete(self, val):
        """
        This method takes in the value to be deleted and deletes the corresponding node
        :param val: 
        :return: 
        """
        if self.head.val == val:
            self.head.next.prev = None
            self.head = self.head.next
        elif self.tail.val == val:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        else:
            forward_pointer = self.head
            backward_pointer = self.tail
            while forward_pointer is not None and backward_pointer is not None:
                print(forward_pointer, backward_pointer)
                if forward_pointer.next is None and backward_pointer.prev is None:
                    print("Node not found")
                elif forward_pointer.next.val == val:
                    temp = forward_pointer.next.next
                    forward_pointer.next = forward_pointer.next.next
                    temp.prev = forward_pointer
                    return print("Node Deleted")
                elif backward_pointer.prev.val == val:
                    temp = backward_pointer.prev.prev
                    backward_pointer.prev = backward_pointer.prev.prev
                    temp.next = backward_pointer
                    return print("Node Deleted")
                forward_pointer = forward_pointer.next
                backward_pointer = backward_pointer.prev



    def display(self):
        """
        This method is used to visualize the linked list created
        """
        temp_node = self.head
        while temp_node != None:
            print(temp_node.val, end='->')
            temp_node = temp_node.next
        print('Null')
        print('\n')

        temp_node = self.tail
        while temp_node != None:
            print(temp_node.val, end='->')
            temp_node = temp_node.prev
        print('Null')


if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.append(Node(1))
    dll.append(Node(2))
    dll.append(Node(3))
    #dll.insert(Node(0))
    dll.delete(2)

    dll.display()
