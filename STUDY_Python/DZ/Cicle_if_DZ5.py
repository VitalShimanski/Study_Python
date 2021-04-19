best_auto = ['mercedes', 'audi', 'toyota', 'tesla', 'bmw', 'lexus', 'subaru', 'mazda', 'volvo']
medium_auto = ['nissan', 'skoda', 'opel', 'chevrolet', 'kia', 'Hyundai', 'volkswagen', 'seat']
bad_auto = ['fiat', 'lada', 'renault', 'daewoo', 'ford', 'rover', 'Daihatsu']
unknown_auto = []
user_name = input("What is your name? ")
user_message_brand = input("What is your car brand? ")
if user_message_brand.lower() in best_auto:
    print(f"You driving a cool car. {user_message_brand} - this is a premium brand")
elif user_message_brand.lower() in medium_auto:
    print(f"You driving a normal car. {user_message_brand} - this is a normal car")
elif user_message_brand.lower in bad_auto:
    print(f"You driving a terrible car. {user_message_brand} - this is a terrible car")
else:
    print(f"Your car is not in the database. Do you want to add your {user_message_brand} to the database?")
user_message_model = input("What is your car model? ")
user_message_year = input("Year of manufacture of your car?")

def add_car(user_message_brand):
    user_message_brand = input()
    if user_message_brand not in best_auto and user_message_brand not in medium_auto and user_message_brand not in bad_auto:
        unknown_auto.append(user_message_brand)
print(unknown_auto)


