from typing import TypedDict
# it suggests(warns) not validates the type

class Person(TypedDict):
    name: str
    age: int

new_person: Person = {"name": "Alice", "age": 30}

print(new_person)

