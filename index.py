gender = input("Enter your gender")
waist_circum = int(input("Enter your waist circumference"))
hip_circum = int(input("Enter your hip circumference"))
ratio = waist_circum/hip_circum

if (gender.lower() == "male" and ratio > 0.9) or (gender.lower() == "female" and ratio > 0.85):
    print("You are a {} and you waist:hip ratio is {}. Therefore, your risk for cardiovascular diseases is high.".format(gender, ratio))
else:
    print("You are a {} and you waist:hip ratio is {}. Therefore, your risk for cardiovascular diseases is low.".format(gender, ratio))