import random

def random_list():
    how_long = random.randint(0,20)
    list = []
    while(how_long > 0):
        list.append(random.randint(0,100))
        how_long = how_long - 1
    return list

def list_average(list):
    total = 0
    for x in list:
        total += x
    avg = total/len(list)
    return avg

my_list = random_list()
print("List: ")
for x in my_list:
    print(x)
avg = list_average(my_list)
print("Average:" + str(avg))
