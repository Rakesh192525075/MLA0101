age = int(input("Enter age: "))
bmi = float(input("Enter BMI: "))
disease = input("Enter disease: ").lower()

if disease == "diabetes":
    print("Diet: Low-sugar foods")
elif disease == "hypertension":
    print("Diet: Low-salt foods")
elif bmi >= 25:
    print("Diet: Balanced diet with controlled portions")
else:
    print("Diet: Balanced healthy diet")
