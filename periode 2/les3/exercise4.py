class Empty:
    def __init__(self):
        self.IsEmpty = True

class Node:
    def __init__(self, value, tail):
        self.IsEmpty = False
        self.Value = value
        self.Tail = tail

list = Empty()
for i in range(1, 5):
    list = Node(i, list)
    print (list.Value)

def reverse(list):
    tmplist = Empty()
    while not list.IsEmpty:
        tmplist = Node(list.Value, tmplist)
        list = list.Tail
        print(tmplist.Value)
reverse(list)
