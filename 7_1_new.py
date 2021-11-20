class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        return '\n'.join(map(str, self.my_list))

    def __add__(self, other):
        my_list_sum = []
        l = range(len(self.my_list))
        for i in l:
            my_sum = []
            for j in l:
                e = self.my_list[i][j] + other.my_list[i][j]
                my_sum.append(e)
            my_list_sum.append(my_sum)
        return my_list_sum


my_list = [[1, 2, 3], [5, 6, 7], [8, 9, 10]]
my_list2 = [[1, 2, 3], [5, 6, 7], [8, 9, 10]]
a = Matrix(my_list)
b = Matrix(my_list2)
w = Matrix(a + b)
print(w)
