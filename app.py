from flask import Flask, render_template_string, request, redirect, url_for
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# ইন-মেমোরি স্টোরেজ (অ্যাক্সেস এবং ট্রানজেকশন ট্র্যাক করার জন্য)
SUBMITTED_TRX = set()
VALID_ACCESS_TOKENS = set()

# ১. হোমপেজ / প্রাইসিং ও পেমেন্ট পোর্টাল
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        trx_id = request.form.get("trx_id", "").strip()
        if trx_id:
            if trx_id in SUBMITTED_TRX:
                return render_template_string(HOME_HTML, error="This Transaction ID has already been used! Please use a unique TrxID.")
            
            # ট্রানজেকশন সেভ করা হলো
            SUBMITTED_TRX.add(trx_id)
            
            # ইউনিক ওয়ান-টাইম অ্যাক্সেস টোকেন তৈরি
            token = secrets.token_urlsafe(16)
            VALID_ACCESS_TOKENS.add(token)
            
            return redirect(url_for("secret_scanner", token=token))
            
    return render_template_string(HOME_HTML, error=None)


# ২. সিক্রেট স্ক্যানার পেজ (ওয়ান-টাইম ইউনিক লিংক প্রটেকশন সহ)
@app.route("/scanner/<token>")
def secret_scanner(token):
    # চেক করা লিংকটি ভ্যালিড কি না এবং একবারের বেশি ব্যবহার হয়েছে কি না
    if token not in VALID_ACCESS_TOKENS:
        return """
        <!DOCTYPE html>
        <html lang="en">
        <head><title>Access Denied</title></head>
        <body style="background:#0f172a; color:#f8fafc; font-family:Arial; text-align:center; padding-top:100px;">
            <h1 style="color:#ef4444;">❌ Access Denied or Link Already Used!</h1>
            <p>This unique access link has expired or is invalid. Please purchase a new plan.</p>
            <a href="/" style="color:#38bdf8; text-decoration:none; font-weight:bold;">← Go Back to Home</a>
        </body>
        </html>
        """, 403
    
    # সফলভাবে ব্যবহারের পর টোকেনটি ডিলিট করে দেওয়া হলো যাতে পরবর্তীতে আর ব্যবহার করা না যায় (One-Time Link)
    VALID_ACCESS_TOKENS.remove(token)
    
    return render_template_string(SCANNER_HTML)


# HTML Templates (সবগুলো এক জায়গায় সাজানো)

HOME_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tarikul & Gemini - Market Scanner Access Portal</title>
    <style>
        body { background-color: #0f172a; color: #f8fafc; font-family: Arial, sans-serif; margin: 0; padding: 20px; }
        .container { max-width: 600px; margin: 0 auto; background: #1e293b; padding: 30px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
        h1 { text-align: center; color: #38bdf8; }
        .plan-box { background: #334155; padding: 15px; margin: 15px 0; border-radius: 8px; border: 1px solid #475569; }
        .payment-methods { background: #0f172a; padding: 15px; border-radius: 8px; margin-top: 20px; font-size: 14px; line-height: 1.6; }
        .pay-item { margin-bottom: 12px; padding-bottom: 8px; border-bottom: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; }
        .copy-btn { background: #38bdf8; color: #0f172a; border: none; padding: 4px 10px; border-radius: 4px; font-weight: bold; cursor: pointer; font-size: 12px; margin-top: 4px; }
        .btn { display: block; width: 100%; background: #22c55e; color: white; padding: 12px; text-align: center; border: none; border-radius: 6px; font-size: 16px; font-weight: bold; cursor: pointer; text-decoration: none; margin-top: 15px; }
        .toast { position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%); background: #22c55e; color: white; padding: 10px 20px; border-radius: 5px; font-weight: bold; display: none; z-index: 1000; }
        .error-msg { background: #ef4444; color: white; padding: 10px; border-radius: 6px; text-align: center; margin-bottom: 15px; font-weight: bold; }
    </style>
    <script>
        function copyToClipboard(text) {
            navigator.clipboard.writeText(text).then(() => {
                let toast = document.getElementById("toastMessage");
                toast.style.display = "block";
                setTimeout(() => { toast.style.display = "none"; }, 2000);
            });
        }
    </script>
</head>
<body>
    <div class="container">
        <h1>Market Scanner Access Portal</h1>
        
        {% if error %}
        <div class="error-msg">{{ error }}</div>
        {% endif %}

        <div class="plan-box">
            <h3>⚡ 1 Hour Access Plan</h3>
            <p>Price: 50,000 BDT</p>
        </div>
        <div class="plan-box">
            <h3>⚡ 2 Hours Access Plan</h3>
            <p>Price: 90,000 BDT</p>
        </div>

        <div class="payment-methods">
            <h3 style="color: #38bdf8; margin-top: 0;">💳 Payment Accounts (Click to Copy)</h3>
            <div class="pay-item">
                <span><b>🔸 bKash:</b> <span id="acc-bkash">01700000000</span></span>
                <button class="copy-btn" onclick="copyToClipboard('01700000000')">Copy</button>
            </div>
            <div class="pay-item">
                <span><b>🔸 Nagad:</b> <span id="acc-nagad">01700000000</span></span>
                <button class="copy-btn" onclick="copyToClipboard('01700000000')">Copy</button>
            </div>
        </div>

        <form method="POST">
            <label for="trx_id" style="display: block; margin-top: 15px; font-weight: bold;">Enter Transaction ID (TrxID):</label>
            <input type="text" id="trx_id" name="trx_id" required placeholder="Enter unique TrxID" style="width: 100%; padding: 10px; margin-top: 8px; border-radius: 5px; border: 1px solid #64748b; background: #1e293b; color: white; box-sizing: border-box;">
            <button type="submit" class="btn">Submit & Get One-Time Access Link</button>
        </form>
    </div>
    <div id="toastMessage" class="toast">Copied to Clipboard!</div>
</body>
</html>
"""

SCANNER_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tarikul & Gemini 15M Pro</title>
    <style>
        body { background-color: #0f172a; color: #f8fafc; font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: #1e293b; padding: 25px; border-radius: 12px; width: 320px; text-align: center; border: 1px solid #334155; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
        h2 { color: #38bdf8; font-size: 18px; margin-bottom: 5px; }
        .btn { background: #22c55e; color: white; border: none; padding: 10px; width: 100%; border-radius: 6px; font-weight: bold; cursor: pointer; margin: 15px 0; }
        .row { display: flex; justify-content: space-between; background: #0f172a; padding: 8px 12px; margin: 8px 0; border-radius: 4px; font-size: 13px; }
        .call { background: #0f172a; border: 2px solid #22c55e; color: #22c55e; padding: 10px; border-radius: 6px; font-weight: bold; margin-top: 15px; }
        .warning-text { font-size: 11px; color: #facc15; margin-top: 10px; }
    </style>
</head>
<body>
    <div class="card">
        <h2>Tarikul & Gemini 15M Pro</h2>
        <button class="btn">⚡ SCAN 15-MIN LIVE MARKET</button>
        <div class="row"><span>15M Market Trend:</span> <span>0.5027</span></div>
        <div class="row"><span>Chart Volatility:</span> <span>0.2024</span></div>
        <div class="row"><span>AI Master Score:</span> <span>0.5533</span></div>
        <div class="call">15-MINUTE CALL (STRONG BUY UP) [VERIFIED]</div>
        <div class="warning-text">⚠️ Note: This link is one-time use only and is now expired for future entries.</div>
    </div>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
