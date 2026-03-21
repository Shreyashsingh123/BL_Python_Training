import re
email=input("Enter email ")
pattern="^[a-zA-z]{1}[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}+"
match=re.match(pattern,email)
if match:
    print("Valid email")
else:
    print("Invalid email")


# abc1@gla.com.com
    