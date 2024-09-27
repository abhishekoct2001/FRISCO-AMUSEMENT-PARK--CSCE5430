from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book_tickets', methods=['POST'])
def book_tickets():
    details = request.form['details']
    return redirect(url_for('home'))

@app.route('/register_for_events')
def register_for_events():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
