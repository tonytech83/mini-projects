from copy import deepcopy


class CustomList:

    def __init__(self):
        self.__values = []

    def append(self, value):
        """
        The method appends received value to self.__values list. The value can be int/str/float/etc.
        """
        self.__values.append(value)

    def remove(self, index):
        """
        The method removes element form self.__values if index is valid. Raises error when received index is not valid
        index or integer.
        """
        try:
            return self.__values.pop(index)
        except IndexError:
            raise IndexError("Invalid index")
        except TypeError:
            raise ValueError("Index is not a valid integer")

    def get(self, index):
        """
        Returns the value on the index.
        """
        try:
            return self.__values[index]
        except IndexError:
            raise IndexError("Invalid index")
        except TypeError:
            raise ValueError("Index is not a valid integer")

    def extend(self, iter_obj):
        """
        Appends the iterable to the list. Returns the new list.
        """
        try:
            self.__values.extend(iter_obj)
            return deepcopy(self.__values)
        except TypeError:
            raise ValueError("Object not an iterable")

    def insert(self, index, value):
        """
        Adds the value on the specific index. Returns the list.
        """
        try:
            if not isinstance(index, int):
                raise ValueError

            if index < 0 or index >= len(self.__values):
                raise IndexError

            self.__values.insert(index, value)
            return self.__values
        except ValueError:
            raise ValueError("Index is not a valid integer")
        except IndexError:
            raise ValueError("Invalid index")

    def pop(self):
        """
        Removes the last value and returns it.
        """
        try:
            return self.__values.pop()
        except IndexError:
            raise ValueError("Can not pop element form empty list!")

    def clear(self):
        """
        Removes all values, contained in the list.
        """
        self.__values = []

    def index(self, value):
        """
        Returns the index of the given value.
        """
        try:
            return self.__values.index(value)
        except ValueError:
            raise ValueError("The value not exists in the list!")

    def count(self, value):
        """
        Returns the number of times the value is contained in the list.
        """
        try:
            if value not in self.__values:
                raise ValueError
            value_count = len([x for x in self.__values if x == value])
            return value_count
        except ValueError:
            raise ValueError("Not such value in the list")

    def reverse(self):
        """
        Returns the values of the list in reverse order.
        """
        reversed_lst = []

        for i in range(len(self.__values) - 1, -1, -1):
            reversed_lst.append(self.__values[i])

        return reversed_lst

    def copy(self):
        """
        Returns a copy of the list.
        """
        return deepcopy(self.__values)

    def size(self):
        """
        Returns the length of the list.
        """
        return len(self.__values)

    def add_first(self, value):
        """
        Adds the value at the beginning of the list.
        """
        self.__values.insert(0, value)

    def dictionize(self):
        """
        Returns the list as a dictionary: The keys will be each value on an even position and their values
        will be each value on an odd position. If the last value on an even position, it’s value will be " " (space).
        """
        if len(self.__values) % 2 != 0:
            self.__values.append(" ")

        return dict(zip(self.__values[::2], self.__values[1::2]))

    def move(self, amount):
        """
        Move the first "amount" of values to the end of the list. Returns the list.
        """
        if len(self.__values) < amount:
            raise Exception("Elements amount is bigger than size of the list")

        first_amount = self.__values[:amount]
        second_amount = self.__values[amount:]

        self.__values = []
        self.__values = second_amount + first_amount

        return self.__values

    def sum(self):
        """
        Returns the sum of the list. If the value is not a number, add the length of the value to the overall number.
        """
        elements_sum = 0

        for el in self.__values:
            if isinstance(el, int) or isinstance(el, float):
                elements_sum += el
            else:
                elements_sum += len(el)

        return elements_sum

    def overbound(self):
        """
        Returns the index of the biggest value. If the value is not a number, check it’s length.
        """
        if not self.__values:
            raise Exception("The list is empty")

        biggest_value = -float('inf')
        biggest_value_index = 0
        for idx, value in enumerate(self.__values):
            if isinstance(value, int) or isinstance(value, float):
                if value > biggest_value:
                    biggest_value = value
                    biggest_value_index = idx
            else:
                if len(value) > biggest_value:
                    biggest_value = len(value)
                    biggest_value_index = idx

        return biggest_value_index

    def underbound(self):
        """
        Returns the index of the smallest value. If the value is not a number, check it’s length.
        """
        if not self.__values:
            raise Exception("The list is empty")

        smallest_value = float('inf')
        smallest_value_index = 0
        for idx, value in enumerate(self.__values):
            if isinstance(value, int) or isinstance(value, float):
                if value < smallest_value:
                    smallest_value_index = value
                    smallest_value_index = idx
            else:
                if len(value) < smallest_value:
                    smallest_value = len(value)
                    smallest_value_index = idx

        return smallest_value_index

    def __str__(self):
        return f'[{", ".join(str(x) for x in self.__values)}]'




custom_list = CustomList()
# custom_list.index('a')

# print(custom_list.pop())
# custom_list.insert(5, 'b')
# custom_list.insert(0, 'c')
#
# print(custom_list)
