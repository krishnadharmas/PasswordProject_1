import re

# ✅ FIRST: this function
def check_common_password(password):
    try:
        with open("common_passwords.txt", "r") as file:
            common = file.read().splitlines()
            if password in common:
                return True
    except FileNotFoundError:
        print("Common password file not found.")
    return False


# ✅ SECOND: your strength checker
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character")

    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback


# ✅ THIRD: main program
password = input("Enter your password: ")

strength, feedback = check_password_strength(password)

print("\nPassword Strength:", strength)

# ✅ NOW this will work
if check_common_password(password):
    print("⚠️ This password is very common and easily guessable!")

if feedback:
    print("Suggestions:")
    for f in feedback:
        print("-", f)
