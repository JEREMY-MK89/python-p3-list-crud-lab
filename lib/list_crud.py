def create_an_empty_list():
    return []

def create_a_list():
    return [0, 1, 2, 3]

def add_element_to_end_of_list(lst, element):
    lst.append(element)#my_list.append(new_element)=lst.append(element)
    return lst
# My Original list
my_list = [0, 1, 2, 3]
# Assigned my new variabele as New_Element to add
new_element = 4
updated_list = add_element_to_end_of_list(my_list, new_element)

print(updated_list)

def add_element_to_start_of_list(lst, element):
    lst.insert(0,element)#my_list.insert(0, element)
    return lst
    # My Original list
my_list = [0, 1, 2, 3]
# Assigned my new variabele as New_Element to add
new_element = 5 
updated_list = add_element_to_start_of_list(my_list, new_element)
print(updated_list)

def remove_element_from_end_of_list(l):
    l.pop()# my_list.pop()
    return l
 # My Original list
my_list = [0, 1, 2, 3]
updated_list = remove_element_from_end_of_list(my_list)
print(updated_list)


def remove_element_from_start_of_list(lst):
    del (lst[0])# del(my_list[0])
    return lst
# My Original list
my_list = [0, 1, 2, 3]
updated_list = remove_element_from_start_of_list(my_list)
print(updated_list)

def retrieve_first_element_from_list(lst):
    return lst[0]# my_list
# My Original list
my_list = [0, 1, 2, 3]
updated_list = retrieve_first_element_from_list(my_list)
print(updated_list)

def retrieve_element_from_index(lst, index):
    return lst[index]#my_list[index]=1st=my_list
# My Original list
my_list = [0, 1, 2, 3]
updated_list = retrieve_element_from_index(my_list, 2)# from test index==2
print(updated_list)


def retrieve_last_element_from_list(lst):
    return lst[-1]#my_list[-1]=1st=my_list
# My Original list
my_list = [0, 1, 2, 3, 4]
updated_list = retrieve_last_element_from_list(my_list)# from test index==4
print(updated_list)