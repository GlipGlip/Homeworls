import random

slot_1 = random.randrange(3,21)
slot_2 = []

for i in range(slot_1):
    for j in range(slot_1):

        if i <= j:
            continue

        if i !=0 and j != 0 and slot_1 % (i+j) == 0:

            slot_2.append((i,j))


print("Ячейка: " + str(slot_1))
print("Пароль:" + str(slot_2))