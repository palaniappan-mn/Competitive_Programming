class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_node):
        """
        This method is used to add element to the end of the linked list
        """
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert(self, new_node):
        """
        This method is used to insert element to the beginning of the linked list
        """
        new_node.next = self.head
        self.head = new_node

    def display(self):
        """
        This method is used to visualize the linked list created
        """
        temp_node = self.head
        while temp_node != None:
            print(temp_node.val, end='->')
            temp_node = temp_node.next
        print('Null')

    def delete(self, val):
        """
        This method is used to delete a particular value from the linked-list
        """
        if self.head.val == val:
            self.head = self.head.next
            return print("Node Deleted")
        else:
            pointer = self.head
            while pointer is not None:
                if pointer.next is None:
                    return print("Node not found")
                elif pointer.next.val == val:
                    pointer.next = pointer.next.next
                    return print("Node Deleted")
                else:
                    pointer = pointer.next




if __name__ == '__main__':
    linked_list = LinkedList()

    linked_list.append(Node(1))
    linked_list.append(Node(2))
    linked_list.append(Node(3))
    linked_list.append(Node(4))
    linked_list.append(Node(5))
    linked_list.append(Node(6))
    linked_list.append(Node(7))
    linked_list.append(Node(8))
    linked_list.append(Node(9))
    linked_list.append(Node(10))
    linked_list.insert(Node(0))
    linked_list.delete(0)

    linked_list.display()
