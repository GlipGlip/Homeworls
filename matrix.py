def get_matrix(n, m, value):
    if n <= 0 or m <= 0:
        return []


    matrix = []

    for i in range(n):
        row = []

        for j in range(m):
            row.append(value)

        matrix.append(row)

    return matrix

result_1 = get_matrix(3,5,7)
result_2 = get_matrix(2,5,4)
result_3 = get_matrix(5,3,8)
result_4 = get_matrix(0,3,5)

print(result_1)
print(result_2)
print(result_3)
print(result_4)