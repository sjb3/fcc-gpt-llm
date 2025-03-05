

# class Person:
#     def __init__(self, name:str, address: str):
#         self.name = name    
#         self.address = address

#     def __str__(self) -> str:
#         return f'{self.name} {self.address}'
    

# def main() -> None:
#     person = Person(name='JOHN', address='NONE of your biz')
#     print(person)

## Use dataClass instead

import random
import string
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    address: str
    active: bool = True

    def __repr__(self) -> str:
        return f'{self.name} {self.address} {self.active} '

def main() -> None:
    person = Person(name='JOHN', address='NONE of your biz')
    print(person)

if __name__ == "__main__":
    main()