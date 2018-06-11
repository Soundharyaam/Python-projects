from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Trying to copy the content from {from_file} to {to_file}") 

indata=open(from_file).read()

print(f"The input of the file is {len(indata)}")

print(f"Does the output file exists? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()
#outdata=open(to_file,"w")
#outdata.write(indata)

outdata=open(to_file,'w')
outdata.write(indata)

print("Alright, all done.")