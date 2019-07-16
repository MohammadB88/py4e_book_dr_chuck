number_or_string = input(
    'Please indicate if you want to enter a list of numbers or just a string by typing (L or S): \n')
input_list = input('Then enter the object: \n')

if number_or_string == 'L':
    initial_list = [float(i)
                    for i in input_list.strip('[').strip(']').split(',')]
elif number_or_string == 'S':
    initial_list = list(input_list.strip().split())


def chop(input_list):
    first_element = input_list[0]
    last_element = input_list[-1]
    input_list.remove(first_element)
    input_list.remove(last_element)
    print(initial_list)
    return None


def middle(input_list):
    middle_list = input_list.copy()
    first_element = middle_list[0]
    last_element = middle_list[-1]
    middle_list.remove(first_element)
    middle_list.remove(last_element)
    print('The final list without the first and the last item is: \n', middle_list)
    # print(input_list)
    return middle_list


# initial_list = [1, 'asalaaaaa', 'ali', 'mobina', 2, 3, 4, 'fatemeh', 5, 6, 7, 'mahan', 'arshia', 'jigaraaaaaa', 'asdlkadsa']

print('********* chop function has modified the initial list but does not return a new list!!! ***********')
chop(initial_list)
print('********* middle function has modified the initial list and returns a new list!!! ***********')
print('The initial list is: \n', initial_list)
middle(initial_list)
