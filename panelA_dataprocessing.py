from utils import *

file_A = open('PanelA_User.txt').readlines()
file_A = file_A[1:]        #remove the first line of the table

## the number of users in Panel A is 49945.


# Establish a dictionary of user information and a city-code dictionary at the same time

all_cities_dict, all_users_dict = {}, {}
user_num, city_num = 1, 1
for line in file_A:
    line = line.split()
    length = len(line)
    user_id, login_date, first_order_date = line[0], line[1], line[3]
    if '市' in line[5] or '区' in line[5] or '州' in line[5]:
        city = line[5]
        is_student = line[6]
        if '.' in line[7]:
            age, gender = line[7], line[8]
            if length == 10:
                zhima = line[9]
            else:
                zhima = '-1'
        else:
            age, gender = '-1', line[7]
            if length == 9:
                zhima = line[8]
            else:
                zhima = '-1'
        if city not in all_cities_dict.keys():
            all_cities_dict[city] = city_num
            city_num += 1

    else:
        city = '-1'
        is_student = line[5]
        if '.' in line[6]:
            age, gender = line[6], line[7]
            if length == 9:
                zhima = line[8]
            else:
                zhima = '-1'
        else:
            age, gender = '-1', line[6]
            if length == 8:
                zhima = line[7]
            else:
                zhima = '-1'

    user_dict = {'user_id':user_id, 'login_date': login_date, 'first_order_date': first_order_date, 'is_student': is_student,
                 'city':city, 'age': age, 'gender': gender, 'zhima': zhima}

    all_users_dict[user_num] = user_dict
    user_num += 1

all_cities_dict = {b:a for a,b in all_cities_dict.items()}
print(len(all_cities_dict))

# There are altogether 211 different cities in this table.