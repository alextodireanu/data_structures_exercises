# Create a stack data structure using linked list that has the following methods
# get_size()– Get the number of items in the stack.
# is_empty() – Return True if the stack is empty, False otherwise.
# peek() – Return the top item in the stack. If the stack is empty, raise an exception.
# push(value) – Push a value into the head of the stack.
# pop() – Remove and return a value in the head of the stack. If the stack is empty, raise an exception.
# print_stack() - To print the values

class Node:
    """Representation of a node"""
    def __init__(self, data):
        """Node initialization"""
        self.data = data
        self.next = None


class LinkedStack:
    """Representation of a linked stack structure"""
    def __init__(self):
        """Initializing the stack"""
        self.head = None
        self.length = 0

    def get_size(self):
        """Method to get the length of the stack"""
        if self.length != 0:
            print(f'The length of the stack is {self.length}')

        else:
            print('Empty stack!')

    def is_empty(self):
        """Method to determine if the stack is empty"""
        if self.length == 0:
            return True
        else:
            return False

    def peek(self):
        """Method to return the value of the head"""
        if not self.is_empty():
            print(f"The head value of the stack is {self.head.data}")
        else:
            raise IndexError("Empty Stack")

    def push(self, new_data):
        """Method to push a new value as the new head"""
        if self.head is None:
            self.head = Node(new_data)
        else:
            new_node = Node(new_data)
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop_value(self):
        """Method to pop and return the head value"""
        if self.is_empty() is True:
            raise IndexError("Empty Stack!")
        else:
            popped_value = self.head.data
            self.head = self.head.next
            self.length -= 1
            print(f'The popped value is {popped_value}')

    def print_stack(self):
        """Method to print the stack"""
        if not self.is_empty():
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.next
        else:
            print("Empty stack!")

    @staticmethod
    def app_start():
        """Method to initiate the app"""
        print('Hello, please see below the available options:\n')
        options = {1: 'get size',
                   2: 'check if empty',
                   3: 'peek',
                   4: 'push',
                   5: 'pop',
                   6: 'print stack',
                   7: 'quit'}
        for key, option in options.items():
            print(f'{key}.{option}')
        LinkedStack.validate_user_data()

    @staticmethod
    def validate_user_data():
        """Method to gather and validate the user's input"""
        while True:
            try:
                user_option = int(input('\nPlease type the corresponding number for the selected option -> '))
            except ValueError:
                print("Only numbers are accepted!")
                break
            else:
                if user_option == 1:
                    stack.get_size()
                elif user_option == 2:
                    print(stack.is_empty())
                elif user_option == 3:
                    stack.peek()
                elif user_option == 4:
                    push_value = input('Please type the value you want to push -> ')
                    stack.push(push_value)
                elif user_option == 5:
                    stack.pop_value()
                elif user_option == 6:
                    stack.print_stack()
                elif user_option == 7:
                    print('Bye bye!')
                    break
                else:
                    print('Option not available, please try again!')


if __name__ == '__main__':
    stack = LinkedStack()
    stack.app_start()
