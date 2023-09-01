class MySet:
    def __init__(self, enumerable=[]):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):
        return value in self.dictionary

    def add(self, value):
        self.dictionary[value] = True
        return self

    def delete(self, value):
        self.dictionary.pop(value, None)
        return self

    def size(self):
        return len(self.dictionary)

    def clear(self):
        self.dictionary.clear()

    def __str__(self):
        set_list = [str(key) for key in self.dictionary.keys()]
        return f'MySet: {{{",".join(set_list)}}}'

# Display results in the VS Code terminal
if __name__ == '__main__':
    # Create an empty set
    empty_set = MySet()
    print(empty_set)  # Output: MySet: {}

    # Create a set with initial values
    my_set = MySet([1, 2, 3, 3, 4, 4])
    print(my_set)  # Output: MySet: {1,2,3,4}

    # Test has method
    print(my_set.has(2))  # Output: True
    print(my_set.has(5))  # Output: False

    # Test add method
    my_set.add(5)
    print(my_set)  # Output: MySet: {1,2,3,4,5}

    # Test delete method
    my_set.delete(3)
    print(my_set)  # Output: MySet: {1,2,4,5}

    # Test size method
    print(my_set.size())  # Output: 4

    # Test clear method
    my_set.clear()
    print(my_set)  # Output: MySet: {}
