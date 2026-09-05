import os

LOG_FILE = "scam_log.txt"

def load_data_from_file():
    database = {}
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(":", 1)
                if len(parts) == 2:
                    phone, reason = parts
                    database[phone] = reason
    return database

def save_data_to_file(phone, reason):
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"{phone}:{reason}\n")

def update_file_after_delete(database):
    with open(LOG_FILE, "w", encoding="utf-8") as file:
        for phone, reason in database.items():
            file.write(f"{phone}:{reason}\n")

def scam_tracker_system():
    scam_database = load_data_from_file()
    
    while True:
        print("\n=== SCAM ALERT & VERIFICATION SYSTEM ===")
        print("1. Add New Scam Entry")
        print("2. Search/Check Phone Number")
        print("3. Remove Entry After Resolution")
        print("4. Exit")
        
        choice = input("\nEnter your option (1, 2, 3 or 4): ").strip()
        
        if choice == '1':
            phone = input("Enter phone number: ").strip()
            reason = input("Enter scam reason/complaint: ").strip()
            scam_database[phone] = reason
            save_data_to_file(phone, reason)
            print(f"[+] Success! Number {phone} saved to scam list and file.")
            
        elif choice == '2':
            phone = input("Enter phone number to check: ").strip()
            if phone in scam_database:
                print(f"[!] Warning! This number is a scammer. Reason: {scam_database[phone]}")
            else:
                print(f"[+] This number is safe or not in our database.")
                
        elif choice == '3':
            phone = input("Enter resolved phone number to remove: ").strip()
            if phone in scam_database:
                del scam_database[phone]
                update_file_after_delete(scam_database)
                print(f"[+] Number {phone} removed from list and file!")
            else:
                print(f"[-] Number not found in the list!")
                
        elif choice == '4':
            print("Exiting program. Goodbye, friend!")
            break
        else:
            print("[-] Invalid option! Please choose a valid choice.")

if __name__ == "__main__":
    scam_tracker_system()
