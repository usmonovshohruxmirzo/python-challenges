orginal_str = str
orginal_int = int

def int_to_str(num):
    return orginal_str(num)

def str_to_int(num):
    return orginal_int(num)

if orginal_str(4) == "4" and orginal_int("4") == 4:
    print('**EXTRA POINTS**')
    print('You have successfully de-drunken Python')