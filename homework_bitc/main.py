# # # class Car:
# # #     NAME = 'car'
# # #     DESCRIPTION = 'it runs'
# # #     car_count = 0
# # #
# # #     def __init__(self, name, color, year):
# # #         self.car_name = name
# # #         self.color = color
# # #         self.year = year
# # #
# # #
# # #     @classmethod
# # #     def add_count(cls):
# # #         car_count +=1
# # #
# # # print(Car.add_count)
# # # mercedes = Car("CLA 200", 'red', 2014)
# # # bmw = Car("X6", 'black', 2013)
# # # # test = Car("CLA 200", 'red', 2014)
# # # test = mercedes
# # # print(test.car_name)
# # # # print(mercedes == test)
# # # # # print(Car.car_count)
# # # #
# # # # name, job email
# # # #present, cahnge email
# # # class Person(object):
# # #     def __init__(self, name, job, email):
# # #         self.name = name
# # #         self.job = job
# # #         self.email = email
# # #
# # #     def present(self):
# # #         print(f"Hi I am {self.name}. I work as {self.job}  and my email is {self.email}")
# # #
# # #     def change_email(self, new_email):
# # #         self.validate_email(new_email)
# # #         self.email = new_email
# # #
# # #     def validate_email(self, new_email):
# # #         if "@" not in new_email:
# # #             raise ValueError("wrong type of email")
# # #         return new_email
# # #
# # #
# # # #
# # # # test_1 = Person("test1", "test2", "test2")
# # # # test_1.present()
# # # # test_1.change_email("aaa@")
# # # # test_1.present()
# # # dict_1 ={"a": 1, "b":2}
# # # dict_2 ={"a": 1, "b":2}
# # # print(dict_1 ==dict_2)
# # #
# # # class Letter_count(object):
# # #     def __init__(self, text):
# # #         self.text = text
# # #
# # #     def letters_dictionary(self) -> dict:
# # #         new_dict = {}
# # #         for item_ in self.text:
# # #             if item_ not in new_dict:
# # #                 new_dict[item_] = self.text.count(item_)
# # #         return new_dict
# # #
# # #     def remove_duplicate_values(self) -> dict:
# # #         dict_={}
# # #         my_dict = self.letters_dictionary()
# # #         for item_ in my_dict:
# # #             if my_dict[item_] not in dict_.values():
# # #                 dict_[item_] = my_dict[item_]
# # #         return dict_
# # #
# # #     def max_three_values(self) -> list:
# # #         my_dict = self.letters_dictionary()
# # # #         dict_= sorted(my_dict.values())
# # # #         return dict_[::-1][:3]
# # # #
# # # #
# # # #
# # # # test = 'cajsnsjndjsndnsjdnjsndjsndjsn'
# # # # a= Letter_count(test)
# # # # # # b=a.letters_dictionary()
# # # # # b = a.remove_duplicates()
# # # # b=a.max_three_values()
# # # # # a = {"a":5, "B":10, "c":8}
# # # # # b=sorted(a.values())
# # # # print(b)
# # #
# # # # class Circle(object):
# # # #     def __init__(self, radius):
# # # #         self.radius = radius
# # # #
# # # #     def circle_area(self):
# # # #         return f"The area of the circle is {3.14 * self.radius **2}"
# # # #
# # # #     def circle_perimeter(self):
# # # #         return f"The perimeter of the circle is {2 * 3.14 * self.radius}"
# # # #
# # # # a = Circle(3)
# # # # print(a.circle_area())
# # # # print(a.circle_perimeter())
# # #
# # class Rectangle(object):
# #     def __init__(self, length, width):
# #
# #         self.length = self.validate_attribute(length)
# #         self.width = self.validate_attribute(width)
# #
# #
# #     @staticmethod
# #     def validate_attribute(value):
# #         if type(value) != int or value <= 0:
# #             raise ValueError("wrong value")
# #         return value
# #     # def area(self):
# #     #     return self.length * self.width
# # #
# # #     def perimeter(self):
# # #         return 2*(self.length + self.width)
# # #
# # #     def diagonal(self):
# # #         return (self.length**2 + self.width**2)**0.5
# # #
# # #     def present(self):
# # #         print(f"The area is {self.area()}, the perimeter is {self.perimeter()} and the diagonal is {self.diagonal()}")
# # #
# # #
# # # a = Rectangle(3,4)
# # # # b = a.area()
# # # # c = a.perimeter()
# # # # d = a.diagonal()
# # # # print(b, c, d)
# # # a.present()
# # # a=5
# # # # b=5
# # # # c=5
# # # # print(a==b==c)
# # # #
# # # class A:
# # #     pass
# # #
# # # c = Rectangle(5,4)
# # # d = Rectangle(5,4)
# # # # dict_1 = {c: 3}
# # # # print(dict_1[c])
# # # # a=(1,2,3)
# # # # b=(1,2,3)
# # # # print(hash(a)) #529344067295497451
# # # # print(hash(c))
# # # # # print(hash(d))
# # # # a = [1,2,3,[4,5]]
# # # # b = a[::]
# # # # print(b)
# # # # a[3].append(0)
# # # # a.append(10)
# # # # print(b)
# # # #
# # # # print(a)
# # #
# # person_1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
# # person_1_availability = ['9:00', '20:00']
# # person_2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
# # person_2_availability = ['10:00', '18:30']
# # 30
# # # sample output = [['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]
# # can_1 = []
# # for i in range(len(person_1)-1):
# #     if person_1_availability[0] != person_1[0][0]:
# #         can_1.append([person_1_availability[0], person_1[0][0]])
# #     if person_1[i][1] != person_1[i+1][0]:
# #         can_1.append([person_1[i][1],person_1[i+1][0] ])
# #     if person_1_availability[1] != person_1[-1][1]:
# #         can_1.append([person_1[-1][1], person_1_availability[1]])
# #
# # def change_to_numbers(list_):
# #     new_list_ = []
# #     for item_ in list_:
# #         if type(item_) == list:
# #             new_item=[]
# #             for i in item_:
# #                 new_item.append(int(i.replace(':','')))
# #             new_list_.append(new_item)
# #         else:
# #             new_list_.append(int(item_.replace(':', '')))
# #     return new_list_
# # #
# # # elif len(list_) == 1:
# # # for i in list_:
# # #     new_list_.append(int(i.replace(':', '')))
# # # print(change_to_numbers(person_1))
# # # print(change_to_numbers(person_1_availability))
# # #
# # def check_available_times_meeting_minutes(busy_times_, availability_):
# #     busy_times = change_to_numbers(busy_times_)
# #     availability = change_to_numbers(availability_)
# #     new_list = []
# #     if availability[0] < busy_times[0][0]:
# #         new_list.append([availability[0], busy_times[0][0]])
# #     for i in range(len(busy_times)-1):
# #         if busy_times[i][1] < busy_times[i + 1][0]:
# #             new_list.append([busy_times[i][1], busy_times[i + 1][0]])
# #     if busy_times[-1][1] < availability[1]:
# #         new_list.append([busy_times[-1][1], availability[1]])
# #
# #     return new_list
# # p1=check_available_times_meeting_minutes(person_1, person_1_availability)
# # print(p1)
# # p2=check_available_times_meeting_minutes(person_2, person_2_availability)
# # print(p2)
# # def compare(list_1, list_2):
# #     possible_times = []
# #     for i in list_1:
# #         for j in list_2:
# #             if i[1] > j[0] and i[0] < j[1]:
# #                 new_list = i + j
# #                 new_list = sorted(new_list)
# #                 possible_times.append(new_list[1:3])
# #     return possible_times
# #
# # result = compare(p1, p2)
# # print(result)
# # #
# # # def final(list_, minutes):
# # #     new_list = []
# # #     for i in list_:
# # #         if str(i[1]).endswith("00")
# # #         if i[1]x=
# # x=list[9]
# # print(type(x))
#
# class A:
#     pass
# class B(A):
#     pass
# class C(B):
#     pass
# a = C()
#
# print(issubclass(C,A))

# a = [[2000,2005], [1990, 2005], [2005,2010], [1980, 1995]]
# b= []
# for i in a:
#     b +=i
# print(b)
# min_year = min(b)
# max_year = max(b)
# my_dict = {}
# for i in range(min_year, max_year+1):
#     my_dict[i] = 0
#     for j in a:
#         if j[0] <= i <= j[1]:
#             my_dict[i] +=1
# print(my_dict)
# max_ = 0
# key_ = 0
# for i in my_dict:
#     if my_dict[i] >= max_:
#         max_ = my_dict[i]
#         key_ = i
# print(key_, my_dict[key_])

# a = [(2000,2005), (1990, 2005), (2005,2010), (1980, 1995)]
# b= []
# for i in a:
#     b += range(i[0], i[1]+1)
#
# print(b)
# from statistics import mode
# print(mode(b))
#
# #
# import abc
#
# a = ["Apple", "Apple", "Apple", "Banana", "Orange", "Apple", "Orange", "Apple"]
# #
# type1, type2 = a[0], a[1]
# max_len = 0
# count_ = []
# continue_check = True
# for j in range(len(a)):
#     type_1 = a[j]
#     while continue_check:
#         for i in range(1,len(a)):
#             type2 = a[i]
#             if type1 != type2:
#                 example_list = [type1, type2]
#                 break
#         continue_check = False
#     max_len = 0
#     for k in a:
#         print(example_list)
#         if k in example_list:
#             max_len += 1
#     count_.append(max_len)

# my_list = ["Apple", "Apple", "Apple", "Orange", "Orange", "Orange","Banana", "Orange", "Apple", "Orange", "Apple"]
# pairs = []
# for j in range(len(my_list)):
#     possible_pairs = [my_list[j]]
#     for i in my_list[j:]:
#         if i not in possible_pairs:
#             possible_pairs.append(i)
#             possible_pairs = sorted(possible_pairs)
#         if len(possible_pairs) == 2:
#             if possible_pairs not in pairs:
#                 pairs.append(possible_pairs)
#             break
# max_count = 0
# for j in pairs:
#     count = 0
#     for i in my_list:
#         if i in j:
#             count += 1
#         else:
#             break
#     if count >=max_count:
#         max_count = count
#
# # print(max_count)
# my_list = ["Apple", "Apple", "Apple", "Orange", "Orange", "Orange","Banana", "Orange", "Apple", "Orange", "Apple"]
# pairs = []
# for j in range(len(my_list)-1):
#     possible_pairs = [my_list[j:j+2]]
#     if possible_pairs[0] == possible_pairs[1]:
#
#     # if
#     print(possible_pairs)

#     for i in my_list[j:]:
#         if i not in possible_pairs:
#             possible_pairs.append(i)
#             possible_pairs = sorted(possible_pairs)
#         if len(possible_pairs) == 2:
#             if possible_pairs not in pairs:
#                 pairs.append(possible_pairs)
#             break
# max_count = 0
# for j in pairs:
#     count = 0
#     for i in my_list:
#         if i in j:
#             count += 1
#         else:
#             break
#     if count >=max_count:
#         max_count = count
# #
# # print(max_count)
# #
# #
#
# print(possible_pairs)


# import collections
#
#
# class Solution(object):
#     def totalFruit(self, tree):
#         """
#         :type tree: List[int]
#         :rtype: int
#         """
#         count = collections.defaultdict(int)
#         print(count)
#         result, i = 0, 0
#         print(list(enumerate(tree)))
#         for j, v in enumerate(tree):
#             count[v] += 1
#             while len(count) > 2:
#                 count[tree[i]] -= 1
#                 if count[tree[i]] == 0:
#                     del count[tree[i]]
#                 i += 1
#             result = max(result, j-i+1)
#         return result
#
#
# my_list = ["Apple", "Apple", "Apple", "Orange", "Orange", "Orange","Banana", "Orange", "Apple", "Orange", "Apple"]
# #
# # a = Solution()
# # # print(a.totalFruit(my_list))
# # print(len({"a":3, "b":5}))
# from collections import Counter
# a= "scndljkcnwdsjkcnjdsncjnjnjn"
# b=[1,2,3,6,44,4,4,4,4]
# print(Counter(a))
# print(Counter(b))
# my_a=Counter(a)
# print(max(my_a.values()))
# print(my_a.most_common(1))
# print(my_a.keys())

# def num_coins(cents):
#     number_coins = 0
#     coin_types = [25, 10, 1]
#     for i in coin_types:
#         if cents > 0 and cents//i > 0:
#             count_ = cents//i
#             number_coins += count_
#             cents -= (i * count_)
#     return number_coins
#
# print(num_coins(30))
#
# class Shape(ABC):
#     @abc.abstractmethod
#     def area(self):
#         # print("hello from A")
#         pass
#
#     def present(self):
#         print("hello")
#
#     @abc.abstractmethod
#     def perimeter(self):
#         pass
# from abc import ABC
# class Triangle(ABC):
#     def __init__(self, side_1, side_2, side_3):
#         self.side_1 = side_1
#         self.side_2 = side_2
# #         self.side_3 = side_3
# #     # __hash__ = None
# # a= Triangle(1,3,2.5)
# # # b = {a: 5}
# # # print(b[a])
# # print(a.__dict__)
# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)
#
# print(next(myit))
# print(next(myit))
# print(next(myit))
#
# test_1 = "ABCD"
# test2 = test_1[::-1]
# print(test2)
# b=reversed(test_1)
# print(b)
#
# def reversed_string(x):
#     return reversed(x)
# print(reversed_string("ABCD"))

a = [4, 12, 9, 5, 6]
b = [4, 9, 12, 6]
# def return_missing_item(list_1, list_2):
#     if len(list_1)>=len(list_2):
#         search_list = list_1
#         from_list = list_2
#     else:
#         search_list = list_2
#         from_list = list_1
#     for i in search_list:
# #         if i not in from_list:
# #             return i#
# def return_missing_item(list_1, list_2):
#     set_1 = set(list_1)
#     set_2 = set(list_2)
#
#     return set_1.difference(set_2)
#
# set_1 = set(a)
# set_2 = set(b)
# print(sum(a)-sum(b))
#
# #
# # print(return_missing_item(a, b))
#
# word_list = ['bgg', "fbg", "ffq", "fqf", "gfg"]
# a= list(set(''.join(word_list)))
# alph_dict = dict()
# for i in range(len(a)):
#     alph_dict[i] = None
# print(alph_dict)
#
#
# # b= list(set(a))
# # print(b)
# print(a)
# #first letters
# order = []
# # while len(order)<len(a):
# for i in word_list:
#     if i[0] not in order:
#         order.append(i[0])
# for i in range(len(order)):
#     alph_dict[i]=order[i]
#
# for i in range(len(word_list)-1):
#     if word_list[i][0] = word_list[i+1][0]
#         if word_list[i][1] not in alph_dict.values():
#
#
# print(alph_dict)
#
# word_list = ['bgg', "fbg", "ffq", "fqfb", "gfg"]
# first_letter = word_list[0][0]
# for i in word_list:
#     if first_letter in i:
#         compare = i[:(i.index(first_letter))]
# #
#
#
# print(compare)


# print(order)
# first_letter = word_list[0][0]
# print(word_list[0][0], "->", word_list[1][0], "->", word_list[1][0])


import json
from datetime import datetime

class MyJSONEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, datetime):
            return str(o)
        elif isinstance(o, User):
            return o.to_json()
        elif isinstance(o, set):
            return list(o)
        else:
            super().default(o)

class User:
    def __init__(self, name, surname, created_at = datetime.now()):
        self.name = name
        self.surname = surname
        self.created_at = created_at

    def to_json(self):
        return {"name":self.name, "surname": self.surname, "created_at": self.created_at}



user_1 = User("John", "Dohn")

user_2 = User("Mike", "Dohn")
def insert_user_to_json(user_as_dict):
    with open("user.json", "r") as json_file:
        users = json.load(json_file)
        # json.dump([], json_file)

    users.append(user_as_dict)

    with open("user.json", "w") as json_file:
        json.dump(users, json_file, indent=4, cls=MyJSONEncoder)



user_list = [user_1, user_2]
new_list = [[n, user] for n, user in enumerate(user_list, start=1)]
# print(new_list)
# for user in user_list:
#     insert_user_to_json(user)

# print(json.dumps(new_list, cls=MyJSONEncoder))
print(json.dumps({1,5}, cls=MyJSONEncoder))

