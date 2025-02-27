from flask import Flask, render_template, request

app= Flask(__name__)

@app.route('/')

def home:
	return "Welcome to credit card manager"

if __name__ == '__main__':
    app.run(debug=True)


#card details

cards = [
    {"name": "CIBC", "due_date": "2025-03-01", "min_payment": 100, "paid": False},
    {"name": "Neo Hudson", "due_date": "2025-03-05", "min_payment": 200, "paid": True},
    {"name": "Tims", "due_date": "2025-03-10", "min_payment": 150, "paid": False},
    {"name": "Triangle", "due_date": "2025-03-10", "min_payment": 150, "paid": False},
    {"name": "Walmart", "due_date": "2025-03-10", "min_payment": 150, "paid": False}
]


@app.route('/cards')
def card_list:
	render_template('cards.html', cards=cards)