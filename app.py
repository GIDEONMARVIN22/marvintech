from flask import Flask, render_template, request, flash, redirect, url_for, session
from functools import wraps
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'marvintech-secret-2026'

# ===== ADMIN CREDENTIALS =====
ADMIN_USERNAME = 'marvin'
ADMIN_PASSWORD = 'marvintech2026'

# ===== IN-MEMORY BOOKINGS STORE =====
bookings = []

SERVICES = [
    {"id": 1,  "icon": "💿", "title": "OS Installation",                    "desc": "Windows 10/11, Linux — clean, genuine, and fully activated. Fast and reliable setup on any machine.",                                                                          "price": "From KSh 500"},
    {"id": 2,  "icon": "📦", "title": "MS Office Installation",             "desc": "Genuine Microsoft Office installation — Word, Excel, PowerPoint, Outlook and more. All versions available.",                                                                    "price": "From KSh 300"},
    {"id": 3,  "icon": "⚙️", "title": "Software Installation & System Setup","desc": "Any software you need installed, configured, and ready to use. Full system setup from scratch.",                                                                               "price": "From KSh 200"},
    {"id": 4,  "icon": "🚀", "title": "Laptop & Desktop Optimization",       "desc": "Slow computer? We clean, tune, and optimize your machine to run like new. Virus removal included.",                                                                             "price": "From KSh 400"},
    {"id": 5,  "icon": "🔓", "title": "Password Unlocking",                  "desc": "Forgot your laptop or phone password? We safely unlock Windows, BIOS, and phone screen locks.",                                                                                "price": "From KSh 300"},
    {"id": 6,  "icon": "🛡️", "title": "Genuine & Safe Installation",         "desc": "All our installations are 100% genuine, licensed, and safe. No pirated or malware-infected software.",                                                                         "price": "Included"},
    {"id": 7,  "icon": "💾", "title": "Driver Installation",                 "desc": "Missing drivers causing issues? We install all necessary drivers — graphics, audio, network, and more.",                                                                        "price": "From KSh 200"},
    {"id": 8,  "icon": "🖥️", "title": "Hardware & Device Setup",             "desc": "Printers, external drives, routers, and peripherals — we set up and configure any device.",                                                                                    "price": "From KSh 300"},
    {"id": 9,  "icon": "🌐", "title": "Website Creation",                    "desc": "Professional websites for businesses, portfolios, schools, and shops. Built with modern HTML, CSS, JavaScript and Python. Mobile-friendly and fast.",                          "price": "From KSh 2,000"},
    {"id": 10, "icon": "🗄️", "title": "System Development",                  "desc": "Custom management systems for schools, businesses, shops, and more. Student records, inventory, billing, POS — built to fit your exact needs.",                               "price": "From KSh 3,000"},
]

# ===== AUTH DECORATOR =====
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('admin'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

# ===== PUBLIC ROUTES =====
@app.route('/')
def index():
    return render_template('index.html', services=SERVICES)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name    = request.form.get('name', '').strip()
        phone   = request.form.get('phone', '').strip()
        service = request.form.get('service', '').strip()
        message = request.form.get('message', '').strip()
        if name and phone:
            bookings.append({
                'id': len(bookings) + 1,
                'name': name,
                'phone': phone,
                'service': service or 'Not specified',
                'message': message,
                'date': datetime.now().strftime('%d %b %Y, %H:%M'),
                'status': 'New'
            })
            flash(f"Thanks {name}! We'll contact you on {phone} shortly.", 'success')
            return redirect(url_for('contact'))
        else:
            flash('Please fill in your name and phone number.', 'error')
    return render_template('contact.html', services=SERVICES)

# ===== ADMIN ROUTES =====
@app.route('/admin/login', methods=['GET', 'POST'])
def login():
    if session.get('admin'):
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin'] = True
            return redirect(url_for('dashboard'))
        flash('Invalid username or password.', 'error')
    return render_template('admin/login.html')

@app.route('/admin/logout')
def logout():
    session.pop('admin', None)
    return redirect(url_for('login'))

@app.route('/admin/dashboard')
@login_required
def dashboard():
    return render_template('admin/dashboard.html', bookings=bookings, total=len(bookings))

@app.route('/admin/booking/<int:booking_id>/status', methods=['POST'])
@login_required
def update_status(booking_id):
    status = request.form.get('status')
    for b in bookings:
        if b['id'] == booking_id:
            b['status'] = status
            break
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
