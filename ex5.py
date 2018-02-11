my_name="Shinchan"
my_age=5 
my_height=60 #in cm
my_weight=30 #in kg
my_eyes="Black"
my_teeth="white"
my_hair="Black"
weight_in_pounds=my_weight*0.393701
height_in_inches=my_height*2.2

print(f"Let's talk about {my_name}.")
print(f"He's {round(height_in_inches)} inches tall.")
print(f"He's {round(weight_in_pounds)} pounds heavy.")
print("Oh. That's not too much.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the juices.")

#line is tricky, try to get it exactly right
total=my_age+my_height+my_weight
print(f"If I add {my_age}, {my_height} and {my_weight} together, I will get {total}")