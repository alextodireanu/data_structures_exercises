# implementation of simple linked list

class Node:
    """Class representing a node"""
    def __init__(self, data):
        """Node initialization"""
        self.data = data
        self.next = None  # pointing to None at init


class LinkedList:
    """Class used to represent a linked list structure"""
    def __init__(self):
        """Linked list init"""
        self.head = None

    def print_list(self):
        """Method used to print the list"""
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        """Method used to push a new head to the list"""
        new_node = Node(new_data)
        new_node.next = self.head  # linking the new head to the old head
        self.head = new_node

    def append(self, new_data):
        """Method to add a new tail to the list"""
        new_node = Node(new_data)
        # checking if we have a linked list
        # if not, the new node will be the head of the list
        if self.head is None:
            self.head = new_node
            return
        # going through the list until reaching the last node
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_after(self, prev_node, new_data):
        """Method to add a new node to the list after a given node"""
        # checking if a previous node exists
        if prev_node is None:
            return
        # creating a new node and linking it to the prev and next nodes
        temp = prev_node.next
        new_node = Node(new_data)
        prev_node.next = new_node
        new_node.next = temp


if __name__ == '__main__':
    # creating a linked list and its nodes
    linked_list = LinkedList()
    linked_list.head = Node(1)
    second_node = Node(2)
    third_node = Node(3)

    # linking the head with the next node
    linked_list.head.next = second_node
    second_node.next = third_node
    linked_list.push(0)
    linked_list.append(4)
    linked_list.insert_after(second_node, 4)
    linked_list.print_list()
