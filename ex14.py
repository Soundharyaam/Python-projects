from sys import argv
script,user_name,course=argv
prompt="#"

print(f"Hi {user_name}, I am the {script} script. Good to know that you studied, {course}")
print("I'd like to ask you few questions.")
print(f"Do you like Potter Series, {user_name}")
likes=input(prompt)
print(f"Where do you live, {user_name}")
lives=input(prompt)

print("What kind of computer do you have?")
computers=input(prompt)

print(f"""Alright! so you said, {likes} about liking Potter series.
You are living in {lives}. You are using {computers} computers. That's really nice.""")