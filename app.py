from flask import Flask, render_template_string
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Market Pro Scanner - Lifetime Access</title>
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
            max-width: 550px;
            background: #111827;
            border: 1px solid #1f2937;
            border-radius: 12px;
            padding: 30px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.5);
            text-align: center;
        }
        h1 { color: #38bdf8; margin-bottom: 10px; font-size: 24px; }
        p { color: #34d399; font-size: 14px; margin-bottom: 20px; font-weight: bold; }
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
            margin-bottom: 20px;
        }
        .submit-btn:hover { background: #16a34a; }
        .signal-box {
            background: #1f2937;
            border: 1px solid #374151;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            text-align: left;
        }
        .signal-row { display: flex; justify-content: space-between; margin-bottom: 12px; font-size: 15px; }
        .signal-badge {
            background: #14532d;
            color: #4ade80;
            padding: 12px;
            border-radius: 6px;
            font-weight: bold;
            text-align: center;
            border: 1px solid #16a34a;
            margin-bottom: 15px;
        }
        .warning-text { font-size: 12px; color: #facc15; }
    </style>
</head>
<body>
    <div class="main-container">
        <h1>Market Pro Scanner</h1>
        <p>Active Plan Duration: Lifetime Access Portal</p>
        
        <button class="submit-btn">⚡ SCAN LIVE MARKET</button>

        <div class="signal-box">
            <div class="signal-row"><span>Market Trend:</span> <strong style="color: #34d399;">Bullish / Buy</strong></div>
            <div class="signal-row"><span>Volatility Score:</span> <strong style="color: #38bdf8;">Stable</strong></div>
            <div class="signal-row"><span>AI Master Index:</span> <strong style="color: #fbbf24;">Verified</strong></div>
        </div>

        <div class="signal-badge">
            LIVE TRADING SIGNAL ACTIVE
        </div>

        <div class="warning-text">
            ⚠️ Note: This link is valid for lifetime access and operates automatically.
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
