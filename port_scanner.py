import socket

def port_scanner():
    print("=== আইপি ও পোর্ট স্ক্যানার টুল ===")
    
    # স্ক্যান করার জন্য টার্গেট বা লোকালহোস্ট দেওয়া
    target = "127.0.0.1"  # নিজের ডিভাইস বা লোকাল নেটওয়ার্ক
    
    print(f"টার্মিনাল স্ক্যান করা হচ্ছে: {target}\n")
    
    # কিছু কমন পোর্ট স্ক্যান করার লিস্ট (যেমন: 21, 22, 80, 443 ইত্যাদি)
    ports = [21, 22, 80, 443, 3306, 8080]
    
    for port in ports:
        # সকেট তৈরি করা
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        # কানেক্ট করার চেষ্টা করা
        result = s.connect_ex((target, port))
        
        if result == 0:
            print(f"[+] পোর্ট {port}: খোলা (OPEN)")
        else:
            print(f"[-] পোর্ট {port}: বন্ধ (CLOSED)")
            
        s.close()

if __name__ == "__main__":
    port_scanner()
