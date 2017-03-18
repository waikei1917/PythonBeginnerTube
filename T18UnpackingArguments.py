def health_calculator(age, apple_ate, cigs_smoked):
    answer = (100-age) + (apple_ate * 3.5) - (cigs_smoked *2 )
    print(answer)

fish_data = [27,20,0]

health_calculator(fish_data[0],fish_data[1],fish_data[2])
health_calculator(*fish_data)

