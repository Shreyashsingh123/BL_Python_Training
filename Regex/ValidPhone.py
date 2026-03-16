import re
number=input("Enter phone number")
pattern="[6-9][0-9]{9}"
match=re.match(pattern,number)
if match:
    print("Valid phone number")
else:
    print("Invalid Phone number")

s=re.search("6",number) # find forst occurence of 6 in number
print(s)
s2=re.findall("6",number) # find all occurence of 6 in number
print(s2)

text=" I like python"
new_text=re.sub("python","Java",text) # replace python with java using sub that is substitute(replace)
print(new_text)

# .	Any character,  ^ Start of string, $ End of string, * 0 or more times, + 1 or more times, ?	0 or 1 time
# {n} Exactly n times, {n,m} Between n and m, [abc]	a or b or c, [^abc]	Not a,b,c, \d Digit
# \D Non digit, \w Word character,  \s	Space