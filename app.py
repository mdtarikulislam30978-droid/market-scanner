from flask import Flask, render_template_string, request, redirect, url_for, session, flash
import uuid
import os
import time

app = Flask(__name__)
app.secret_key = os.urandom(24)

ACTIVE_TOKENS = {}

PRICING_PLANS = {
    "1_hour": {"name": "1 Hour Access Plan", "price": "500,000 BDT", "duration_seconds": 3600},
    "2_hours": {"name": "2 Hours Access Plan", "price": "900,000 BDT", "duration_seconds": 7200},
    "3_hours": {"name": "3 Hours Access Plan", "price": "1,300,000 BDT", "duration_seconds": 10800},
    "4_hours": {"name": "4 Hours Access Plan", "price": "1,600,000 BDT", "duration_seconds": 14400},
    "5_hours": {"name": "5 Hours Access Plan", "price": "2,000,000 BDT", "duration_seconds": 18000}
}

PAYMENT_ACCOUNTS = {
    "bkash_personal": "01785304583",
    "bkash_agent": "01811290498",
    "nagad": "01785304583",
    "rocket_agent": "01811290498",
    "bank": "UCB Bank: 7863244000003204 (MD TARIQUL ISLAM, Bhawal Mirzapur Branch)",
    "crypto_usdt": "USDT (TRC20): TKTTRdKQ23mhD5Ey3zbj8LwuQiqBSSmydL | UID: 552253179"
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Market Scanner - Access Portal</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            background-color: #0b0f19;
            color: #f8fafc;
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }
        .main-container {
            width: 100%;
            max-width: 650px;
            background: #111827;
            border: 1px solid #1f2937;
            border-radius: 12px;
            padding: 30px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.5);
        }
        h1 {
            text-align: center;
            color: #38bdf8;
            margin-bottom: 20px;
            font-size: 24px;
        }
        .video-container {
            position: relative;
            width: 100%;
            padding-bottom: 56.25%;
            height: 0;
            background: #000;
            border-radius: 8px;
            overflow: hidden;
            margin-bottom: 20px;
            border: 1px solid #334155;
        }
        .video-container iframe {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            border: 0;
        }
        .plan-card {
            background: #1f2937;
            border-radius: 8px;
            padding: 12px 18px;
            margin-bottom: 10px;
            border-left: 4px solid #38bdf8;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .plan-title { font-weight: bold; font-size: 14px; color: #f8fafc; }
        .plan-price { color: #34d399; font-size: 14px; }
        .payment-box {
            background: #1e293b;
            border-radius: 8px;
            padding: 15px 20px;
            margin: 20px 0;
            border: 1px solid #334155;
        }
        .payment-title { font-size: 14px; font-weight: bold; color: #fbbf24; margin-bottom: 12px; }
        .account-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 13px;
            margin-bottom: 8px;
            color: #cbd5e1;
            word-break: break-all;
        }
        .account-row span { flex: 1; padding-right: 10px; }
        .copy-btn {
            background: #0284c7;
            color: white;
            border: none;
            padding: 4px 10px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 11px;
            white-space: nowrap;
        }
        .copy-btn:hover { background: #0369a1; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 6px; font-size: 14px; color: #94a3b8; }
        select, input[type="text"] {
            width: 100%;
            padding: 12px;
            background: #0f172a;
            border: 1px solid #334155;
            color: white;
            border-radius: 6px;
            font-size: 14px;
        }
        .submit-btn {
            width: 100%;
            background: #22c55e;
            color: white;
            border: none;
            padding: 14px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 6px;
            cursor: pointer;
            transition: background 0.2s;
        }
        .submit-btn:hover { background: #16a34a; }
        .scanner-box { text-align: center; }
        .signal-box {
            background: #1f2937;
            border: 1px solid #374151;
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
            text-align: left;
        }
        .signal-row { display: flex; justify-content: space-between; margin-bottom: 10px; font-size: 15px; }
        .signal-badge {
            background: #14532d;
            color: #4ade80;
            padding: 12px;
            border-radius: 6px;
            font-weight: bold;
            text-align: center;
            border: 1px solid #16a34a;
        }
        .warning-text { font-size: 12px; color: #facc15; margin-top: 15px; }
    </style>
</head>
<body>
    <div class="main-container">
        {% if page == 'pricing' %}
            <h1>Market Scanner Access Portal</h1>
            
            <div class="video-container">
                <iframe src="https://www.youtube.com/embed/YOUR_VIDEO_ID" title="Payment Tutorial" allowfullscreen></iframe>
            </div>
            
            {% for key, plan in plans.items() %}
            <div class="plan-card">
                <div class="plan-title">⚡ {{ plan.name }}</div>
                <div class="plan-price">{{ plan.price }}</div>
            </div>
            {% endfor %}

            <div class="payment-box">
                <div class="payment-title">💳 Official Payment Accounts (Click to Copy)</div>
                <div class="account-row">
                    <span>• bKash Personal: <strong id="bp">{{ accounts.bkash_personal }}</strong></span>
                    <button class="copy-btn" onclick="copyText('bp')">Copy</button>
                </div>
                <div class="account-row">
                    <span>• bKash Agent: <strong id="ba">{{ accounts.bkash_agent }}</strong></span>
                    <button class="copy-btn" onclick="copyText('ba')">Copy</button>
                </div>
                <div class="account-row">
                    <span>• Nagad (Personal): <strong id="nag">{{ accounts.nagad }}</strong></span>
                    <button class="copy-btn" onclick="copyText('nag')">Copy</button>
                </div>
                <div class="account-row">
                    <span>• Rocket Agent: <strong id="ra">{{ accounts.rocket_agent }}</strong></span>
                    <button class="copy-btn" onclick="copyText('ra')">Copy</button>
                </div>
                <div class="account-row">
                    <span>• UCB Bank: <strong id="bnk">{{ accounts.bank }}</strong></span>
                    <button class="copy-btn" onclick="copyText('bnk')">Copy</button>
                </div>
                <div class="account-row">
                    <span>• Crypto USDT/UID: <strong id="usdt">{{ accounts.crypto_usdt }}</strong></span>
                    <button class="copy-btn" onclick="copyText('usdt')">Copy</button>
                </div>
            </div>

            <form method="POST" action="/verify">
                <div class="form-group">
                    <label for="plan">Select Your Plan:</label>
                    <select id="plan" name="plan" required>
                        {% for key, plan in plans.items() %}
                        <option value="{{ key }}">{{ plan.name }} - {{ plan.price }}</option>
                        {% endfor %}
                    </select>
                </div>
                <div class="form-group">
                    <label for="trxid">Enter Transaction ID / Hash:</label>
                    <input type="text" id="trxid" name="trxid" placeholder="Enter TrxID or Crypto TxID" required>
                </div>
                <button type="submit" class="submit-btn">Submit & Get Access Link</button>
            </form>

            <script>
                function copyText(elementId) {
                    const text = document.getElementById(elementId).innerText;
                    navigator.clipboard.writeText(text);
                    alert("Copied: " + text);
                }
            </script>

        {% elif page == 'scanner' %}
            <div class="scanner-box">
                <h1>Market Pro Scanner</h1>
                <p style="color: #38bdf8; margin-bottom: 15px;">Active Plan Duration: <strong>{{ duration_name }}</strong></p>
                <button class="submit-btn" style="margin-bottom: 20px;">⚡ SCAN LIVE MARKET</button>
                
                <div class="signal-box">
                    <div class="signal-row"><span>Market Trend:</span> <strong>Bullish / Buy</strong></div>
                    <div class="signal-row"><span>Volatility Score:</span> <strong>Stable</strong></div>
                    <div class="signal-row"><span>AI Master Index:</span> <strong>Verified</strong></div>
                </div>

                <div class="signal-badge">
                    LIVE TRADING SIGNAL ACTIVE
                </div>

                <div class="warning-text">
                    ⚠️ Note: This link is valid only for the selected time duration and will expire automatically.
                </div>
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/')
def pricing():
    return render_template_string(HTML_TEMPLATE, page='pricing', plans=PRICING_PLANS, accounts=PAYMENT_ACCOUNTS)

@app.route('/verify', methods=['POST'])
def verify():
    selected_plan = request.form.get('plan')
    trxid = request.form.get('trxid')
    
    if selected_plan in PRICING_PLANS and trxid:
        duration_seconds = PRICING_PLANS[selected_plan]["duration_seconds"]
        plan_name = PRICING_PLANS[selected_plan]["name"]
        
        expiry_time = time.time() + duration_seconds
        token = str(uuid.uuid4())
        
        ACTIVE_TOKENS[token] = {
            "expiry": expiry_time,
            "plan_name": plan_name
        }
        
        return redirect(url_for('secure_scanner', token=token))
    
    return redirect(url_for('pricing'))

@app.route('/scanner/<token>')
def secure_scanner(token):
    current_time = time.time()
    
    if token in ACTIVE_TOKENS:
        token_data = ACTIVE_TOKENS[token]
        if current_time <= token_data["expiry"]:
            return render_template_string(
                HTML_TEMPLATE, 
                page='scanner', 
                duration_name=token_data["plan_name"]
            )
        else:
            del ACTIVE_TOKENS[token]
            return "<h2 style='color:red; text-align:center; margin-top:50px;'>❌ This Access Link Has Expired! The purchased time duration is over.</h2>", 403
    else:
        return "<h2 style='color:red; text-align:center; margin-top:50px;'>❌ Invalid or Already Used Link!</h2>", 403

if __name__ == '__main__':
    app.run(debug=True, port=5000)
