grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students = sorted(students)

m_b_dict = {}

for student, grade_list in zip(students, grades):
    m_b = sum(grade_list) / len(grade_list)
    m_b_dict[student] = m_b

print(m_b_dict)

