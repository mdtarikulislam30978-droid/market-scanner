# একটি সহজ ডেটাবেজ যেখানে ফোন নাম্বার এবং তাদের স্ট্যাটাস থাকবে
# স্ট্যাটাস: "ACTIVE" (সচল) অথবা "FROZEN" (লক করা)
user_accounts = {
    "01700000000": "ACTIVE",
    "01800000000": "ACTIVE",
    "01900000000": "ACTIVE"
}

def account_manager():
    print("=== মানুষের সেবায় ডিজিটাল অ্যাকাউন্ট ম্যানেজার ===")
    print("1. অ্যাকাউন্ট স্ট্যাটাস চেক করুন")
    print("2. প্রতারক বা অভিযুক্ত নাম্বার ফ্রিজ (লক) করুন")
    print("3. সমাধান হওয়ার পর নাম্বার আনলক করুন")
    
    choice = input("\nতোমার অপশন বেছে নাও (1, 2 বা 3): ").strip()
    
    if choice == '1':
        phone = input("যাচাই করার জন্য ফোন নাম্বারটি লিখো: ").strip()
        if phone in user_accounts:
            status = user_accounts[phone]
            print(f"\n[ি] নাম্বার {phone}-এর বর্তমান স্ট্যাটাস: {status}")
        else:
            print(f"\n[-] এই নাম্বারটি সিস্টেমে রেজিস্টার্ড নয়।")
            
    elif choice == '2':
        phone = input("যে নাম্বারটি লক (Freeze) করতে চাও সেটি লিখো: ").strip()
        if phone in user_accounts:
            user_accounts[phone] = "FROZEN"
            print(f"\n[+] সফল! নাম্বার {phone} এখন সম্পূর্ণ ফ্রিজ বা লক করা হয়েছে। সে আর কোনো লেনদেন করতে পারবে না।")
        else:
            print(f"\n[-] নাম্বারটি পাওয়া যায়নি!")
            
    elif choice == '3':
        phone = input("যে নাম্বারটি আনলক (Unfreeze) করতে চাও সেটি লিখো: ").strip()
        if phone in user_accounts:
            user_accounts[phone] = "ACTIVE"
            print(f"\n[+] সফল! নাম্বার {phone}-এর লক খুলে দেওয়া হয়েছে। সে এখন আগের মতো স্বাভাবিক ব্যবহার করতে পারবে।")
        else:
            print(f"\n[-] নাম্বারটি পাওয়া যায়নি!")
    else:
        print("\n[-] ভুল অপশন সিলেক্ট করেছ বন্ধু!")

if __name__ == "__main__":
    account_manager()
