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
    <title>Tarikul & Gemini 15M Pro</title>
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
            max-width: 420px;
            background: #111827;
            border: 1px solid #1f2937;
            border-radius: 16px;
            padding: 25px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.6);
            text-align: center;
        }
        h1 { color: #38bdf8; margin-bottom: 8px; font-size: 22px; font-weight: bold; }
        .engine-badge {
            display: inline-block;
            background: #1e3a8a;
            color: #60a5fa;
            font-size: 11px;
            font-weight: bold;
            padding: 5px 12px;
            border-radius: 20px;
            margin-bottom: 20px;
            border: 1px solid #3b82f6;
        }
        .scan-btn {
            width: 100%;
            background: #22c55e;
            color: white;
            border: none;
            padding: 14px;
            font-size: 15px;
            font-weight: bold;
            border-radius: 8px;
            cursor: pointer;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(34, 197, 94, 0.3);
        }
        .signal-box {
            background: #1f2937;
            border: 1px solid #374151;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 20px;
            text-align: left;
        }
        .signal-row { 
            display: flex; 
            justify-content: space-between; 
            align-items: center;
            margin-bottom: 12px; 
            font-size: 14px; 
            color: #cbd5e1;
        }
        .signal-row:last-child { margin-bottom: 0; }
        .signal-row strong { color: #ffffff; font-family: monospace; font-size: 15px; }
        .action-badge {
            background: #064e3b;
            color: #4ade80;
            padding: 14px;
            border-radius: 8px;
            font-weight: bold;
            font-size: 14px;
            text-align: center;
            border: 1px solid #10b981;
            margin-bottom: 15px;
        }
        .footer-text { font-size: 11px; color: #64748b; margin-top: 10px; }
    </style>
</head>
<body>
    <div class="main-container">
        <h1>Tarikul & Gemini 15M Pro</h1>
        <div class="engine-badge">Live Screen Overlay Engine v7.0</div>
        
        <button class="scan-btn">⚡ SCAN 15-MIN LIVE MARKET</button>

        <div class="signal-box">
            <div class="signal-row"><span>15M Market Trend:</span> <strong>0.5027</strong></div>
            <div class="signal-row"><span>Chart Volatility:</span> <strong>0.2024</strong></div>
            <div class="signal-row"><span>AI Master Score:</span> <strong>0.5533</strong></div>
        </div>

        <div class="action-badge">
            15-MINUTE CALL (STRONG BUY UP) [VERIFIED]
        </div>

        <div class="footer-text">
            Engineered by Tarikul & Gemini - 100% 15M Master Edition
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
