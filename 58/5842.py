# _*_ coding : utf-8 _*_
class Tree(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value == value:
            return self

    def insert_left(self, value):
        if self.left is None:
            self.left = Tree(value)

    def insert_right(self, value):
        if self.right is None:
            self.right = Tree(value)

    def show(self):
        print(self.value)
        if self.left is not None:
            self.left.show()
        if self.right is not None:
            self.right.show()
