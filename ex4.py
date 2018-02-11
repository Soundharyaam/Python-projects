cars=100
space_in_a_car=4
drivers=30
passengers=90

#calculating the "number of cars not driven"
cars_not_driven=cars-drivers
#calculating the "number of cars driven"
cars_driven=drivers
#calculating the "carpool capacity"
carpool_capacity=cars_driven*space_in_a_car
#calculating the "average number of passengers which can be accommodated in each car"
average_passengers_per_car=passengers/cars_driven

print("There are", cars, "cars available")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people today")
print("We have", float(passengers), "to carpool today")
print("We need to put about", int(average_passengers_per_car), "in each car")

