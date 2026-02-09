if __name__ == '__main__':
    N = int(input())


class UserList:
    def __init__(self):
        self.my_list = []

    def insert(self, index, value):
        self.my_list.insert(int(index), int(value))

    def print(self):
        print(self.my_list)

    def remove(self, value):
        self.my_list.remove(int(value))

    def append(self, value):
        self.my_list.append(int(value))

    def sort(self):
        self.my_list.sort()

    def pop(self):
        self.my_list.pop()

    def reverse(self):
        self.my_list = self.my_list[::-1]


l = UserList()
for _ in range(N):
    command, *args = input().split()
    getattr(l, command)(*args)