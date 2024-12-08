immutable_var = (1, 2, 3, True, "Hello")
print(immutable_var)

# immutable_var[0] = 3 - Изменение значений внутри кортежа невозможно потому что данный тип операций не поддерживается

mutable_list = [1, "kraken", 2, 4, True]
print(mutable_list)

mutable_list[0] = "kripto"
print(mutable_list)