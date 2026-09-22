import os
import re
SYMBOLS = "!@#$%^&*()-_=+[]{};:'\",.<>/?\\|`~"
PASSWORD_FILE = os.getenv("PASSWORD_FILE", "/usr/share/wordlists/rockyou.txt") ######or choose your own path to the password file

def load_passwords(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return {line.strip() for line in f if line.strip()}

def score_password(password, weak_set):
    score = 0

    has_lower = bool(re.search(r"[a-z]", password))
    has_upper = bool(re.search(r"[A-Z]", password))
    has_digit = bool(re.search(r"[0-9]", password))
    has_symbol = any(c in SYMBOLS for c in password)
    over_8 = len(password) > 8
    less_4 = len(password) < 4
    leaked = password in weak_set or password.lower() in weak_set

    if has_lower:
        score += 5
    if has_upper:
        score += 10
    if has_digit:
        score += 10
    if has_symbol:
        score += 20
    if over_8:
        score += 15
    if not leaked:
        if not less_4:
            score += 40
            print("we didn't find your password in the leaked database")
    else:
        print("we found your password in the leaked database")
    if not has_symbol and not has_digit and not has_upper and not has_lower:
        score = 0
        
    
    meets_all = has_lower and has_upper and has_digit and has_symbol and over_8 and not leaked

    return score, meets_all

def rate(score):
    if score >= 90:
        return "Excellent"
    if score >= 70:
        return "Strong"
    if score >= 50:
        return "Moderate"
    if score >= 30:
        return "Weak"
    return "Very Weak"

def main():
    weak_passwords = load_passwords(PASSWORD_FILE)
    print(f"Loaded {len(weak_passwords)} passwords.\n")

    while True:
        pwd = input("Enter password to check (or 'q' to quit): ")
        if pwd.lower() == "q":
            break

        score, meets_all = score_password(pwd, weak_passwords)

        print(f"\nScore: {score}% ->  {rate(score)}")
        print(f"Meets all requirements: {'YES' if meets_all else 'NO'}")
        print()

print("\n ---  Password Checker Tool  --- \n")
print("          L  Y  A  N  0\n\n")
print("            &&&   &&& ")
print("           &&&&& &&&&&")
print("            &&&&&&&&&")
print("             &&&&&&&")
print("               &&&")
print("                &\n\n\n\n")

if __name__ == "__main__":
    main()