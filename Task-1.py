# %%
#Pass / Fail Analyzer

marks = [45, 78, 90, 33, 60]

pass_count = 0
fail_count = 0

for m in marks:
    if m >=50:
        pass_count +=1
    else:
        fail_count+=1

print("Total Students:",len(marks))
print("Pass Students:",pass_count)
print("Fail students:",fail_count)



# %%
#Simple Data Cleaner

names = [" Alice ", "bob", " CHARLIE "]


cleaned_names = []

for i in names:
    cleaned = i.strip().lower()
    cleaned_names.append(cleaned)


print(cleaned_names)

# %%
# Message Length Analyzer

messages = ["Hi", "Welcome to the platform", "OK"]

for msg in messages:
    length = len(msg)
    print(msg,"length:",length)

    if length>10:
        print("Long message")

# %%
#Error Message Detector

logs = ["INFO", "ERROR", "WARNING", "ERROR"]

error_count = 0

for log in logs:
    if log == "ERROR":
        error_count +=1

print("Toatl error entries:",error_count)


# %%
# User Login Check

username = "admin"
password = "1234"

print("Enter login details")

user = input("Enter username: ")
user_pass = input("Enter password: ")

if user == username and user_pass == password:
    print("Login Successful")
else:
    print("Invalid Credentials")



