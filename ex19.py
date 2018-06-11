#defining cheese_and_crackers() wih two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

#calling cheese_and_crackers()
print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)

#assigning the values for the variables
print("OR, we can just give the function numbers directly:")
amount_of_cheese=10
amount_of_crackers=50
cheese=3
boxes=4

#calling cheese_and_crackers with different arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#making the calculations inside the arguments and passing it
print("We can even do math inside too:")
cheese_and_crackers(10+20,5+6)

#again making calculations with variables and number inside the arguments
print("And we can combine two variables and math:")
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000)

#calling in the different way
print("calling with two variable addition")
cheese_and_crackers(amount_of_cheese%cheese, amount_of_crackers%boxes)

#getting input from the users
print("function with input from the user")
cheese=int(input("No of cheese you want:"))
crackers=int(input("No of crackers you want:"))

cheese_and_crackers(cheese,crackers)
#my new function
def soundharya(*args, who_she_is="Engineer"):
    arg1, arg2=args
    print(f"She is doing {arg1} and {arg2}. She is a {who_she_is}")

soundharya("programming","photography")

choice="painter"
profession="photographer"
soundharya(choice,profession)