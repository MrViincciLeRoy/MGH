# File Structure Guide

## 📁 What Each File Does

```
miss_gorgeous_hearts/
│
├── 🚀 START HERE
│   ├── start.bat                  ← Double-click this on Windows
│   ├── start.sh                   ← Run this on Mac/Linux
│   └── QUICK_SETUP.md            ← Read this first!
│
├── 📖 DOCUMENTATION
│   ├── README.md                  ← Full detailed guide
│   └── FILE_STRUCTURE.md         ← This file!
│
├── 🐍 PYTHON APPLICATION
│   ├── app.py                     ← Main Flask application
│   └── requirements.txt           ← Python dependencies
│
├── 💾 DATA FILES (Edit these!)
│   └── data/
│       ├── contestants.json       ← Add contestants here
│       └── votes.json            ← Vote tracking data
│
├── 🎨 WEBSITE FILES
│   ├── static/                    ← Public files
│   │   ├── css/
│   │   │   └── style.css         ← All styling (colors, layout)
│   │   ├── js/
│   │   │   └── script.js         ← Interactive features
│   │   └── images/               ← PUT CONTESTANT PHOTOS HERE!
│   │       ├── angel_lekala.jpg  ← Example contestant photo
│   │       └── placeholder.jpg   ← Backup image
│   │
│   └── templates/                 ← HTML pages
│       ├── index.html            ← Home page
│       ├── gallery.html          ← Contestants gallery
│       ├── vote.html             ← Individual voting page
│       ├── how_to_vote.html      ← Voting guide
│       └── admin.html            ← Admin panel
│
└── 🗑️ TEMPORARY FILES (Auto-generated)
    └── __pycache__/               ← Python cache (ignore this)
```

## 📝 Files You'll Need to Edit

### 1. Adding Contestants
**File:** `data/contestants.json`
```json
{
  "id": "M22",              ← Unique ID
  "name": "Angel Lekala",   ← Full name
  "status": "Semi-Finalist", ← Status badge
  "image": "angel_lekala.jpg", ← Photo filename
  "votes": 0                ← Starting votes
}
```

### 2. Bank Details
**File:** `app.py` (Line ~49)
```python
BANK_DETAILS = {
    'bank_name': 'Capitec',
    'account_holder': 'CT Mohlala',
    'account_number': '1694576912',
    'linked_number': '0681019320'
}
```

### 3. Contact Information
**File:** `app.py` (Line ~57)
```python
CONTACT_INFO = {
    'whatsapp': ['0673083980', '0681019320'],
    'facebook': 'Miss Gorgeous Hearts Pretoria',
    'instagram': 'gorg.eousheartspretoria',
    'tiktok': 'miss.gorgeous.hearts.pt4'
}
```

### 4. Admin Password
**File:** `app.py` (Line ~76)
```python
ADMIN_PASSWORD = 'gorgeoushearts2026'  ← CHANGE THIS!
```

### 5. Closing Date
**File:** `app.py` (Line ~64)
```python
CLOSING_DATE = datetime(2026, 4, 30)
```

### 6. Theme Colors
**File:** `static/css/style.css` (Lines 1-8)
```css
:root {
    --gold: #D4AF37;
    --dark-gold: #B8941E;
    --light-gold: #F4E5C2;
    --black: #000000;
}
```

## 🖼️ Adding Contestant Photos

1. **Prepare your image:**
   - Recommended size: 800x1000 pixels (portrait)
   - Format: .jpg, .jpeg, or .png
   - Good quality but not too large (under 2MB)

2. **Rename the file:**
   - Use lowercase
   - Replace spaces with underscores
   - Example: "Angel Lekala.jpg" → "angel_lekala.jpg"

3. **Add to folder:**
   - Copy photo to: `static/images/`

4. **Update contestants.json:**
   - Add contestant entry with matching filename

## 🎯 Common Tasks

### Adding a New Contestant
1. Add photo to `static/images/`
2. Edit `data/contestants.json`
3. Restart the website

### Changing Vote Packages
Edit `app.py` (Line ~34):
```python
VOTE_PACKAGES = {
    '50': {'price': 50, 'votes': 20},
    '100': {'price': 100, 'votes': 60},
    '200': {'price': 200, 'votes': 120},
    '300': {'price': 300, 'votes': 300}
}
```

### Adding Votes (After Payment)
1. Go to: http://localhost:5000/admin
2. Login with password
3. Find contestant
4. Enter votes to add
5. Click "Add Votes"

### Backing Up Your Data
**Copy these files regularly:**
- `data/contestants.json`
- `data/votes.json`
- `static/images/` folder

## 🔧 Technical Files (Don't Edit Unless You Know Python/Web Dev)

- `app.py` - Flask application logic
- `templates/*.html` - Page structures
- `static/css/style.css` - Styling rules
- `static/js/script.js` - JavaScript code

## 📊 Data Flow

```
1. User visits website
   ↓
2. Flask (app.py) loads data from contestants.json
   ↓
3. Templates (HTML) display the data
   ↓
4. CSS makes it look beautiful
   ↓
5. JavaScript adds interactivity
```

## 🔄 Vote Processing Flow

```
1. Someone makes payment
   ↓
2. They WhatsApp proof with contestant code
   ↓
3. You verify payment in bank
   ↓
4. You login to admin panel
   ↓
5. You add votes for that contestant
   ↓
6. contestants.json is updated
   ↓
7. Website shows new vote count immediately
```

## 🆘 Troubleshooting by File

### Images Not Showing
**Check:**
- Is file in `static/images/`?
- Does filename in `contestants.json` match exactly?
- Is file format supported (.jpg, .jpeg, .png)?

### Votes Not Saving
**Check:**
- Can you write to `data/contestants.json`?
- Is JSON format valid? (Use online JSON validator)
- Is website running with proper permissions?

### Styling Looks Wrong
**Check:**
- Is `static/css/style.css` present?
- Are there any CSS syntax errors?
- Try clearing browser cache (Ctrl+F5)

### Pages Not Loading
**Check:**
- Are all files in `templates/` present?
- Is Flask running? (Check terminal)
- Any error messages in terminal?

## 💡 Quick Tips

1. **Always backup before editing**
2. **Edit one thing at a time**
3. **Restart website after changes to Python files**
4. **Refresh browser (Ctrl+F5) after CSS changes**
5. **Check terminal for error messages**

## 📱 Mobile Testing

1. Start website on computer
2. Find computer's IP address
3. On phone, go to: `http://COMPUTER_IP:5000`
4. Test all pages
5. Test on different screen sizes

## 🌐 Website Pages

| URL | Page | Purpose |
|-----|------|---------|
| / | Home | Welcome and overview |
| /gallery | Gallery | View all contestants |
| /vote/M22 | Vote Page | Vote for specific contestant |
| /how-to-vote | Guide | Voting instructions |
| /admin | Admin | Manage votes (password protected) |

## 🎨 Customization Levels

**Easy (No coding):**
- Add contestant photos
- Update bank details
- Change contact info
- Change admin password

**Medium (Basic editing):**
- Change colors
- Update text content
- Adjust vote packages
- Change closing date

**Advanced (Requires coding):**
- Modify layouts
- Add new features
- Change functionality
- Add payment integration

---

**Need more help? Check QUICK_SETUP.md or README.md!**
