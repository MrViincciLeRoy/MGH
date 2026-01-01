# Miss Gorgeous Hearts Pretoria 2026 - Voting Website

A beautiful and elegant voting platform for the Miss Gorgeous Hearts Pretoria 2026 pageant. Built with Flask (Python) and featuring a stunning gold and black theme.

## Features

- **Home Page**: Welcoming hero section with countdown timer, about section, contestant previews, voting packages, and contact information
- **Contestants Gallery**: View all contestants with filtering options and progress tracking
- **Individual Voting Pages**: Dedicated pages for each contestant with voting instructions
- **How to Vote Guide**: Step-by-step instructions for supporters
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Elegant Theme**: Gold and black color scheme with animated sparkles and stars
- **Vote Tracking**: Real-time vote count display and progress to finalist status (400 votes)

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. **Extract the project files** to your desired location

2. **Install Python dependencies**:
   ```bash
   cd miss_gorgeous_hearts
   pip install -r requirements.txt
   ```

3. **Add contestant images**:
   - Place contestant photos in `static/images/` folder
   - Name the images as specified in the `data/contestants.json` file
   - Recommended image size: 800x1000 pixels or similar portrait ratio
   - Supported formats: .jpg, .jpeg, .png

4. **Configure contestants** (optional):
   - Edit `data/contestants.json` to add more contestants
   - Each contestant needs: id, name, status, image filename, and initial votes

## Running the Application

1. **Start the Flask server**:
   ```bash
   python app.py
   ```

2. **Access the website**:
   - Open your web browser
   - Go to: `http://localhost:5000`
   - Or from another device on the same network: `http://YOUR_IP_ADDRESS:5000`

3. **Stop the server**:
   - Press `Ctrl+C` in the terminal

## Project Structure

```
miss_gorgeous_hearts/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── data/
│   ├── contestants.json        # Contestant data
│   └── votes.json             # Vote tracking data
├── static/
│   ├── css/
│   │   └── style.css          # Stylesheet
│   ├── js/
│   │   └── script.js          # JavaScript functionality
│   └── images/                # Contestant photos
├── templates/
│   ├── index.html             # Home page
│   ├── gallery.html           # Contestants gallery
│   ├── vote.html              # Individual voting page
│   └── how_to_vote.html       # Voting instructions
```

## Adding New Contestants

1. **Add contestant photo** to `static/images/`

2. **Update contestants.json**:
   ```json
   {
     "id": "M23",
     "name": "New Contestant",
     "status": "Semi-Finalist",
     "image": "new_contestant.jpg",
     "votes": 0
   }
   ```

3. **Restart the application** to see changes

## Customization

### Changing Colors
Edit the CSS variables in `static/css/style.css`:
```css
:root {
    --gold: #D4AF37;
    --dark-gold: #B8941E;
    --light-gold: #F4E5C2;
    --black: #000000;
}
```

### Changing Bank Details
Edit the `BANK_DETAILS` dictionary in `app.py`:
```python
BANK_DETAILS = {
    'bank_name': 'Your Bank',
    'account_holder': 'Your Name',
    'account_number': '1234567890',
    'linked_number': '0123456789'
}
```

### Changing Contact Information
Edit the `CONTACT_INFO` dictionary in `app.py`:
```python
CONTACT_INFO = {
    'whatsapp': ['0123456789', '0987654321'],
    'facebook': 'Your Page Name',
    'instagram': 'your_handle',
    'tiktok': 'your_handle'
}
```

### Changing Closing Date
Edit the `CLOSING_DATE` in `app.py`:
```python
CLOSING_DATE = datetime(2026, 4, 30)
```

## Vote Management

### Manual Vote Addition
The system is designed for manual vote verification. When someone sends proof of payment:

1. Verify the payment
2. Update the contestant's votes in `data/contestants.json`
3. The website will automatically display the updated count

### Automated Vote System (Optional Enhancement)
For automated vote processing, you would need to:
- Integrate with a payment gateway
- Add database support (e.g., SQLite, PostgreSQL)
- Implement admin panel for vote management
- Add authentication system

## Deployment

### Local Network (For Events)
- Run on a computer connected to local network
- Share the IP address with attendees
- They can access via their phones

### Online Hosting Options

1. **Heroku** (Free tier available):
   - Create Heroku account
   - Install Heroku CLI
   - Deploy with: `git push heroku main`

2. **PythonAnywhere** (Free tier available):
   - Upload files via web interface
   - Configure web app in dashboard

3. **DigitalOcean/Linode** (Paid):
   - More control and better performance
   - Requires server management knowledge

4. **Vercel/Netlify** (For static hosting):
   - Would require converting to static site
   - Or using serverless functions

## Security Notes

- The `SECRET_KEY` in app.py should be changed to a random string in production
- Consider adding rate limiting for vote submissions
- Implement HTTPS for payment information
- Add CAPTCHA for vote submission forms if making them automated
- Never commit sensitive data (like actual bank credentials) to version control

## Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers (iOS Safari, Chrome Mobile)

## Troubleshooting

### Images not showing:
- Check that images are in `static/images/`
- Verify filename matches `contestants.json`
- Check file permissions

### Port already in use:
- Change port in `app.py`: `app.run(port=5001)`
- Or kill the process using port 5000

### Votes not updating:
- Check that `data/contestants.json` is writable
- Verify JSON format is valid
- Restart the application

## Support

For questions or issues with the website:
- WhatsApp: 0673083980 / 0681019320
- Facebook: Miss Gorgeous Hearts Pretoria
- Instagram: @gorg.eousheartspretoria

## License

This is a custom website created for Miss Gorgeous Hearts Pretoria 2026.

## Credits

Website designed and developed for Miss Gorgeous Hearts PTA
Theme: Gold & Black Elegance
Tagline: "Real Queens Fix Each Other's Crowns"

---

**Good luck to all contestants! 👑**
