from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/your_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Card Model
class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    max_limit = db.Column(db.Integer, nullable=False)
    used = db.Column(db.Integer, nullable=False)
    available = db.Column(db.Integer, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    minimum_payment = db.Column(db.Numeric(10, 2), nullable=False)
    paid = db.Column(db.Boolean, default=False)

# Redirect home to the cards page
@app.route('/')
def home():
    return redirect(url_for('card_list'))  # Redirects to /cards

# Display all cards
@app.route('/cards')
def card_list():
    cards = Card.query.all()  # Fetch all cards from DB
    return render_template('cards.html', cards=cards)

# Card details route
@app.route('/card/<int:card_id>')
def card_details(card_id):
    card = Card.query.get_or_404(card_id)  # Fetch card by ID
    return render_template('card_details.html', card=card)

# Update card details
@app.route('/update_card/<int:card_id>', methods=['POST'])
def update_card(card_id):
    card = Card.query.get_or_404(card_id)

    card.due_date = request.form['due_date']
    card.minimum_payment = request.form['min_payment']

    # Update payment status
    status = request.form['status']
    card.paid = True if status == 'paid' else False

    db.session.commit()  # Save changes to DB
    return redirect(url_for('card_details', card_id=card_id))

if __name__ == '__main__':
    app.run(debug=True)
