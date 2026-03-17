def BMI_def(height, weight):
    bmi_list = []
    height_m = height / 100
    bmi = weight /(height_m ** 2)
    bmi = round(bmi,2)
    bmi_list.append(bmi)    
    print(weight, height)
        
    if bmi < 18.5:
         category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    bmi_list.append(category)

    return bmi_list

# if __name__== '__main__':
#     print(BMI(150,40))