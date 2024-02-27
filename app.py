from flask import Flask, request, render_template_string, jsonify

app = Flask(__name__)

# HTML form for entering transaction details
HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Credit Card Fraud Detection</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        form {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 400px;
        }
        h2 {
            text-align: center;
            color: #333;
        }
        label {
            font-weight: bold;
            color: #555;
        }
        input[type="text"],
        input[type="month"],
        input[type="number"] {
            width: 100%;
            padding: 8px;
            margin: 8px 0 16px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }
        input[type="submit"] {
            width: 100%;
            background-color: #007bff;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        input[type="submit"]:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <h2>Credit Card Transaction Form</h2>
    <form action="/detect-fraud" method="post">
        <label for="cardNumber">Card Number:</label><br>
        <input type="text" id="cardNumber" name="cardNumber" pattern="[0-9]{16}" title="Card number should be 16 digits" required><br>
        <label for="expiryDate">Expiry Date:</label><br>
        <input type="month" id="expiryDate" name="expiryDate" required><br>
        <label for="cvv">CVV:</label><br>
        <input type="text" id="cvv" name="cvv" pattern="[0-9]{3}" title="CVV should be 3 digits" required><br>
        <label for="amount">Amount:</label><br>
        <input type="number" id="amount" name="amount" step="0.01" required><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
'''

@app.route('/')
def form():
    return render_template_string(HTML)

@app.route('/detect-fraud', methods=['POST'])
def detect_fraud():
    # Extract transaction details from form
    card_number = request.form['cardNumber']
    expiry_date = request.form['expiryDate']
    cvv = request.form['cvv']
    amount = float(request.form['amount'])
    
    # Simple mock-up fraud detection logic
    # In a real system, this would involve complex algorithms and data analysis
    fraud_risk = "low"
    if amount > 10000:  # Example criterion for demonstration
        fraud_risk = "high"
    
    # Respond with whether the transaction is suspicious
    response = {
        "card_number": card_number,
        "expiry_date": expiry_date,
        "cvv": cvv,
        "amount": amount,
        "fraud_risk": fraud_risk
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
