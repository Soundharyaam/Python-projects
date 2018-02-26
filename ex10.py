tabby_cat="\t I'm tabbed in."
persian_cat="I'm split\non a line."
backslash_cat="I'm \\a\\ cat."

fat_cat='''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
formatter="{}{}"
a="I am 6'2 tall."
b='I am 6\'2 tall.'
print(formatter.format(tabby_cat, persian_cat, backslash_cat, fat_cat))
print("\n\n")
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(a)
print(b)