def get_first():
    first = str(input("Enter first name:"))
    return first

def get_last():
    last = str(input("Enter last name: "))
    return last

def get_full_name(first, last):
    full_name = str(first) + ' ' + str(last)
    return full_name

first_name = get_first()
last_name = get_last()
print(get_full_name(first_name, last_name))
