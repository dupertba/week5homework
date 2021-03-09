"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    incoming_list = [1,2,3,4,5,6,7,8,9,10]
    max(incoming_list)
    print(incoming_list)

    """
    Required parameter, incoming_list, should be a list.
    
    Find the largest number in the list.
    """
    pass


def find_least_number(incoming_list):
    incoming_list = [1,2,3,4,5,6,7,8,9,10]
    min(incoming_list)
    print(incoming_list)
    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """
    pass


def add_list_numbers(incoming_list):
    incoming_list = [1,2,3,4,5,6,7,8,9,10]
    sum(incoming_list)
    print(incoming_list)
    
    """
    Required parameter, incoming_list, should be a list.
    Add all the values together and return it.
    """

    pass


def longest_value_key(incoming_dict):
    incoming_dict = {'Richmond': 'Virginia',
    'Boston':'Massachusetts',
    'Raleigh': 'North Carolina'}

    biggest_capital = max(incoming_dict, key = lambda x: len(set(biggest_capital[x])))
    print(biggest_capital)
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """
    pass
print("hello")