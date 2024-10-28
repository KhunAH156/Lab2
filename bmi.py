def calculate_bmi(height, weight):
    print("Height="+str(height))
    print("Weight="+str(weight))
    
    bmi=weight/(height*height)
    BMI=round(bmi,2)
    print("BMI="+str(BMI))

    if BMI < 18.5:
        print("Under Weight")
        return -1
    elif BMI >= 18.5 and BMI <= 25.0:
        print("Normal Weight")
        return 0
    else: 
        print("Over Weight") 
        return 1   


calculate_bmi(weight=57,height=1.73)