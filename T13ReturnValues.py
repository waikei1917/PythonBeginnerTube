def allowed_dating_age(my_age):
    girls_age = my_age/2+7
    return girls_age

fish_limit = allowed_dating_age(27)
creep_fish_limit = allowed_dating_age(49)
print("Fish eat", fish_limit, "or older")
print("Fish creep eat", creep_fish_limit, "or older")

