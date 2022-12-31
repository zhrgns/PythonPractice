# 1 find longest word in a list
def longest_word(lst):
    longest_item = ""
    check_length = 1
    for i in lst:
        if(len(i) > check_length):
            check_length = len(i)
            longest_item = i
    return longest_item


# 2 find and make a list with the same items in given lists

def check_same_items(lst1, lst2):
    list_of_sames = []
    for i in lst2:
        if i in lst1 and i not in list_of_sames:
            list_of_sames.append(i)
    return list_of_sames


# 3 Shuffle a given list

import random


def shuffle_my_list(shuffled_list):
    n = len(shuffled_list)

    for i in range(n):
        j = random.randint(0, n)
        item = shuffled_list.pop(j)
        shuffled_list.append(item)
    return shuffled_list


# 4 return the middle 3 characters of a given text

def middle_three_char(input_str):
    if len(input_str) > 2:
        if len(input_str) % 2 == 1:
            chr_index = (len(input_str)//2)
            middle_chr = input_str[chr_index-1:chr_index+2]
            return middle_chr
        else:
            return "Please enter a string with odd length!"
    else:
        return "Length of the given string should be greater than 3!"


# 5 reverse a string type in a string type

def reverse_string(input_str):
    # first step: reversed string 
    reversed_string = ""
    for i in input_str:
        reversed_string = i + reversed_string
    r_str_list = reversed_string.split(" ")

    # second step: made a re_reversed_list from reversed string 
    str_list = []
    n =len(r_str_list)
    for i in range(n):
        str_list.append(r_str_list[n-i-1])

    # third step: join re reversed words
    output_str = ""
    for item in str_list:
        output_str = output_str + " " + item
    return output_str


# 6 find same strings with a list type in given lists

def check_same_item(lst1,lst2):
    sames_list = []
    for item1 in lst1:
        for item2 in lst2:
            if item1 == item2:
                sames_list.append(item1)
    return sames_list


# 7 in given string make letters upper case which have odd index

def make_upper_even_cases(input_str):
    strs = ""
    
    for i in range(0,len(input_str)):
        if i % 2 != 0:
            strs += input_str[i].upper()
        else:
            strs += input_str[i]
    return strs


# 8 check if given words consist of same letters

def same_letter_check(str1,str2):
        #MADE LISTS FROM LETTERS
        letter_list1 = list(str1)
        letter_list2 = list(str2)

        #SORT LIST 1
        sorted_list1 = []
        while letter_list1:
            first_letter = letter_list1[0]
            for item in letter_list1: 
                if item < first_letter:
                    first_letter = item
            sorted_list1.append(first_letter)
            letter_list1.remove(first_letter)
        #SORT LIST 2
        sorted_list2 = []
        while letter_list2:
            first_letter = letter_list2[0]
            for item in letter_list2: 
                if item < first_letter:
                    first_letter = item
            sorted_list2.append(first_letter)
            letter_list2.remove(first_letter)
        
        #CHECK LISTS ARE EQUAL
        if sorted_list1 == sorted_list2:
            return True
        else: return False


# 9 check if given word is a polindrome

def find_palindromes(txt_file):

    input_file = open(txt_file, "r")
    list_lines = input_file.readlines()
    total = 0

    for line in list_lines:
        upper_line = line.upper()
        letter_list = list(upper_line.strip())
        
        reversed_letter_list = []
        n =len(letter_list)
        for i in range(n):
            reversed_letter_list.append(letter_list[n-i-1])

        if reversed_letter_list == letter_list:
            total = total + 1

    return total


    #  10 return distinct words in given *.txt file

def find_distinct_ones(txt_file):
    input_file = open(txt_file,"r")
    lines = input_file.readlines()

    values=[]
    for line in lines:
        lists = line.strip().split()
        values += lists

    fruits= set()
    for value in values:
        fruits.add(value)

    return fruits