from flask import Flask, render_template, request

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
    return render_template('card_details.html', card=card)


@app.route('/cards')
def card_list():
	return render_template('cards.html', cards=cards)

if __name__ == '__main__':
    app.run(debug=True)