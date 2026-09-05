import random
import string

def generate_password():
    print("\n=== STRONG PASSWORD GENERATOR ===")
    try:
        user_input = input("Enter password length (e.g., 12): ").strip()
        length = int(user_input)
        
        if length < 6:
            print("[-] Password length should be at least 6 characters for security!")
            return
            
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        password = "".join(random.choice(chars) for _ in range(length))
        
        print(f"\n[+] Generated Secure Password: {password}")
        print("[+] Keep it safe and secure, friend!\n")
        
    except ValueError:
        print("[-] Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    generate_password()
