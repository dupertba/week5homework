"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    great_num = max(incoming_list)
    return great_num




def find_least_number(incoming_list):
    least_num = min(incoming_list)
    return least_num
  



def add_list_numbers(incoming_list):

    if incoming_list:
        sum_list = sum(incoming_list)
    else:
        sum_list = 0
    return sum_list




def longest_value_key(incoming_dict):
    long_val = len(max(incoming_dict, key=len))
    return long_val
    


