#!/usr/bin/python3

from_json_string = __import__('4-from_json_string').from_json_string

s_my_list = "[1, 2, 3]"

my_list = from_json_string(s_my_list)

print(s_my_list)
print(type(s_my_list))

s_my_dict = """ {
    'id' : 12,
    'name' : "John",
    'places' : ['San Francisco', 'Tokyo'],
    'is_active' : True,
    'info': {
        'age' : 36,
        'average' : 3.14
    }
}"""
my_dict = from_json_string(s_my_dict)
print(my_dict)
print(type(my_dict))

try:
    s_my_dict =""" {"is_active" : True, 12} """
    
    my_dict = from_json_string(s_my_dict)
    print(my_dict)
    print(type(my_dict))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))