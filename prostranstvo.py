calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    lenght = len(string)
    upper = string.upper()
    lower = string.lower()
    return (lenght,upper,lower)

def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in (item.lower() for item in list_to_search)

info = string_info("Hello world!")
print(info)

print(string_info('Hi'))

contains = is_contains("World", ['world', 'WORLD', "Warld"])
print(contains)

contains = is_contains("Good", ['Giid','gaad','gyOd'])
print(contains)

print(is_contains("Good", ['Giid','gaad','gyOd']))

print(calls)

