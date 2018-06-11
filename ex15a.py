from sys import argv

script, filename=argv

txt=open(filename)

print(f"Here, the content of file {filename}")
print(txt.read())
txt.close()
print("Please type the file name once again:")
file_again=input(">")
print_again=open(file_again)
a=print_again.read()
print(a)
print_again.close()