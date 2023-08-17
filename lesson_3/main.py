# Task 1

# 1.1 erku dzevov el karanq bayc ete array-ov anenq amen inchvor jamanaky mek append aneluc
# hishoxutyan mech nor tex enq allocate anelu, dra hamar erevi Linked Listov.

# 1.2 qani vor hertova aveli optimal klni Linked Listov

# Task 2

class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

    def set_next(self, next):
        self.__next = next

    def get_next(self):
        return self.__next


class LinkedList:
    def __init__(self, head=None):
        self.__head = head

    def is_empty(self):
        return self.__head is None

    def add(self, item):
        node = Node(item)
        node.set_next(self.__head)
        self.__head = node

    def size(self):
        current = self.__head
        size = 0
        while current is not None:
            current = current.get_next()
            size += 1
        return size

    def remove(self, target):
        current_node = self.__head
        prev_node = None

        while current_node is not None:

            if current_node.get_data() == target:
                if isinstance(prev_node, Node):
                    prev_node.set_next(current_node.get_next())
                else:
                    self.__head = current_node.get_next()
                return True

            prev_node = current_node
            current_node = current_node.get_next()
        return False

    def search(self, target):
        current_node = self.__head

        while current_node is not None:
            if current_node.get_data() == target:
                return True
            current_node = current_node.get_next()
        return False

    def __iter__(self):
        self.current_node = self.__head
        return self

    def __next__(self):
        current_node = self.current_node
        if current_node is None:
            raise StopIteration
        current_value = current_node.get_data()
        self.current_node = current_node.get_next()
        return current_value

    def __str__(self):
        if self.__head is None:
            return '[]'
        current = self.__head
        result = '[' + str(current.get_data()) + ', '
        while not current.get_next() is None:
            current = current.get_next()
            result += str(current.get_data()) + ', '
        return result + ']'


linked_sequence = LinkedList()

linked_sequence.add(10)
linked_sequence.add(20)
linked_sequence.add(30)
linked_sequence.add(40)
linked_sequence.add(50)
linked_sequence.add(60)


for elem in linked_sequence:
    print(elem)


# Research
# 1.	Dynamic Array

# Dynamic array-y hamematac static arrayneri runtime gorcoxutyunnera anum takic.

# Dynamic array@ iranic entadruma vor petqa inqy mi qani karevor harcer vercni ira vra,
# Dynamic Sizing => tarbervuma static array-ic vorovhetev fixvac size chuni u dynamic dzevi size-@ kara poxvi
# Memory Managment => kaxvac array-i chapic memory-in manage-a anum kaxvac arrayi chapic nor taracq kara allocate ani hishoxutyan mech
# Ira mech inchvor ban insert aneluc time complexity-n O1-a vonc haskaca
