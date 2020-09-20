
class Menu():

    def show_menu(self):
        print("1. Add matrices\n"
              "2. Multiply matrix by a constant\n"
              "3. Multiply matrices\n"
              "4. Transpose matrix\n"
              "5. Calculate a determinant\n"
              "6. Inverse matrix\n"
              "0. Exit\n")
        self.ask_for_action()

    def ask_for_action(self):
        action = input('Your choice: ')
        self.start_activity(action)

    def start_activity(self, action):
        if int(action) == 1:
            self.add_matrices()
        elif int(action) == 2:
            self.multiply_by_constant()
        elif int(action) == 3:
            self.multiply_matrices()
        elif int(action) == 4:
            self.transpose_matrix()
        elif int(action) == 5:
            self.calculate_determinant()
        elif int(action) == 6:
            self.inverse_matrix()
        elif action == "Exit":
            return None

    def add_matrices(self):
        n, m = [int(a) for a in input('Enter size of first matrix: ').split()]
        print('Enter first matrix:')
        matrix_a = [[float(a) for a in input().split()] for line in range(n)]


        n2, m2 = [int(a) for a in input('Enter size of second matrix: ').split()]
        print('Enter second matrix:')
        matrix_b = [[float(a) for a in input().split()] for line in range(n)]

        if (n == n2) & (m == m2):
            matrix_c = []
            print('The result is:')
            for line in range(n):
                matrix_c.append([])
                for item in range(m):
                    matrix_c[line].append(matrix_a[line][item] + matrix_b[line][item])
                result_matrix = " ".join([str(elem) for elem in matrix_c[line]])
                print(result_matrix)
            print()

        else:
            print('The operation cannot be performed.\n')

        self.show_menu()

    def multiply_by_constant(self):
        n, m = [int(a) for a in input('Enter size of matrix: ').split()]
        print('Enter matrix:')
        matrix_a = [[int(a) for a in input().split()] for line in range(n)]

        c = int(input('Enter constant: '))

        matrix_c = []
        print('The result is:')
        for line in range(n):
            matrix_c.append([])
            for item in range(m):
                matrix_c[line].append(matrix_a[line][item] * c)
            result_matrix = " ".join([str(elem) for elem in matrix_c[line]])
            print(result_matrix)
        print()

        self.show_menu()

    def multiply_matrices(self):
        n, m = [int(a) for a in input('Enter size of first matrix: ').split()]
        print('Enter first matrix:')
        matrix_a = [[float(a) for a in input().split()] for line in range(n)]

        n2, m2 = [int(n) for n in input('Enter size of second matrix: ').split()]
        print('Enter second matrix:')
        matrix_b = [[float(a) for a in input().split()] for line in range(n2)]

        if m == n2:
            matrix_c = []
            print('The result is:')
            for row in range(n):
                matrix_c.append([])
                for column in range(m2):
                    new_matrix_item = 0
                    for item in range(m):
                        new_matrix_item += matrix_a[row][item] * matrix_b[item][column]
                    matrix_c[row].append(new_matrix_item)
                result = " ".join([str(elem) for elem in matrix_c[row]])
                print(result)
            print()
        else:
            print('The operation cannot be performed.\n')

        self.show_menu()

    def transpose_matrix(self):
        print("1. Main diagonal\n"
        "2. Side diagonal\n"
        "3. Vertical line\n"
        "4. Horizontal line\n")
        transpose_type = int(input('Your choice: '))

        n, m = [int(a) for a in input('Enter matrix size: ').split()]
        print('Enter matrix:')
        matrix_a = [[float(a) for a in input().split()] for line in range(n)]

        if transpose_type == 1:
            self.main_diagonal_transpose(n, m, matrix_a)
        elif transpose_type == 2:
            self.side_diagonal_transpose(n, m, matrix_a)
        elif transpose_type == 3:
            self.vertical_transpose(n, m, matrix_a)
        elif transpose_type == 4:
            self.horizontal_transpose(n, m, matrix_a)

    def main_diagonal_transpose(self, n, m, matrix_a):
        matrix_c = []
        print('The result is:')

        for row in range(n):
            matrix_c.append([])
            for column in range(m):
                new_matrix_item = matrix_a[column][row]
                matrix_c[row].append(new_matrix_item)

        for row in range(n):
            result_matrix = " ".join([str(elem) for elem in matrix_c[row]])
            print(result_matrix)

        self.show_menu()

    def side_diagonal_transpose(self, n, m, matrix_a):
        matrix_c = []
        print('The result is:')

        for row in range(n):
            matrix_c.insert(0, [])
            for column in range(m):
                new_matrix_item = matrix_a[column][row]
                matrix_c[0].insert(0, new_matrix_item)

        for row in range(n):
            result_matrix = " ".join([str(elem) for elem in matrix_c[row]])
            print(result_matrix)

        self.show_menu()

    def vertical_transpose(self, n, m, matrix_a):
        matrix_c = []
        print('The result is:')

        for row in range(n):
            matrix_c.append([])
            for column in range(m):
                new_matrix_item = matrix_a[row][column]
                matrix_c[row].insert(0, new_matrix_item)

        for row in range(n):
            result_matrix = " ".join([str(elem) for elem in matrix_c[row]])
            print(result_matrix)

        self.show_menu()

    def horizontal_transpose(self, n, m, matrix_a):
        matrix_c = []
        print('The result is:')

        for row in range(n):
            matrix_c.insert(0, [])
            for column in range(m):
                new_matrix_item = matrix_a[row][column]
                matrix_c[0].append(new_matrix_item)

        for row in range(n):
            result_matrix = " ".join([str(elem) for elem in matrix_c[row]])
            print(result_matrix)

        self.show_menu()

    def calculate_determinant(self):
        n, m = [int(a) for a in input('Enter matrix size: ').split()]
        print('Enter matrix:')
        matrix_a = [[float(a) for a in input().split()] for line in range(n)]

        print('The result is: ')
        print(self.determinant(n, matrix_a))
        print()
        self.show_menu()

    def determinant(self, n, matrix_a, total=0):
        indices = list(range(len(matrix_a)))
        if n == 1:
            return matrix_a[0][0]
        elif n == 2:
            return matrix_a[0][0] * matrix_a[1][1] - matrix_a[0][1] * matrix_a[1][0]
        else:
            for j in indices:
                sub_matrix_a = [row[:] for row in matrix_a]
                sub_matrix_a = sub_matrix_a[1:]
                height = len(sub_matrix_a)

                for i in range(height):
                    sub_matrix_a[i] = sub_matrix_a[i][0:j] + sub_matrix_a[i][j+1:]

                sign = (-1) ** (j % 2)

                total += sign * matrix_a[0][j] * self.determinant(n - 1, sub_matrix_a)
        return total

    def inverse_matrix(self):
        n, m = [int(a) for a in input('Enter matrix size: ').split()]
        print('Enter matrix:')
        matrix_a = [[float(a) for a in input().split()] for line in range(n)]

        if n <= 2:
            print("This matrix doesn't have an inverse.\n")
            self.show_menu()

        else:
            matrix_c = self.count_cofactors_matrix(matrix_a)
            matrix_d = []
            print('The result is:')
            for line in range(n):
                matrix_d.append([])
                for item in range(m):
                    matrix_d[line].append(matrix_c[item][line] * (1 / self.determinant(n, matrix_a)))
                result_matrix = " ".join([str(elem) for elem in matrix_d[line]])
                print(result_matrix)

        self.show_menu()

    def count_cofactors_matrix(self, matrix_a):
        indices = list(range(len(matrix_a)))
        if len(matrix_a) == 2:
            return matrix_a[0][0] * matrix_a[1][1] - matrix_a[0][1] * matrix_a[1][0]
        else:
            cofactor_matrix = []
            for i in indices:
                cofactor_matrix.append([])
                sub_matrix_a = [row[:] for row in matrix_a]
                sub_matrix_a = sub_matrix_a[0:i] + sub_matrix_a[(i+1):]
                height = len(sub_matrix_a)

                indices_a = list(range(len(sub_matrix_a[0])))
                for z in indices_a:
                    sub_matrix_b = [row[:] for row in sub_matrix_a]
                    for j in range(height):
                        sub_matrix_b[j] = sub_matrix_a[j][0:z] + sub_matrix_a[j][z+1:]

                    cofactor = (-1) ** (i + 1 + z + 1) * (self.determinant(len(sub_matrix_b), sub_matrix_b))
                    cofactor_matrix[i].append(cofactor)

            return cofactor_matrix

        #     for j in indices:
        #         sub_matrix_a = [row[:] for row in matrix_a]
        #         sub_matrix_a = sub_matrix_a[1:]
        #         height = len(sub_matrix_a)
        #
        #         for i in range(height):
        #             sub_matrix_a[i] = sub_matrix_a[i][0:j] + sub_matrix_a[i][j+1:]
        #
        #         sign = (-1) ** (j % 2)
        #
        #         total += sign * matrix_a[0][j] * self.determinant(n - 1, sub_matrix_a)
        # return total


processor = Menu()
processor.show_menu()


