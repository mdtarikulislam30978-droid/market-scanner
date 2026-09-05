from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def pricing_page():
    return render_template('pricing.html')

@app.route('/submit-payment', methods=['POST'])
def submit_payment():
    trx_id = request.form.get('trx_id')
    return f"<h3>Thank you! Your payment proof (TrxID: {trx_id}) has been received. Please contact our Telegram Support Bot for instant verification and access link.</h3><br><a href='/'>Go Back</a>"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
