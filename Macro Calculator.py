
sex = input('Are you a male or a female?' )
if sex == 'male':
    weight = input('What is your weight in lbs?: ')
    height = input('What is your height in feet?: ')
    age = input('What is your age in years?: ')
    print('(1) No formal Exercise')
    print('(2) Light walking or housework, 1 to 3 days a week')
    print('(3) Moderate exercise 3 to 4 days a week')
    print('(4) Moderate to vigorous exercise 5 to 6 days a week')
    print('(5) Vigorous exercise 6 to 7 days a week')
    days_work = input('Rate your activity level from 1-5: ')
    weight = float(weight) * .453592 * 10
    height = float(height) * 30.48 * 6.25
    age = float(age) * 5
    bmr = float(weight) + float(height) - float(age) + 5
    print(f'Base Metabolic Rate (BMR) = {bmr} calories')
    if int(days_work) == 1:
        tdee = float(bmr) * 1.2
        print(f'Total Daily Energy Expenditure (TDEE) = {tdee} calories')
        print('(1) Maintenance')
        print('(2) Cutting')
        print('(3) Recomposition')
        print('(4) Dirty Bulk')
        print('(5) Lean Bulk')
        goal = input('What is your goal? (1-5): ')
        if int(goal) == 1:
            protein_c = float(tdee) * .3
            carb_c = float(tdee) * .4
            fat_c = float(tdee) * .3
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 2:
            tdee = float(tdee) * .8
            protein_c = float(tdee) * .35
            carb_c = float(tdee) * .35
            fat_c = float(tdee) * .3
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 3:
            tdee = float(tdee) * .8
            protein_c = float(tdee) * .4
            carb_c = float(tdee) * .3
            fat_c = float(tdee) * .3
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 4:
            tdee = float(tdee) * 1.1
            protein_c = float(tdee) * .25
            carb_c = float(tdee) * .4
            fat_c = float(tdee) * .35
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 5:
            tdee = float(tdee) * 1.1
            protein_c = float(tdee) * .4
            carb_c = float(tdee) * .4
            fat_c = float(tdee) * .2
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        else:
            print('invalid entry, please only enter numbers (1-5)')
    elif int(days_work) == 2:
        tdee = float(bmr) * 1.375
        print(f'Total Daily Energy Expenditure (TDEE) = {tdee} calories')
        print('(1) Maintenance')
        print('(2) Cutting')
        print('(3) Recomposition')
        print('(4) Dirty Bulk')
        print('(5) Lean Bulk')
        goal = input('What is your goal? (1-5): ')
        if int(goal) == 1:
            protein_c = float(tdee) * .3
            carb_c = float(tdee) * .4
            fat_c = float(tdee) * .3
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 2:
            tdee = float(tdee) * .8
            protein_c = float(tdee) * .35
            carb_c = float(tdee) * .35
            fat_c = float(tdee) * .3
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 3:
            tdee = float(tdee) * .8
            protein_c = float(tdee) * .4
            carb_c = float(tdee) * .3
            fat_c = float(tdee) * .3
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 4:
            tdee = float(tdee) * 1.1
            protein_c = float(tdee) * .25
            carb_c = float(tdee) * .4
            fat_c = float(tdee) * .35
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 5:
            tdee = float(tdee) * 1.1
            protein_c = float(tdee) * .4
            carb_c = float(tdee) * .4
            fat_c = float(tdee) * .2
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        else:
            print('invalid entry, please only enter numbers (1-5)')
    elif int(days_work) == 3:
        tdee = float(bmr) * 1.55
        print(f'Total Daily Energy Expenditure (TDEE) = {tdee} calories')
        print('(1) Maintenance')
        print('(2) Cutting')
        print('(3) Recomposition')
        print('(4) Dirty Bulk')
        print('(5) Lean Bulk')
        goal = input('What is your goal? (1-5): ')
        if int(goal) == 1:
            protein_c = float(tdee) * .3
            carb_c = float(tdee) * .4
            fat_c = float(tdee) * .3
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 2:
            tdee = float(tdee) * .8
            protein_c = float(tdee) * .35
            carb_c = float(tdee) * .35
            fat_c = float(tdee) * .3
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 3:
            tdee = float(tdee) * .8
            protein_c = float(tdee) * .4
            carb_c = float(tdee) * .3
            fat_c = float(tdee) * .3
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 4:
            tdee = float(tdee) * 1.1
            protein_c = float(tdee) * .25
            carb_c = float(tdee) * .4
            fat_c = float(tdee) * .35
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 5:
            tdee = float(tdee) * 1.1
            protein_c = float(tdee) * .4
            carb_c = float(tdee) * .4
            fat_c = float(tdee) * .2
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        else:
            print('invalid entry, please only enter numbers (1-5)')
    elif int(days_work) == 4:
        tdee = float(bmr) * 1.725
        print(f'Total Daily Energy Expenditure (TDEE) = {tdee} calories')
        print('(1) Maintenance')
        print('(2) Cutting')
        print('(3) Recomposition')
        print('(4) Dirty Bulk')
        print('(5) Lean Bulk')
        goal = input('What is your goal? (1-5): ')
        if int(goal) == 1:
            protein_c = float(tdee) * .3
            carb_c = float(tdee) * .4
            fat_c = float(tdee) * .3
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 2:
            tdee = float(tdee) * .8
            protein_c = float(tdee) * .35
            carb_c = float(tdee) * .35
            fat_c = float(tdee) * .3
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 3:
            tdee = float(tdee) * .8
            protein_c = float(tdee) * .4
            carb_c = float(tdee) * .3
            fat_c = float(tdee) * .3
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 4:
            tdee = float(tdee) * 1.1
            protein_c = float(tdee) * .25
            carb_c = float(tdee) * .4
            fat_c = float(tdee) * .35
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 5:
            tdee = float(tdee) * 1.1
            protein_c = float(tdee) * .4
            carb_c = float(tdee) * .4
            fat_c = float(tdee) * .2
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        else:
            print('invalid entry, please only enter numbers (1-5)')
    elif int(days_work) == 5:
        tdee = float(bmr) * 1.9
        print(f'Total Daily Energy Expenditure (TDEE) = {tdee} calories')
        print('(1) Maintenance')
        print('(2) Cutting')
        print('(3) Recomposition')
        print('(4) Dirty Bulk')
        print('(5) Lean Bulk')
        goal = input('What is your goal? (1-5): ')
        if int(goal) == 1:
            protein_c = float(tdee) * .3
            carb_c = float(tdee) * .4
            fat_c = float(tdee) * .3
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 2:
            tdee = float(tdee) * .8
            protein_c = float(tdee) * .35
            carb_c = float(tdee) * .35
            fat_c = float(tdee) * .3
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 3:
            tdee = float(tdee) * .8
            protein_c = float(tdee) * .4
            carb_c = float(tdee) * .3
            fat_c = float(tdee) * .3
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 4:
            tdee = float(tdee) * 1.1
            protein_c = float(tdee) * .25
            carb_c = float(tdee) * .4
            fat_c = float(tdee) * .35
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 5:
            tdee = float(tdee) * 1.1
            protein_c = float(tdee) * .4
            carb_c = float(tdee) * .4
            fat_c = float(tdee) * .2
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        else:
            print('invalid entry, please only enter numbers (1-5)')
    else:
        print('invalid input please enter a number 1-5')
elif sex == 'female':
    weight = input('What is your weight in lbs?: ')
    height = input('What is your height in feet?: ')
    age = input('What is your age in years?: ')
    print('(1) No formal Exercise')
    print('(2) Light walking or housework, 1 to 3 days a week')
    print('(3) Moderate exercise 3 to 4 days a week')
    print('(4) Moderate to vigorous exercise 5 to 6 days a week')
    print('(5) Vigorous exercise 6 to 7 days a week')
    days_work = input('Rate your activity level from 1-5: ')
    weight = float(weight) * .453592 * 10
    height = float(height) * 30.48 * 6.25
    age = float(age) * 5
    bmr = float(weight) + float(height) - float(age) - 161
    print(f'Base Metabolic Rate (BMR) = {bmr} calories')
    if int(days_work) == 1:
        tdee = float(bmr) * 1.2
        print(f'Total Daily Energy Expenditure (TDEE) = {tdee} calories')
        print('(1) Maintenance')
        print('(2) Cutting')
        print('(3) Recomposition')
        print('(4) Dirty Bulk')
        print('(5) Lean Bulk')
        goal = input('What is your goal? (1-5): ')
        if int(goal) == 1:
            protein_c = float(tdee) * .3
            carb_c = float(tdee) * .4
            fat_c = float(tdee) * .3
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 2:
            tdee = float(tdee) * .8
            protein_c = float(tdee) * .35
            carb_c = float(tdee) * .35
            fat_c = float(tdee) * .3
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 3:
            tdee = float(tdee) * .8
            protein_c = float(tdee) * .4
            carb_c = float(tdee) * .3
            fat_c = float(tdee) * .3
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 4:
            tdee = float(tdee) * 1.1
            protein_c = float(tdee) * .25
            carb_c = float(tdee) * .4
            fat_c = float(tdee) * .35
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 5:
            tdee = float(tdee) * 1.1
            protein_c = float(tdee) * .4
            carb_c = float(tdee) * .4
            fat_c = float(tdee) * .2
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        else:
            print('invalid entry, please only enter numbers (1-5)')
    elif int(days_work) == 2:
        tdee = float(bmr) * 1.375
        print(f'Total Daily Energy Expenditure (TDEE) = {tdee} calories')
        print('(1) Maintenance')
        print('(2) Cutting')
        print('(3) Recomposition')
        print('(4) Dirty Bulk')
        print('(5) Lean Bulk')
        goal = input('What is your goal? (1-5): ')
        if int(goal) == 1:
            protein_c = float(tdee) * .3
            carb_c = float(tdee) * .4
            fat_c = float(tdee) * .3
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 2:
            tdee = float(tdee) * .8
            protein_c = float(tdee) * .35
            carb_c = float(tdee) * .35
            fat_c = float(tdee) * .3
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 3:
            tdee = float(tdee) * .8
            protein_c = float(tdee) * .4
            carb_c = float(tdee) * .3
            fat_c = float(tdee) * .3
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 4:
            tdee = float(tdee) * 1.1
            protein_c = float(tdee) * .25
            carb_c = float(tdee) * .4
            fat_c = float(tdee) * .35
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 5:
            tdee = float(tdee) * 1.1
            protein_c = float(tdee) * .4
            carb_c = float(tdee) * .4
            fat_c = float(tdee) * .2
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        else:
            print('invalid entry, please only enter numbers (1-5)')
    elif int(days_work) == 3:
        tdee = float(bmr) * 1.55
        print(f'Total Daily Energy Expenditure (TDEE) = {tdee} calories')
        print('(1) Maintenance')
        print('(2) Cutting')
        print('(3) Recomposition')
        print('(4) Dirty Bulk')
        print('(5) Lean Bulk')
        goal = input('What is your goal? (1-5): ')
        if int(goal) == 1:
            protein_c = float(tdee) * .3
            carb_c = float(tdee) * .4
            fat_c = float(tdee) * .3
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 2:
            tdee = float(tdee) * .8
            protein_c = float(tdee) * .35
            carb_c = float(tdee) * .35
            fat_c = float(tdee) * .3
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 3:
            tdee = float(tdee) * .8
            protein_c = float(tdee) * .4
            carb_c = float(tdee) * .3
            fat_c = float(tdee) * .3
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 4:
            tdee = float(tdee) * 1.1
            protein_c = float(tdee) * .25
            carb_c = float(tdee) * .4
            fat_c = float(tdee) * .35
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 5:
            tdee = float(tdee) * 1.1
            protein_c = float(tdee) * .4
            carb_c = float(tdee) * .4
            fat_c = float(tdee) * .2
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        else:
            print('invalid entry, please only enter numbers (1-5)')
    elif int(days_work) == 4:
        tdee = float(bmr) * 1.725
        print(f'Total Daily Energy Expenditure (TDEE) = {tdee} calories')
        print('(1) Maintenance')
        print('(2) Cutting')
        print('(3) Recomposition')
        print('(4) Dirty Bulk')
        print('(5) Lean Bulk')
        goal = input('What is your goal? (1-5): ')
        if int(goal) == 1:
            protein_c = float(tdee) * .3
            carb_c = float(tdee) * .4
            fat_c = float(tdee) * .3
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 2:
            tdee = float(tdee) * .8
            protein_c = float(tdee) * .35
            carb_c = float(tdee) * .35
            fat_c = float(tdee) * .3
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 3:
            tdee = float(tdee) * .8
            protein_c = float(tdee) * .4
            carb_c = float(tdee) * .3
            fat_c = float(tdee) * .3
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 4:
            tdee = float(tdee) * 1.1
            protein_c = float(tdee) * .25
            carb_c = float(tdee) * .4
            fat_c = float(tdee) * .35
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 5:
            tdee = float(tdee) * 1.1
            protein_c = float(tdee) * .4
            carb_c = float(tdee) * .4
            fat_c = float(tdee) * .2
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        else:
            print('invalid entry, please only enter numbers (1-5)')
    elif int(days_work) == 5:
        tdee = float(bmr) * 1.9
        print(f'Total Daily Energy Expenditure (TDEE) = {tdee} calories')
        print('(1) Maintenance')
        print('(2) Cutting')
        print('(3) Recomposition')
        print('(4) Dirty Bulk')
        print('(5) Lean Bulk')
        goal = input('What is your goal? (1-5): ')
        if int(goal) == 1:
            protein_c = float(tdee) * .3
            carb_c = float(tdee) * .4
            fat_c = float(tdee) * .3
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 2:
            tdee = float(tdee) * .8
            protein_c = float(tdee) * .35
            carb_c = float(tdee) * .35
            fat_c = float(tdee) * .3
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 3:
            tdee = float(tdee) * .8
            protein_c = float(tdee) * .4
            carb_c = float(tdee) * .3
            fat_c = float(tdee) * .3
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 4:
            tdee = float(tdee) * 1.1
            protein_c = float(tdee) * .25
            carb_c = float(tdee) * .4
            fat_c = float(tdee) * .35
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        elif int(goal) == 5:
            tdee = float(tdee) * 1.1
            protein_c = float(tdee) * .4
            carb_c = float(tdee) * .4
            fat_c = float(tdee) * .2
            protein_g = int(protein_c) / 4
            carb_g = int(carb_c) / 4
            fat_g = int(fat_c) / 9
            print(f'Calories of Protein: {protein_c}')
            print(f'Calories of Carbs: {carb_c}')
            print(f'Calories of Fat: {fat_c}')
            print(f'Grams of Protein: {protein_g}')
            print(f'Grams of Carbs: {carb_g}')
            print(f'Grams of Fat: {fat_g}')
        else:
            print('invalid entry, please only enter numbers (1-5)')
    else:
        print('invalid input please enter a number 1-5')
else:
    print('invalid input please enter male or female')



