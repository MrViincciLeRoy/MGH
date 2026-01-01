from flask import Flask, render_template, request, jsonify, redirect, url_for
from datetime import datetime
import json
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

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
                'votes': 0
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
    return render_template('index.html', 
                         contestants=contestants,
                         vote_packages=VOTE_PACKAGES,
                         bank_details=BANK_DETAILS,
                         contact_info=CONTACT_INFO,
                         closing_date=CLOSING_DATE,
                         days_remaining=max(0, days_remaining))

@app.route('/gallery')
def gallery():
    contestants = load_contestants()
    return render_template('gallery.html', contestants=contestants)

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
