my_list = [1, 2, 3, 4, 5]
def print_element(arg, index):
    try:
        print(arg[index])
    except IndexError as err:
        print("올바른 인덱스를 설정해 주세요! ({0})".format(err))

print_element(my_list, 2)
print_element(my_list, 4)
print_element(my_list, 5)