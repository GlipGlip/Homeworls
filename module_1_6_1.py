# Словарь

my_dict = {"Andrew" : 1999, "Victor" : 2001, "Julia" : 1997, "Katy": 2005, "Gans": 1985}

print(my_dict)

print(my_dict["Andrew"])

print(my_dict.get("Kostya"))

my_dict.update({"Kirill" : 2012,
               "Anna" : 2003})

print(my_dict)

el_pop = my_dict.pop("Victor")

print(my_dict)
print(el_pop)

# Множества

my_set = {1,2,10,8,6,9,2,2,8,3}
print(my_set)

my_set.add(52), my_set.add(34)

print(my_set)

my_set.remove(2)
print(my_set)