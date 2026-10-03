# Section 1: Variables and Types
name = "Jung"
age = 27
height = "5'5"
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

# Section 2: User Input and Math
name = input("What is your name?")
birth_year = input("What year were you born?")
int_year = int(birth_year)
current_year = 2026
age = current_year - int_year
print(f"Hi, {name}! You are approximately , {age}, years old!")

# Section 3: Type Conversion and f-strings
number_1 = input("Please provide me with a number:")
number_f1 = float(number_1)
number_2 = input("Please provide me with another number:")
number_f2 = float(number_2)
answer = number_f1 * number_f2
print(f"{answer} = {number_f1} * {number_f2}")

# Section 4: Formatted Receipt
# Store the item name, price, and quantity in variables, and compute the total from those variables
item_name = "vanilla latte"
price = 7.99
quantity = 3
total = price * quantity

print ()
print("===================")
print("      Receipt      ")
print("===================")
print(f"Item: {item_name}")
print(f"Price: {price}")
print(f"Quantity: {quantity}")
print(f"Total: $ {total}")
print()
print("===================")


# Section 5: Mini-Project — Profile Card
# Finally, tie it all together. Use input() to ask the user for:
# Their name
# Their hometown
# Their favorite hobby
# One fun fact about themselves
# The year they were born

name = input("What is your name?")
hometown = input("Where are you from?")
hobby = input("What is your favorite hobby?")
fun_fact = input("Tell me a fun fact about yourself:")
birth_year1 = input("What year were you born?")
int_year1 = int(birth_year1)
current_year = 2026
age = current_year - int_year1

print ()
print("=============================")
print(f"      Profile: {name}       ")
print("=============================")
print(f"\nHometown: {hometown}\n")
print(f"\nHobby: {hobby}\n")
print(f"\nFun Fact: {fun_fact}\n")
print(f"\nAge: {age}\n")
print("=============================")









