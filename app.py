from flask import Flask, render_template, request

app= Flask(__name__)

@app.route('/')

def home:
	return "Welcome to credit card manager"

if __name__ == '__main__':
    app.run(debug=True)


#card details

cards = [
    {"name": "Card 1", "due_date": "2025-03-01", "min_payment": 100, "paid": False},
    {"name": "Card 2", "due_date": "2025-03-05", "min_payment": 200, "paid": True},
    {"name": "Card 3", "due_date": "2025-03-10", "min_payment": 150, "paid": False}
]


@app.route('/cards')
def card_list:
	render_template('cards.html', cards=cards)