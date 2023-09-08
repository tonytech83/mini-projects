class HashTable:

    def __init__(self):
        self.__max_capacity = 4
        self.__keys = [None] * self.__max_capacity
        self.__values = [None] * self.__max_capacity

    def add(self, key: any, value: any):
        """
        Add new key-value pair in HastTable
        """
        self[key] = value

    def get(self, key: any):
        """
        Returns value by key if received key is in self.__keys array
        """
        try:
            return self[key]
        except KeyError as ke:
            return ke

    def delete(self, key):
        """
        Removes key-value pair by key if received key is in self.__keys array
        """
        try:
            idx = self.__keys.index(key)
            self.__keys[idx] = None
            self.__values[idx] = None
        except ValueError:
            raise KeyError(f'Received key "{key}" is not valid key!')


    def __resize_table(self):
        """
        Resized keys and values arrays if they are full.
        """
        self.__keys = self.__keys + [None] * self.__max_capacity
        self.__values = self.__values + [None] * self.__max_capacity
        self.__max_capacity *= 2

    def __setitem__(self, key, value):
        """
        Adds new key and new value into corresponding arrays.
        """
        if key in self.__keys:
            idx = self.__keys.index(key)
            self.__values[idx] = value
            return

        if len(self) == self.__max_capacity:
            self.__resize_table()

        calculated_idx = self.__calc_index(key)
        idx = self.__get_index(calculated_idx)

        self.__keys[idx] = key
        self.__values[idx] = value

    def __getitem__(self, key):
        try:
            index = self.__keys.index(key)
            return self.__values[index]
        except ValueError:
            raise KeyError(f'Received key "{key}" is not valid key!')

    def __calc_index(self, key):
        """
        Calculates the hash from all symbols in key.
        """
        return sum([ord(c) for c in key]) % self.__max_capacity

    def __get_index(self, index):
        """
        Returns next index which is not None.
        """
        if index == self.__max_capacity:
            index = 0

        if self.__keys[index] is None:
            return index

        return self.__get_index(index + 1)

    def __len__(self):
        return len([k for k in self.__keys if k is not None])

    def __str__(self):
        key_value_pair = []
        for idx in range(len(self.__keys)):
            if self.__keys[idx] is not None:
                key_value_pair.append(f"{self.__keys[idx]}: {self.__values[idx]}")

        return "{" + f"{', '.join(key_value_pair)}" + "}"


# Test code
table = HashTable()

table["name"] = "Peter"
table["age"] = 25
table.add('key', 'value')

print(table)
print(table.get("name"))
print(table["age"])
print(len(table))
print(table)

table.delete('age')
print(table)

table.add('test', 'this is test value')
table.add('test', 'this is test value')
print(table)