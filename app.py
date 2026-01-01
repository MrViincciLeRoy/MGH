from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from datetime import datetime
import json
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here-change-in-production'

# Database file paths
CONTESTANTS_FILE = 'data/contestants.json'
VOTES_FILE = 'data/votes.json'

# Ensure data directory exists
os.makedirs('data', exist_ok=True)

# Initialize data files if they don't exist
def init_data():
    if not os.path.exists(CONTESTANTS_FILE):
        contestants = [
            {
                'id': 'M22',
                'name': 'Angel Lekala',
                'status': 'Semi-Finalist',
                'image': 'angel_lekala.jpg',
                'votes': 0,
                'bio': 'A passionate and driven young woman who believes in empowering others.',
                'age': 22,
                'location': 'Pretoria',
                'gallery': ['angel_lekala_1.jpg', 'angel_lekala_2.jpg', 'angel_lekala_3.jpg']
            }
        ]
        with open(CONTESTANTS_FILE, 'w') as f:
            json.dump(contestants, f, indent=2)
    
    if not os.path.exists(VOTES_FILE):
        with open(VOTES_FILE, 'w') as f:
            json.dump({}, f)

init_data()

# Voting packages
VOTE_PACKAGES = {
    '50': {'price': 50, 'votes': 20},
    '100': {'price': 100, 'votes': 60},
    '200': {'price': 200, 'votes': 120},
    '300': {'price': 300, 'votes': 300}
}

# Bank details
BANK_DETAILS = {
    'bank_name': 'Capitec',
    'account_holder': 'CT Mohlala',
    'account_number': '1694576912',
    'linked_number': '0681019320'
}

# Contact information
CONTACT_INFO = {
    'whatsapp': ['0673083980', '0681019320'],
    'facebook': 'Miss Gorgeous Hearts Pretoria',
    'instagram': 'gorg.eousheartspretoria',
    'tiktok': 'miss.gorgeous.hearts.pt4'
}

CLOSING_DATE = datetime(2026, 4, 30)

def load_contestants():
    with open(CONTESTANTS_FILE, 'r') as f:
        return json.load(f)

def save_contestants(contestants):
    with open(CONTESTANTS_FILE, 'w') as f:
        json.dump(contestants, f, indent=2)

def load_votes():
    with open(VOTES_FILE, 'r') as f:
        return json.load(f)

def save_votes(votes):
    with open(VOTES_FILE, 'w') as f:
        json.dump(votes, f, indent=2)

@app.route('/')
def index():
    contestants = load_contestants()
    days_remaining = (CLOSING_DATE - datetime.now()).days
    
    # Get top 3 contestants for preview
    top_contestants = sorted(contestants, key=lambda x: x['votes'], reverse=True)[:3]
    
    return render_template('index.html', 
                         contestants=contestants,
                         top_contestants=top_contestants,
                         vote_packages=VOTE_PACKAGES,
                         bank_details=BANK_DETAILS,
                         contact_info=CONTACT_INFO,
                         closing_date=CLOSING_DATE,
                         days_remaining=max(0, days_remaining))

@app.route('/gallery')
def gallery():
    contestants = load_contestants()
    return render_template('gallery.html', contestants=contestants)

@app.route('/contestant/<contestant_id>')
def contestant_profile(contestant_id):
    contestants = load_contestants()
    contestant = next((c for c in contestants if c['id'] == contestant_id), None)
    if not contestant:
        return redirect(url_for('index'))
    
    # Get other contestants for suggestions
    other_contestants = [c for c in contestants if c['id'] != contestant_id][:3]
    
    return render_template('contestant_profile.html', 
                         contestant=contestant,
                         other_contestants=other_contestants,
                         vote_packages=VOTE_PACKAGES)

@app.route('/leaderboard')
def leaderboard():
    contestants = load_contestants()
    # Sort contestants by votes (descending)
    sorted_contestants = sorted(contestants, key=lambda x: x['votes'], reverse=True)
    
    # Calculate statistics
    total_votes = sum(c['votes'] for c in contestants)
    total_contestants = len(contestants)
    finalists = len([c for c in contestants if c['votes'] >= 400])
    
    stats = {
        'total_votes': total_votes,
        'total_contestants': total_contestants,
        'finalists': finalists,
        'average_votes': total_votes // total_contestants if total_contestants > 0 else 0
    }
    
    return render_template('leaderboard.html', 
                         contestants=sorted_contestants,
                         stats=stats,
                         closing_date=CLOSING_DATE)

@app.route('/about')
def about():
    return render_template('about.html',
                         contact_info=CONTACT_INFO,
                         closing_date=CLOSING_DATE)

@app.route('/vote/<contestant_id>')
def vote_page(contestant_id):
    contestants = load_contestants()
    contestant = next((c for c in contestants if c['id'] == contestant_id), None)
    if not contestant:
        return redirect(url_for('index'))
    return render_template('vote.html', 
                         contestant=contestant,
                         vote_packages=VOTE_PACKAGES,
                         bank_details=BANK_DETAILS,
                         contact_info=CONTACT_INFO)

@app.route('/checkout/<contestant_id>/<package_id>')
def checkout(contestant_id, package_id):
    contestants = load_contestants()
    contestant = next((c for c in contestants if c['id'] == contestant_id), None)
    
    if not contestant or package_id not in VOTE_PACKAGES:
        return redirect(url_for('index'))
    
    package = VOTE_PACKAGES[package_id]
    
    # Store checkout info in session
    session['checkout'] = {
        'contestant_id': contestant_id,
        'contestant_name': contestant['name'],
        'package_id': package_id,
        'amount': package['price'],
        'votes': package['votes']
    }
    
    return render_template('checkout.html',
                         contestant=contestant,
                         package=package,
                         package_id=package_id,
                         bank_details=BANK_DETAILS,
                         contact_info=CONTACT_INFO)

@app.route('/process-payment', methods=['POST'])
def process_payment():
    # This is a mock payment processor
    # In production, you'd integrate with a real payment gateway
    
    if 'checkout' not in session:
        return redirect(url_for('index'))
    
    checkout_data = session['checkout']
    payment_method = request.form.get('payment_method', 'bank_transfer')
    
    # Generate a mock transaction ID
    import random
    transaction_id = f"TXN{random.randint(100000, 999999)}"
    
    # Store transaction info
    session['transaction'] = {
        'transaction_id': transaction_id,
        'contestant_id': checkout_data['contestant_id'],
        'contestant_name': checkout_data['contestant_name'],
        'amount': checkout_data['amount'],
        'votes': checkout_data['votes'],
        'payment_method': payment_method,
        'timestamp': datetime.now().isoformat()
    }
    
    # Clear checkout from session
    session.pop('checkout', None)
    
    return redirect(url_for('success'))

@app.route('/success')
def success():
    if 'transaction' not in session:
        return redirect(url_for('index'))
    
    transaction = session['transaction']
    
    return render_template('success.html',
                         transaction=transaction,
                         contact_info=CONTACT_INFO)

@app.route('/how-to-vote')
def how_to_vote():
    return render_template('how_to_vote.html',
                         vote_packages=VOTE_PACKAGES,
                         bank_details=BANK_DETAILS,
                         contact_info=CONTACT_INFO)

@app.route('/api/contestants')
def get_contestants():
    contestants = load_contestants()
    return jsonify(contestants)

@app.route('/api/vote', methods=['POST'])
def submit_vote():
    data = request.json
    contestant_id = data.get('contestant_id')
    votes_count = data.get('votes')
    
    contestants = load_contestants()
    for contestant in contestants:
        if contestant['id'] == contestant_id:
            contestant['votes'] += votes_count
            save_contestants(contestants)
            return jsonify({'success': True, 'new_vote_count': contestant['votes']})
    
    return jsonify({'success': False, 'error': 'Contestant not found'}), 404

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    # Simple password protection - change this password!
    ADMIN_PASSWORD = 'gorgeoushearts2026'
    
    if request.method == 'POST':
        # Check if adding votes
        if request.form.get('authenticated') == 'true':
            contestant_id = request.form.get('contestant_id')
            votes_to_add = int(request.form.get('votes_to_add', 0))
            
            contestants = load_contestants()
            for contestant in contestants:
                if contestant['id'] == contestant_id:
                    contestant['votes'] += votes_to_add
                    save_contestants(contestants)
                    return render_template('admin.html', 
                                         contestants=contestants,
                                         authenticated=True,
                                         success=f'Successfully added {votes_to_add} votes to {contestant["name"]}!')
        
        # Check password
        password = request.form.get('password')
        if password == ADMIN_PASSWORD:
            contestants = load_contestants()
            return render_template('admin.html', 
                                 contestants=contestants,
                                 authenticated=True)
        else:
            return render_template('admin.html', 
                                 authenticated=False,
                                 error='Incorrect password')
    
    return render_template('admin.html', authenticated=False)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
