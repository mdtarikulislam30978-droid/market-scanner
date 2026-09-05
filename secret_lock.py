def encrypt_decrypt():
    print("=== সিক্রেট মেসেজ লকার টুল ===")
    
    choice = input("তুমি কি মেসেজ লক (L) করতে চাও নাকি আনলক (U) করতে চাও? (L/U): ").strip().upper()
    message = input("তোমার মেসেজটি এখানে লেখো: ")
    
    # সহজ একটি শিফট লজিক বা সাইফার ব্যবহার করা
    key = 3 
    result = ""
    
    if choice == 'L':
        # এনক্রিপ্ট বা লক করা
        for char in message:
            result += chr(ord(char) + key)
        print(f"\n[+] তোমার লক করা সিক্রেট মেসেজটি হলো:\n{result}\n")
        
    elif choice == 'U':
        # ডিক্রিপ্ট বা আনলক করা
        for char in message:
            result += chr(ord(char) - key)
        print(f"\n[+] তোমার আনলক করা আসল মেসেজটি হলো:\n{result}\n")
    else:
        print("[-] ভুল অপশন সিলেক্ট করেছ! শুধু L বা U দাও।")

if __name__ == "__main__":
    encrypt_decrypt()
