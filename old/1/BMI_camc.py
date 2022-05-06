print("BMI calculator")
weight = input("What is Your Weight?\n")
height = input("What Is Your Height?\n")
result = int(weight)/float(height)**2
result_int = int(result)
if result_int < 18.5 :
    print(f"Your BMI is {result_int} you are underweight! ") 
elif result_int < 25 :
    print(f"Your BMI is {result_int} you have a normal weight! ")
elif result_int < 30 :
    print(f"Your BMI is {result_int} you are overweight! ") 
elif result_int < 35 :
    print(f"Your BMI is {result_int} you are obese! ")
else :
    print(f"Your BMI is {result_int} you are clinically obese ")
  
