# magic
from dataclasses import dataclass


@dataclass
class Person:
    age: int = 8


class MagicList:

    def __init__(self, cls_type=None):
        self.magic_list = []
        self.cls_type = cls_type

        if cls_type is not None:
            self.magic_list.append(cls_type)

    def __len__(self):
        return len(self.magic_list)

    def __repr__(self):
        return 'Object: {}'.format(self.magic_list)

    def __getitem__(self, index):
        return self.magic_list[index]

    def __setitem__(self, index, value):
        if len(self.magic_list) == 0:

            print("==> Initiating Magic list")
            self.magic_list.append(value)
        elif len(self.magic_list) <= index:

            print("==> Out of Range, value was appended")
            self.magic_list.append(value)
        elif len(self.magic_list) > index:

            print("==> Value was set in index")
            self.magic_list[index] = value

    @staticmethod
    def define_item(item):
        if type(item) == int:
            return 'number'
        elif type(item) == object:
            return 'object'
        else:
            print("Item type not supported")


if __name__ == "__main__":

    a = MagicList()
    a[0] = 5
    print(a)
    a[0] = 3
    print(a)
    a[3] = 7
    print(a)
    a = MagicList(Person)
    print(a[0].age)
