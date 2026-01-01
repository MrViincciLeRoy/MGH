# Quick Setup Guide - Miss Gorgeous Hearts Website

## 🚀 Quick Start (3 Easy Steps!)

### Step 1: Install Python
- Download Python 3.8+ from: https://www.python.org/downloads/
- During installation, **check "Add Python to PATH"**
- Restart your computer after installation

### Step 2: Add Contestant Photos
- Put contestant photos in the `static/images/` folder
- The first contestant should be named: `angel_lekala.jpg`
- Add more contestants by editing `data/contestants.json`

### Step 3: Run the Website

**On Windows:**
- Double-click `start.bat`

**On Mac/Linux:**
- Open Terminal in this folder
- Run: `./start.sh`

**Alternative (All Systems):**
```bash
pip install -r requirements.txt
python app.py
```

## 🌐 Access the Website

Once running, open your browser and go to:
- **Local access:** http://localhost:5000
- **From other devices:** http://YOUR_COMPUTER_IP:5000

## 🔐 Admin Panel

Access the admin panel to add votes:
- URL: http://localhost:5000/admin
- Default password: `gorgeoushearts2026`
- **IMPORTANT:** Change this password in `app.py` line 76!

## 📝 Adding More Contestants

1. Add contestant photo to `static/images/`
2. Open `data/contestants.json`
3. Add new entry:
```json
{
  "id": "M23",
  "name": "New Contestant Name",
  "status": "Semi-Finalist",
  "image": "photo_filename.jpg",
  "votes": 0
}
```
4. Restart the website

## 💰 Update Bank Details

Edit these lines in `app.py` (around line 49):
```python
BANK_DETAILS = {
    'bank_name': 'Your Bank',
    'account_holder': 'Your Name',
    'account_number': '1234567890',
    'linked_number': '0123456789'
}
```

## 📞 Update Contact Info

Edit these lines in `app.py` (around line 57):
```python
CONTACT_INFO = {
    'whatsapp': ['0123456789', '0987654321'],
    'facebook': 'Your Page Name',
    'instagram': 'your_handle',
    'tiktok': 'your_handle'
}
```

## 🎨 Change Theme Colors

Edit `static/css/style.css` (lines 1-8):
```css
:root {
    --gold: #D4AF37;         /* Main gold color */
    --dark-gold: #B8941E;    /* Darker gold */
    --light-gold: #F4E5C2;   /* Light gold */
    --black: #000000;        /* Background */
}
```

## 📱 For Mobile Access

1. Make sure your computer and phones are on the same WiFi
2. Find your computer's IP address:
   - **Windows:** Open Command Prompt → type `ipconfig`
   - **Mac:** System Preferences → Network
   - **Linux:** Terminal → type `hostname -I`
3. Share this address: `http://YOUR_IP:5000`

## ⚠️ Troubleshooting

### "Port already in use"
- Another program is using port 5000
- Change port in `app.py` line 124: `app.run(port=5001)`

### Images not showing
- Check filenames match exactly (case-sensitive!)
- Supported formats: .jpg, .jpeg, .png
- Make sure files are in `static/images/`

### Can't access from other devices
- Check firewall settings
- Make sure devices are on same network
- Try disabling firewall temporarily to test

### Vote counts not saving
- Check file permissions on `data/contestants.json`
- Make sure the app has write access

## 🌟 Features Overview

### Public Pages:
1. **Home** - Welcome page with countdown
2. **Contestants Gallery** - View all contestants
3. **Individual Vote Pages** - Vote for specific contestants
4. **How to Vote** - Step-by-step guide

### Admin Features:
- Add votes after payment verification
- View current vote counts
- Track progress to finalist (400 votes)

## 🔒 Security Tips

1. **Change the admin password** immediately!
2. Don't share the admin URL publicly
3. For production, use HTTPS
4. Consider adding rate limiting
5. Back up `data/contestants.json` regularly

## 📊 Vote Management Process

1. Someone sends payment proof via WhatsApp
2. Verify the payment in your bank account
3. Go to admin panel: http://localhost:5000/admin
4. Enter password
5. Find the contestant
6. Add the number of votes they purchased
7. Votes appear immediately on the website!

## 🎯 Vote Packages

- R50 = 20 votes
- R100 = 60 votes  
- R200 = 120 votes
- R300 = 300 votes (Best value!)

## 📅 Important Dates

Closing Date: **30 April 2026**

To change this, edit `app.py` line 64:
```python
CLOSING_DATE = datetime(2026, 4, 30)
```

## 💾 Backup Your Data

**Important files to backup regularly:**
- `data/contestants.json` - All contestant info and votes
- `static/images/` - All contestant photos

## 🆘 Need Help?

For technical support:
- Check the full README.md for detailed information
- Contact WhatsApp: 0673083980 / 0681019320

## 🎉 Success Checklist

- [ ] Python installed
- [ ] Contestant photos added
- [ ] Bank details updated
- [ ] Contact info updated
- [ ] Admin password changed
- [ ] Website tested locally
- [ ] Mobile access tested
- [ ] Admin panel tested
- [ ] Vote tracking works

---

**You're ready to go! Good luck with the pageant! 👑✨**
