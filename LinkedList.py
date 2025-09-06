# Here, self is the variable that refers to the instance of the class on which the object is called/
# MyList.print_list() --> self will refer to the instance of the MyList object.
class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None

    """
    Created By Meet Gandhi on 06/09/2025 | Method to get the Length of linked list
    """
    def len_list(self):
        node = self.head
        i = 0
        while node:
            node = node.next_node
            i += 1
        return i

    """
    Created By Meet Gandhi on 06/09/2025 | Method to print the given linked list.
    """
    def print_list(self):
        node = self.head
        while node:
            print(node.value, end='->')
            node = node.next_node
        print("None")

    """
    Created By Meet Gandhi on 06/09/2025 | Method to add the new node at the end of the linked list.
    """
    def add_element(self, new_node):
        if not self.head:
            self.head = new_node
            return
        node = self.head
        while node.next_node != None:
            node = node.next_node
        node.next_node = new_node

    """
    Created By Meet Gandhi on 06/09/2025 | Method the add the element at the start of the linked list.
    """
    def add_startelement(self, new_node):
        if not self.head:
            self.head = new_node
            return
        node = self.head
        new_node.next_node = node
        self.head = new_node

    """
    Created By Meet Gandhi on 06/09/2025 | Method to add the Node at ith position in Linked List.
    """
    def add_ithelement(self,position,new_node):
        node = self.head
        length_list = self.len_list()

        if position > length_list:
            print("Index out of Bound")
            return

        if position == 1:
            new_node.next_node = node
            self.head = new_node
            return

        i = 1
        while node and i != (position - 1):
            node = node.next_node
            i += 1

        new_node.next_node = node.next_node
        node.next_node = new_node
    """
    Created By Meet Gandhi on 06/09/2025 | Method for removing the last element from the linked list.
    """
    def delete_lastnode(self):
        if not self.head:
            print("No element in the LinkedList")
            return
        if not self.head.next_node:
            self.head = None
            return
        node = self.head
        while node.next_node.next_node != None:
            node = node.next_node
        node.next_node = None

    """
    Created By Meet Gandhi on 06/09/2025 | Method for removing the kth element from the linked list.
    Case 1: check for the list whether its empty or not.
    Case 2: check whether the list has one element or not.
    Case 3: Also check for the last element and the index that is passed whether is in bound or not.
    """
    def remove_Kthelement(self,k):
        node = self.head
        if not node.next_node:
            if k == 1:
                self.head = None
            else:
                print("Index out of bound.....")
        else:
            temp = node.next_node
            i = 2
            if k == 1:
                self.head = temp
            elif k > 1:
                while temp and i != k:
                    temp = temp.next_node
                    node = node.next_node
                    i += 1
                if not temp:
                    print("Index out of bound error.")
                else:
                    node.next_node = temp.next_node
            elif k <= 0:
                print("Invalid index")

    """
    Created By Meet Gandhi on 06/09/2025 | Removing the element with particular value from the list.
    """
    def remove_value(self,value):
        node = self.head
        if not node:
            print("Linked List is empty")
        else:
            if not node.next_node:
                if node.value == value:
                    self.head = None
                else:
                    print(f"{value} does not exists")
            else:
                if node.value == value:
                    self.head = node.next_node
                    return
                temp = node.next_node
                while temp and temp.value != value:
                    temp = temp.next_node
                    node = node.next_node
                if not temp:
                    print(f"{value} does not exists")
                else:
                    node.next_node = temp.next_node