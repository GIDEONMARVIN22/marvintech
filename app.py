from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'marvintech-secret-2026'

SERVICES = [
    {
        "id": 1,
        "icon": "💿",
        "title": "OS Installation",
        "desc": "Windows 10/11, Linux — clean, genuine, and fully activated. Fast and reliable setup on any machine.",
        "price": "From KSh 500"
    },
    {
        "id": 2,
        "icon": "📦",
        "title": "MS Office Installation",
        "desc": "Genuine Microsoft Office installation — Word, Excel, PowerPoint, Outlook and more. All versions available.",
        "price": "From KSh 300"
    },
    {
        "id": 3,
        "icon": "⚙️",
        "title": "Software Installation & System Setup",
        "desc": "Any software you need installed, configured, and ready to use. Full system setup from scratch.",
        "price": "From KSh 200"
    },
    {
        "id": 4,
        "icon": "🚀",
        "title": "Laptop & Desktop Optimization",
        "desc": "Slow computer? We clean, tune, and optimize your machine to run like new. Virus removal included.",
        "price": "From KSh 400"
    },
    {
        "id": 5,
        "icon": "🔓",
        "title": "Password Unlocking",
        "desc": "Forgot your laptop or phone password? We safely unlock Windows, BIOS, and phone screen locks.",
        "price": "From KSh 300"
    },
    {
        "id": 6,
        "icon": "🛡️",
        "title": "Genuine & Safe Installation",
        "desc": "All our installations are 100% genuine, licensed, and safe. No pirated or malware-infected software.",
        "price": "Included"
    },
    {
        "id": 7,
        "icon": "💾",
        "title": "Driver Installation",
        "desc": "Missing drivers causing issues? We install all necessary drivers — graphics, audio, network, and more.",
        "price": "From KSh 200"
    },
    {
        "id": 8,
        "icon": "🖥️",
        "title": "Hardware & Device Setup",
        "desc": "Printers, external drives, routers, and peripherals — we set up and configure any device.",
        "price": "From KSh 300"
    },
    {
        "id": 9,
        "icon": "🌐",
        "title": "Website Creation",
        "desc": "Professional websites for businesses, portfolios, schools, and shops. Built with modern HTML, CSS, JavaScript and Python. Mobile-friendly and fast.",
        "price": "From KSh 2,000"
    },
    {
        "id": 10,
        "icon": "🗄️",
        "title": "System Development",
        "desc": "Custom management systems for schools, businesses, shops, and more. Student records, inventory, billing, POS — built to fit your exact needs.",
        "price": "From KSh 3,000"
    },
]

@app.route('/')
def index():
    return render_template('index.html', services=SERVICES)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        phone = request.form.get('phone', '').strip()
        service = request.form.get('service', '').strip()
        message = request.form.get('message', '').strip()
        if name and phone:
            flash(f"Thanks {name}! We'll contact you on {phone} shortly.", 'success')
            return redirect(url_for('contact'))
        else:
            flash('Please fill in your name and phone number.', 'error')
    return render_template('contact.html', services=SERVICES)

if __name__ == '__main__':
    app.run(debug=True)
