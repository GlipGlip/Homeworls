# Цикл завершается как только доходит до отрицтельного значения

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0

while index < len(my_list):
    if my_list[index] < 0 :
        break
    print(my_list[index])
    index += 1


# Цикл выовдит все значения списка кроме отрицтельных

# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# index = 0
#
# while index < len(my_list):
#     if my_list[index] < 0:
#         index += 1
#         continue
#
#     print(my_list[index])
#     index += 1