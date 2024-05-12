import random

FILE_INPUT = "matrix.txt"
determinant_znak = 1
external_matrix = []

def read_len_console():
    while True:
        try:
            number = int(input("Enter number of unknowns: <= 20 "))
            if 1 <= number <= 20:
                return number
            else:
                print("The number must be from 1 to 20.")
        except ValueError:
            print("Error number format")



def gaussian_elimination(matrix):
    global external_matrix
    n = len(matrix)

    # Прямой ход метода Гаусса
    for i in range(n):
        if matrix[i][i] == 0:
            for j in range(i + 1, len(matrix)):
                if matrix[j][0] != 0:  # Находим первую ненулевую строку
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    break
        # Приведение к единичной диагонали
        for k in range(i + 1, n):
            factor = matrix[k][i] / matrix[i][i]
            for j in range(i, n + 1):
                matrix[k][j] -= factor * matrix[i][j]
    external_matrix = matrix
    for row in matrix:
        if all(element == 0 for element in row[:-1]) and row[-1] != 0:
            print("Error: The system of equations has no solutions")
            return None
    # Обратный ход метода Гаусса
    solution = [0] * n
    for i in range(n - 1, -1, -1):
        solution[i] = matrix[i][n] / matrix[i][i]
        for k in range(i - 1, -1, -1):
            matrix[k][n] -= matrix[k][i] * solution[i]
    return solution

def gaussian_elimination(matrix):
    global external_matrix
    n = len(matrix)

    # Прямой ход метода Гаусса
    for i in range(n):
        # Проверяем, равен ли главный элемент нулю
        if matrix[i][i] == 0:
            # Ищем строку, где элемент в текущем столбце не равен нулю
            for j in range(i + 1, n):
                if matrix[j][i] != 0:
                    # Меняем местами строки
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    global determinant_znak
                    determinant_znak = -1
                    break
            else:
                print("Error: The system of equations has no solutions")
                return None

        # Приведение к единичной диагонали
        pivot = matrix[i][i]
        for k in range(i + 1, n):
            factor = matrix[k][i] / pivot
            for j in range(i, n + 1):
                matrix[k][j] -= factor * matrix[i][j]

    external_matrix = matrix
    for row in matrix:
        if all(element == 0 for element in row[:-1]) and row[-1] != 0:
            print("Error: The system of equations has many solutions")
            return None
    # Обратный ход метода Гаусса
    solution = [0] * n
    for i in range(n - 1, -1, -1):
        solution[i] = matrix[i][n]
        for j in range(i + 1, n):
            solution[i] -= matrix[i][j] * solution[j]
        solution[i] /= matrix[i][i]
    return solution





def read_matrix_console(n):
    matrix = []

    print("Enter Matrix Coefficients:")
    for i in range(n):
        row = []
        for j in range(n + 1):
            while True:
                try:
                    coefficient = input(f'Enter coefficient a[{i}][{j}]: ')
                    coefficient = coefficient.replace(',', '.')
                    row.append(float(coefficient))
                    break
                except ValueError:
                    print("Error: Please enter a valid number.")
        matrix.append(row)
    return matrix

def is_extended_matrix(matrix):
    if not matrix:
        raise ValueError("Матрица пуста")

    num_rows = len(matrix)
    if num_rows == 0:
        raise ValueError("Матрица пуста")
    num_cols = len(matrix[0])
    # Проверяем, что количество столбцов больше на 1, чем количество строк
    return num_cols == num_rows + 1
def read_matrix_file():
    matrix = []
    try:
        print("Enter file name: ")
        file_name = input()  # Читаем имя файла с консоли
        with open(file_name, 'r') as file:
            for line in file:
                # Разделяем строку по пробелам и преобразуем каждый элемент в число
                line = line.replace(",", ".")
                row = [float(x) for x in line.strip().split()]
                matrix.append(row)
    except FileNotFoundError:
        print("File not found")
        return 1
    except PermissionError:
        print("Permission error")
        return 2
    except ValueError:
        return 3
    except KeyboardInterrupt:
        return 1
    try:
        if not is_extended_matrix(matrix):
            return 3
    except ValueError as e:
        return 3
    return matrix

def generate_random_matrix(n):
    matrix = []
    for _ in range(n):
        row = []
        for _ in range(n + 1):
            row.append(random.randint(0, 99))
        matrix.append(row)
    return matrix


def calculate_determinant(matrix):
    determinant = 1
    for row_index, row in enumerate(matrix):
        determinant *= row[row_index]  # Умножаем элементы на диагонали
    return determinant
def extract_vector_b(matrix):
    # Последний столбец матрицы
    vector_b = [row[-1] for row in matrix]
    return vector_b

def remove_last_column(matrix):
    if not matrix:
        print("Error: Input matrix cannot be empty.")
        return []

    # Проверяем, что все строки матрицы имеют одинаковую длину
    column_lengths = set(len(row) for row in matrix)
    if len(column_lengths) != 1:
        print("Error: Matrix rows have different lengths.")
        return []

    # Удаляем последний элемент из каждой строки матрицы
    result_matrix = [row[:-1] for row in matrix]
    return result_matrix


def compute_residuals(matrix_A, vector_b, vector_x):
    vector_residuals = []
    for i in range(len(vector_b)):
        residual = vector_b[i]
        for j in range(len(vector_x)):
            residual -= matrix_A[i][j] * vector_x[j]
        vector_residuals.append(residual)
    return vector_residuals
def start():
    print("\nHow do you want to enter the coefficients?")
    print("1 - enter from the keyboard")
    print("2 - read from file")
    print("3 - random matrix\n")
    try:
        method = input()
    except Exception:
        print("Error: Could not read input. Exiting.")
        return
    except KeyboardInterrupt:
        return
    while (method != '1') and (method != '2') and (method != '3'):
        print("Enter 1 or 2 or 3:")
        method = input()

    if method == '1':
        try:
            n = read_len_console()
            a = read_matrix_console(n)
        except:
            return
    if method == '2':
        a = read_matrix_file()
        if a == 1:
            return
        if a == 2:
            return
        if a == 3:
            print("Error: matrix format")
            return
    if method == '3':
        try:
            n = read_len_console()
            a = generate_random_matrix(n)
        except:
            return
    if a is None:
        print("Error, please check your input")
        return


    print('\n' 'Matrix:')
    for row in a:
        for element in row:
            print("%.2f" % element, end=' ')
        print('\n')


    solutions = gaussian_elimination(a)
    if solutions is None:
        return
    print('\n' 'Triangular matrix:')
    for row in a:
        for element in row:
            print("%.2f" % element, end=' ')
        print('\n')
    print('Determinant: ', calculate_determinant(external_matrix)*determinant_znak)

    print('\nRequired solution is: ')
    for i in range(len(solutions)):
        print('x%d = %0.2f' % (i, solutions[i]), end='\n')
    print('\n')
    vector_residuals = compute_residuals(remove_last_column(a), extract_vector_b(a), solutions)
    print("Residuals:", vector_residuals)

start()