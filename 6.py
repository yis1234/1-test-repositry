"""Calories burned
Shows how many kgs lost
Sun Woo Yi
07/02/22
"""
bicycling = int(input("How many hours did you bike for: "))
jogging = int(input("How many hours did you jog for: "))
swimming = int(input("How many hours did you swim for: "))
bicycling_calories_lost = bicycling * 200
jogging_calories_lost = jogging * 475
swimming_calories_lost = swimming * 275
kgs_lost = (bicycling_calories_lost + jogging_calories_lost + \
           swimming_calories_lost)/7709
print(kgs_lost)
