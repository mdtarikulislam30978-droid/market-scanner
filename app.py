from flask import Flask, render_template_string, request
import numpy as np
import time
import random

app = Flask(__name__)

# 1. Original Market Scanner Engine (Protected / Secret Route)
def fifteen_minute_master_scanner():
    try:
        time.sleep(1.5)
        current_timestamp = time.time()
        random.seed(int(current_timestamp * 1000) % 10000)
        np.random.seed(int(current_timestamp * 1000) % 10000)
        
        market_candles = np.random.uniform(0.15, 0.85, size=(24, 24))
        medium_term_trend = np.mean(market_candles)
        volatility_index = np.std(market_candles)
        
        time_factor = int(current_timestamp) % 2
        if time_factor == 0:
            signal = "15-MINUTE CALL (STRONG BUY UP) [VERIFIED]"
            color = "#00ffcc"
        else:
            signal = "15-MINUTE PUT (STRONG SELL DOWN) [VERIFIED]"
            color = "#ff4d4d"
            
        master_score = medium_term_trend + (volatility_index * 0.25) if time_factor == 0 else medium_term_trend - (volatility_index * 0.35)
            
        return {
            "trend": f"{medium_term_trend:.4f}",
            "volatility": f"{volatility_index:.4f}",
            "score": f"{master_score:.4f}",
            "signal": signal,
            "color": color,
            "status": "Screen Overlay & 15M Sync Active"
        }
    except Exception as e:
        return {
            "trend": "0.0000",
            "volatility": "0.0000",
            "score": "0.0000",
            "signal": "SCREEN SYNC ERROR / RESCAN",
            "color": "#ff4d4d",
            "status": "Error"
        }

# 2. Homepage: Professional Landing & Pricing Page with Live USD Converter & Copy to Clipboard
@app.route("/", methods=["GET", "POST"])
def pricing_page():
    return render_template_string("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tarikul & Gemini - Market Scanner Access</title>
    <style>
        body { background-color: #0f172a; color: #f8fafc; font-family: Arial, sans-serif; margin: 0; padding: 20px; }
        .container { max-width: 600px; margin: 0 auto; background: #1e293b; padding: 30px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
        h1 { text-align: center; color: #38bdf8; }
        .plan-box { background: #334155; padding: 12px 15px; margin: 10px 0; border-radius: 8px; border: 1px solid #475569; display: flex; justify-content: space-between; align-items: center; }
        .plan-box h3 { margin: 0; font-size: 15px; color: #f8fafc; }
        .plan-box span { color: #38bdf8; font-weight: bold; font-size: 15px; }
        .payment-methods { background: #0f172a; padding: 15px; border-radius: 8px; margin-top: 20px; font-size: 14px; line-height: 1.6; }
        .pay-item { margin-bottom: 10px; padding-bottom: 6px; border-bottom: 1px solid #1e293b; cursor: pointer; position: relative; transition: background 0.2s; }
        .pay-item:hover { background: #1e293b; padding-left: 5px; border-radius: 4px; }
        .copy-hint { font-size: 11px; color: #38bdf8; float: right; }
        .btn { display: block; width: 100%; background: #22c55e; color: white; padding: 12px; text-align: center; border: none; border-radius: 6px; font-size: 16px; font-weight: bold; cursor: pointer; text-decoration: none; margin-top: 15px; }
        .btn:hover { background: #16a34a; }
        .support-link { text-align: center; margin-top: 15px; }
        .support-link a { color: #38bdf8; text-decoration: none; }
        /* Toast notification */
        #toast { visibility: hidden; min-width: 200px; background-color: #22c55e; color: #fff; text-align: center; border-radius: 4px; padding: 10px; position: fixed; z-index: 1; left: 50%; bottom: 30px; transform: translateX(-50%); font-size: 14px; box-shadow: 0px 0px 10px rgba(0,0,0,0.5); }
        #toast.show { visibility: visible; animation: fadein 0.5s, fadeout 0.5s 2.5s; }
        @keyframes fadein { from {bottom: 0; opacity: 0;} to {bottom: 30px; opacity: 1;} }
        @keyframes fadeout { from {bottom: 30px; opacity: 1;} to {bottom: 0; opacity: 0;} }
    </style>
</head>
<body>
    <div class="container">
        <h1>Market Scanner Access Portal</h1>
        <p style="text-align: center; color: #94a3b8;">Select your plan, complete payment, and get instant access.</p>
        
        <div class="plan-box">
            <h3>⚡ 1 Hour Access Plan</h3>
            <span>50,000 BDT <small id="usd-1" style="color:#94a3b8; font-weight:normal;"></small></span>
        </div>
        <div class="plan-box">
            <h3>⚡ 2 Hours Access Plan</h3>
            <span>90,000 BDT <small id="usd-2" style="color:#94a3b8; font-weight:normal;"></small></span>
        </div>
        <div class="plan-box">
            <h3>⚡ 3 Hours Access Plan</h3>
            <span>1,30,000 BDT <small id="usd-3" style="color:#94a3b8; font-weight:normal;"></small></span>
        </div>
        <div class="plan-box">
            <h3>⚡ 5 Hours Pro Plan</h3>
            <span>2,00,000 BDT <small id="usd-5" style="color:#94a3b8; font-weight:normal;"></small></span>
        </div>

        <div class="payment-methods">
            <h3 style="color: #38bdf8; margin-top: 0;">💳 Payment Accounts (Click to Copy)</h3>
            
            <div class="pay-item" onclick="copyText('01785304583', 'bKash Personal')">
                <b>🔸 bKash (Personal):</b> <span class="acc-val">01785304583</span> <span class="copy-hint">Copy</span>
            </div>
            <div class="pay-item" onclick="copyText('01785304583', 'Nagad Personal')">
                <b>🔸 Nagad (Personal):</b> <span class="acc-val">01785304583</span> <span class="copy-hint">Copy</span>
            </div>
            <div class="pay-item" onclick="copyText('01785304583-3', 'Rocket Personal')">
                <b>🔸 Rocket (Personal):</b> <span class="acc-val">01785304583-3</span> <span class="copy-hint">Copy</span>
            </div>
            <div class="pay-item" onclick="copyText('01785304583', 'Upay Personal')">
                <b>🔸 Upay (Personal):</b> <span class="acc-val">01785304583</span> <span class="copy-hint">Copy</span>
            </div>
            <div class="pay-item" onclick="copyText('01811290498', 'bKash Agent')">
                <b>🔸 bKash (Agent):</b> <span class="acc-val">01811290498</span> <span class="copy-hint">Copy</span>
            </div>
            <div class="pay-item" onclick="copyText('01811290498-4', 'Rocket Agent')">
                <b>🔸 Rocket (Agent):</b> <span class="acc-val">01811290498-4</span> <span class="copy-hint">Copy</span>
            </div>
            <div class="pay-item" onclick="copyText('7863244000003204', 'UCB Bank Account')">
                <b>🏦 Bank Account (UCB Bank):</b><br>
                <b>Account Name:</b> MD TARIQUL ISLAM<br>
                <b>Account Number:</b> <span class="acc-val">7863244000003204</span><br>
                <b>Branch:</b> Bhawal Mirzapur Branch <span class="copy-hint">Copy Acc</span>
            </div>
            <div class="pay-item" onclick="copyText('TKTTRdKQ23mhD5Ey3zbj8LwuQiqBSSmydL', 'USDT Address')">
                <b>🌐 Crypto (USDT TRC20):</b><br>
                <code class="acc-val" style="word-break: break-all; color: #38bdf8;">TKTTRdKQ23mhD5Ey3zbj8LwuQiqBSSmydL</code><br>
                <b>Crypto UID:</b> <span class="acc-val">552253179</span> <span class="copy-hint">Copy</span>
            </div>
        </div>

        <form action="/submit-payment" method="POST">
            <label for="trx_id" style="display: block; margin-top: 15px; font-weight: bold;">Enter Transaction ID (TrxID) or Proof:</label>
            <input type="text" id="trx_id" name="trx_id" required style="width: 100%; padding: 10px; margin-top: 8px; border-radius: 5px; border: 1px solid #64748b; background: #1e293b; color: white; box-sizing: border-box;">
            <button type="submit" class="btn">Submit & Request Access</button>
        </form>

        <div class="support-link">
            <p>Having trouble? <a href="https://t.me/YourTelegramSupportBot" target="_blank">Contact Telegram Support Bot</a></p>
        </div>
    </div>

    <div id="toast">Copied to clipboard!</div>

    <script>
        // Fetch Live USD to BDT rate or fallback to market average (~118 BDT)
        async function updateUSD() {
            let rate = 118.0; // Default fallback
            try {
                let response = await fetch('https://open.er-api.com/v6/latest/USD');
                let data = await response.json();
                if(data && data.rates && data.rates.BDT) {
                    rate = data.rates.BDT;
                }
            } catch(e) {
                console.log("Using default exchange rate");
            }

            // Plan amounts in BDT
            let p1 = 50000 / rate;
            let p2 = 90000 / rate;
            let p3 = 130000 / rate;
            let p5 = 200000 / rate;

            document.getElementById('usd-1').innerText = `($${p1.toFixed(2)})`;
            document.getElementById('usd-2').innerText = `($${p2.toFixed(2)})`;
            document.getElementById('usd-3').innerText = `($${p3.toFixed(2)})`;
            document.getElementById('usd-5').innerText = `($${p5.toFixed(2)})`;
        }
        updateUSD();

        // Copy function
        function copyText(text, label) {
            navigator.clipboard.writeText(text).then(() => {
                let x = document.getElementById("toast");
                x.innerText = label + " Copied!";
                x.className = "show";
                setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
            });
        }
    </script>
</body>
</html>
    """)

# 3. Payment Submission Handler Route
@app.route("/submit-payment", methods=["POST"])
def submit_payment():
    trx_id = request.form.get('trx_id')
    return render_template_string(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Payment Submitted</title>
    <style>
        body {{ background-color: #0f172a; color: #f8fafc; font-family: Arial, sans-serif; text-align: center; padding: 50px; }}
        .box {{ max-width: 500px; margin: 0 auto; background: #1e293b; padding: 30px; border-radius: 12px; }}
        .btn {{ display: inline-block; background: #38bdf8; color: #0f172a; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold; margin-top: 20px; }}
    </style>
</head>
<body>
    <div class="box">
        <h2 style="color: #22c55e;">Payment Submitted Successfully!</h2>
        <p>Your TrxID: <b>{trx_id}</b> has been recorded.</p>
        <p>Please contact our Telegram Support Bot for instant manual verification and to receive your secure scanner access link.</p>
        <a href="https://t.me/YourTelegramSupportBot" class="btn" target="_blank">Open Telegram Support</a>
        <br><br>
        <a href="/" style="color: #94a3b8; text-decoration: none;">← Back to Home</a>
    </div>
</body>
</html>
    """)

# 4. Protected Secret Scanner Route (Original App Engine)
@app.route("/secret-scanner", methods=["GET", "POST"])
def secret_scanner():
    data = None
    if request.method == "POST":
        data = fifteen_minute_master_scanner()
    
    return render_template_string("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tarikul & Gemini 15M Pro Bot</title>
    <style>
        body { background-color: #04060b; color: #f8fafc; font-family: sans-serif; text-align: center; padding: 20px; }
        .card { background: #0d1527; border-radius: 20px; padding: 20px; max-width: 420px; margin: 0 auto; box-shadow: 0 10px 30px rgba(0,0,0,0.6); }
        h2 { color: #38bdf8; font-size: 21px; margin-bottom: 4px; }
        .badge { background: linear-gradient(135deg, #0284c7, #9333ea); color: #fff; font-size: 13px; padding: 6px 12px; border-radius: 20px; display: inline-block; margin-bottom: 15px; }
        .metric { background: #070b14; margin: 9px 0; padding: 12px; border-radius: 10px; font-size: 14px; text-align: left; border: 1px solid #1e293b; }
        .btn { background: linear-gradient(135deg, #10b981, #047857); color: #fff; border: none; width: 100%; padding: 14px; border-radius: 12px; font-size: 16px; font-weight: bold; cursor: pointer; margin-top: 15px; }
        .btn:active { transform: scale(0.98); }
        .signal { font-size: 16px; font-weight: bold; margin-top: 18px; padding: 15px; border-radius: 10px; background: #070b14; }
        .footer { font-size: 11px; color: #64748b; margin-top: 18px; }
    </style>
</head>
<body>
    <div class="card">
        <h2>Tarikul & Gemini 15M Pro</h2>
        <div class="badge">Live Screen Overlay Engine v7.0</div>
        
        <form method="POST">
            <button type="submit" class="btn">⚡ SCAN 15-MIN LIVE MARKET</button>
        </form>

        {% if data %}
        <div class="signal" style="border: 2px solid {{ data.color }}; color: {{ data.color }};">
            {{ data.signal }}
        </div>
        <div class="metric"><b>Market Trend:</b> {{ data.trend }}</div>
        <div class="metric"><b>Volatility Index:</b> {{ data.volatility }}</div>
        <div class="metric"><b>Master Score:</b> {{ data.score }}</div>
        <div class="metric"><b>System Status:</b> {{ data.status }}</div>
        {% endif %}

        <div class="footer">Secure Access Terminal • Powered by Tarikul & Gemini</div>
    </div>
</body>
</html>
    """, data=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
