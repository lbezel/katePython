
from random import randint

general_time = 0
primary_number = 20
longevity = randint (15, 80)
considering_period = 30
min_marry_age = 16 

General_Table = list ()

def creater_new_animals(number, longevity, general_time=0):
    for index  in range(general_time, number, 1):
        sex = randint(0, 1)
        #завести в переменную
        data_birth = general_time + randint(0, 25)
        data_death = data_birth + longevity
        animal = (len(General_Table), None, None, sex, data_birth, data_death)
        General_Table.append (animal)

def cleaner(Cunner_Table, const, nomber = 5):
    for index  in range (len(Cunner_Table)):
            if Cunner_Table [index][nomber] > const:
                Cunner_Table.pop(index)
            index = max(index - 1, 0)


creater_new_animals (10, 60)


print (General_Table)
print("*******************************")
print (len(General_Table))

for index in range (len(General_Table)):
    print (index)
    if General_Table[index][5] > 0:
        print ("ok")
        General_Table.pop (index)
        print ("new long", len(General_Table))
        print ("new index", index)



# for index in range (len(General_Table)):
#     print (index)
#     if General_Table[index][5] > 0:
#         print ("ok")
#         General_Table.pop (index)
#         print ("new long", len(General_Table))
#         print ("new index", index)


# [(0, None, None, 1, 1, 61), (1, None, None, 1, 14, 74), (2, None, None, 0, 10, 70), (3, None, None, 1, 22, 82), (4, None, None, 1, 2, 62), (5, None, None, 1, 21, 81), (6, None, None, 1, 18, 78), (7, None, None, 1, 11, 71), (8, None, None, 1, 21, 81), (9, None, None, 0, 14, 74)]
# *******************************
# 10
# 0
# ok
# new long 9
# new index 0
# 1
# ok
# new long 8
# new index 1
# 2
# ok
# new long 7
# new index 2
# 3
# ok
# new long 6
# new index 3
# 4
# ok
# new long 5
# new index 4
# 5
# Traceback (most recent call last):
#   File "c:\Users\КатЯ\Desktop\katePython\to_test.py", line 37, in <module>
#     if General_Table[index][5] > 0:
# IndexError: list index out of range


#print (General_Table)

# for index in range (len(General_Table)):
#     print (index)
#     if General_Table[index][5] > 0:
#         print ("a")
#         General_Table.pop (index)
# print (General_Table)
# [(0, None, None, 1, 15, 75), (1, None, None, 0, 9, 69), (2, None, None, 0, 7, 67), (3, None, None, 0, 5, 65), (4, None, None, 1, 10, 70), (5, None, 
# None, 1, 19, 79), (6, None, None, 0, 14, 74), (7, None, None, 1, 10, 70), (8, None, None, 1, 8, 68), (9, None, None, 1, 15, 75), (10, None, None, 0, 19, 79), (11, None, None, 0, 4, 64), (12, None, None, 0, 5, 65), (13, None, None, 1, 8, 68), (14, None, None, 0, 19, 79), (15, None, None, 0, 0, 60), (16, None, None, 0, 11, 71), (17, None, None, 0, 10, 70), (18, None, None, 0, 8, 68), (19, None, None, 0, 5, 65)]
# *******************************
# 20
# 0
# a
# 1
# a
# 2
# a
# 3
# a
# 4
# a
# 5
# a
# 6
# a
# 7
# a
# 8
# a
# 9
# a
# 10
# Traceback (most recent call last):
#   File "c:\Users\КатЯ\Desktop\katePython\to_test.py", line 37, in <module>
#     if General_Table[index][5] > 10:
# IndexError: list index out of range








# for index in range (len(General_Table)):
#     print (index)
#     if General_Table[index][5] > 65:
#         print ("a")


# a = 60
# print (min((General_Table[0][5]), len(General_Table)))
# for index in range (len(General_Table)):
#     print ("a", index)
#     print (min(General_Table[index][5], General_Table[index - 1][5]))

# general_time = 40
# for index  in range (len(General_Table)):
#             if General_Table [index][5] > general_time:
#                 General_Table.pop(index)

# print (General_Table)
# print (len(General_Table))


