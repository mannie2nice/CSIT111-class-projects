# Emmanuel Adisa
# 2/25/26


print("Hello, i am the Ageculator and i tell you what age group you belong based on your age ;)" )

age = int(input("Do tell your age? "))

if age > 65:
    print("You are a senior citizen. ")
elif age >= 18:
    print("You are an adult. ")
else:
    print("You are a minor. ")