from flask import Flask, render_template, redirect,request, url_for

app= Flask(__name__)

#card details

cards = [
    {"name": "CIBC", "due_date": "2025-03-01", "min_payment": 100, "paid": False, "Limit":3000},
    {"name": "Neo Hudson", "due_date": "2025-03-05", "min_payment": 200, "paid": True,"Limit":3500},
    {"name": "Tims", "due_date": "2025-03-10", "min_payment": 150, "paid": False, "Limit":4000},
    {"name": "Triangle", "due_date": "2025-03-10", "min_payment": 150, "paid": False, "Limit":5500},
    {"name": "Walmart", "due_date": "2025-03-10", "min_payment": 150, "paid": False, "Limit":4500}
]




@app.route('/')

def home():
	return "Welcome to credit card manager"

@app.route('/card/<int:card_id>')
def card_details(card_id):
    card = cards[card_id]
    return render_template('card_details.html', card=card, card_id=card_id)


@app.route('/cards')
def card_list():
	return render_template('cards.html', cards=cards)

@app.route('/update_card/<int:card_id>', methods=['POST'])
def update_card(card_id):
    card = cards[card_id]

    due_date = request.form.get('due_date')
    min_payment = request.form.get('min_payment')
    
    # Update due date
    card['due_date'] = request.form['due_date']


    #update min payment
    if not min_payment.isdigit():  # Only check if it's a string that can be converted to int
        error_message = "Minimum payment must be a number."
        return render_template('card_details.html', card=card, card_id=card_id, error_message=error_message)
    
    
    # Update payment status
    status = request.form['status']
    card['paid'] = True if status == 'paid' else False
    
    return redirect(url_for('card_details', card_id=card_id))


if __name__ == '__main__':
    app.run(debug=True)