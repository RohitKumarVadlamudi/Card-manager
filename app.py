from flask import Flask, render_template, redirect,request, url_for

app= Flask(__name__)

#card details

cards = [
    {"name": "CIBC", "due_date": "2025-03-01", "min_payment": 100, "paid": False},
    {"name": "Neo Hudson", "due_date": "2025-03-05", "min_payment": 200, "paid": True},
    {"name": "Tims", "due_date": "2025-03-10", "min_payment": 150, "paid": False},
    {"name": "Triangle", "due_date": "2025-03-10", "min_payment": 150, "paid": False},
    {"name": "Walmart", "due_date": "2025-03-10", "min_payment": 150, "paid": False}
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
    
    # Update due date
    card['due_date'] = request.form['due_date']
    try:
    	card['min_payment'] = int(request.form['min_payment'])
    except:
    	card['min_payment']=card['min_payment']
    
    # Update payment status
    status = request.form['status']
    card['paid'] = True if status == 'paid' else False
    
    return redirect(url_for('card_details', card_id=card_id))


if __name__ == '__main__':
    app.run(debug=True)