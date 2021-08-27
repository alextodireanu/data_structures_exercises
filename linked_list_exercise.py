# create a linked list data structure with the following methods:
# remove head, remove tail, remove a node from user input

class Node:
    """Class representing a node"""
    def __init__(self, data):
        """Node initialization"""
        self.data = data
        self.next = None


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

    def remove_head(self):
        """Method used to remove the head of the list"""
        if self.head is None:
            print("No linked list, nothing to remove")
            return
        temp = self.head.next
        self.head = temp

    def remove_tail(self):
        """Method used to remove the tail of the list"""
        if self.head is None:
            print("No linked list, nothing to remove")
            return
        temp = self.head
        if temp.next is None:
            self.head = None
            return
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def remove_user_input(self):
        """Method used to remove a node based on user input"""
        linked_list.print_list()
        user_input = int(input("Type the value you want to delete -> "))
        temp = self.head
        prev = self.head

        # checking if the head has the value that needs to be deleted
        if temp:
            if temp.data == user_input:
                self.head = temp.next
                linked_list.print_list()
                return
        else:
            print("No linked list")
            return

        while temp:
            if temp.data == user_input:
                break
            prev = temp
            temp = temp.next
        else:
            print("Value not found!")
            return

        # removing the value from the list and linking the previous node with the next one
        prev.next = temp.next
        linked_list.print_list()


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.head = Node(3)
    second_node = Node(-2)
    third_node = Node(7)
    fourth_node = Node(0)

    linked_list.head.next = second_node
    second_node.next = third_node
    third_node.next = fourth_node

    linked_list.remove_head()
    linked_list.remove_tail()
    linked_list.remove_user_input()
    linked_list.print_list()