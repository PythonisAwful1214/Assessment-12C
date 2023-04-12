def update_string(string1, string2, index):
    print(string1[:index] + string2 + string1[index+1:])
update_string("Hello World", 'yup', 3)