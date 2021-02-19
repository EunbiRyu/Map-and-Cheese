# Create an intro message for the user :) Come up with a good name
# names --> Map & Cheese

print("---------------------------Map & Cheese---------------------------")
print("Welcome to Map & Cheese! Been around since '21")
print("Visit our website -> www.mapandcheese.com")
print("Our buisness hours are at the bottom of our page :)")
print("------------------------------------------------------------------\n")

# We want to ask the user for their first and last name and age
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(f"Full Name: {first_name} {last_name}")
correct_name = input("Is your name entered correctly? Please answer with 'yes' or 'no': ")
if correct_name != 'yes':
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    print(f"Updated Full Name: {first_name} {last_name}")

age = int(input("Enter your age: "))
print(f"Age: {age}")
correct_age = input("Did you enter your age correctly? Please answer with 'yes' or 'no': ")
if correct_age != 'yes':
    age = int(input("Enter your age: "))
    print(f"Updated Age: {age}")

# We want to ask the user for their phone number
phone_number = (input("Enter your phone number: "))
print(f"You entered {phone_number} for your number")
correct_number = input("Did you enter your phone number correctly? Please answer with 'yes' or 'no': ")
if correct_number != 'yes':
    phone_number = int(input("Enter your phone number: "))
    print(f"Updated Phone Number: {phone_number}")
    
# Ask if they want takeout or delievery

# Ask what cuisine they want

#Ask user for their current address

# Calculating Distances