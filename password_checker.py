import re

password = input("Enter a password: ")

score = 0

length_check = len(password) >= 8
uppercase_check = bool(re.search(r"[A-Z]", password))
lowercase_check = bool(re.search(r"[a-z]", password))
number_check = bool(re.search(r"\d", password))
special_check = bool(re.search(r"[^A-Za-z0-9]", password))

if length_check:
    score += 1

if uppercase_check:
    score += 1

if lowercase_check:
    score += 1

if number_check:
    score += 1

if special_check:
    score += 1

print("\nPassword Analysis:")
print(f"Length: {'Pass' if length_check else 'Fail'}")
print(f"Uppercase: {'Pass' if uppercase_check else 'Fail'}")
print(f"Lowercase: {'Pass' if lowercase_check else 'Fail'}")
print(f"Number: {'Pass' if number_check else 'Fail'}")
print(f"Special Character: {'Pass' if special_check else 'Fail'}")

if score <= 2:
    print("\nPassword Strength: Weak")
elif score <= 4:
    print("\nPassword Strength: Moderate")
else:
    print("\nPassword Strength: Strong")