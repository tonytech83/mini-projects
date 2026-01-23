def get_id[K, V](db: dict[K, V], user: K) -> V:
    return db[user]


users: dict[str, int] = {
    "bob": 0,
    "jams": 1,
    "sandra": 2,
}

value: int = get_id(users, "bob")


# annotate class with generic type
class CustomList[T]:
    def __init__(self, items: list[T]) -> None:
        self.items = items

    def append(self, item: T) -> None:
        self.items.append(item)

    def get_items(self) -> list[T]:
        return self.items

    def remove(self, item: T) -> None:
        if item in self.items:
            self.items.remove(item)


cl: CustomList[int] = CustomList([1, 2, 3])
cl.append(4)
cl.append("a")  # This will work, because the type annotation is not enforced by python
print(cl.get_items())
cl.remove(1)
print(cl.get_items())
