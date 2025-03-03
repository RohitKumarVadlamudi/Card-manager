from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:4EVERre:monster@localhost/card_manager'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Card Model
class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    max_limit = db.Column(db.Numeric(10,2), nullable=False)
    used = db.Column(db.Numeric(10,2), nullable=False)
    available = db.Column(db.Numeric(10,2), nullable=False)
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

# Add a new card
@app.route('/add_card', methods=['GET', 'POST'])
def add_card():
    if request.method == 'POST':
        name = request.form['name']
        max_limit = float(request.form['max_limit'])
        used = float(request.form['used'])
        available = max_limit - used
        due_date = request.form['due_date']
        minimum_payment = float(request.form['minimum_payment'])

        new_card = Card(
            name=name,
            max_limit=max_limit,
            used=used,
            available=available,
            due_date=due_date,
            minimum_payment=minimum_payment
        )

        db.session.add(new_card)
        db.session.commit()

        return redirect(url_for('card_list'))  # Redirect to cards list after saving

    return render_template('add_card.html')

if __name__ == '__main__':
    app.run(debug=True)
