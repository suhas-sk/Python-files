class A:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

obj = A('Suhas')
print(obj)