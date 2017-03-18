def get_gender(sex='Unknown'):
    if sex is 'm' or sex is 'M':
        sex = "Male"
    elif sex is 'f' or sex is 'F':
        sex = "Female"
    print(sex)

get_gender('m')
get_gender('M')
get_gender('f')
get_gender('F')
get_gender()