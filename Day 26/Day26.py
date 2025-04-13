# Day 26: Introduction to flask/django

# this example user flask to demonstrate a basic web apps
# make sure flask is installed : pip install flask

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, Flask!</h1><p>Welcome to your first Flask app.</p>"

@app.route('/about')
def about():
    return "<h2>About Page</h2><p>This is a simple about page.</p>"

@app.route('/contact')
def contact():
    return "<h3>Contact Page</h3><p>Email us at contact@example.com</p>"

@app.route('/hello/<name>')
def hello(name):
    return f"<h2>Hello, {name.title()}!</h2><p>Welcome to our website.</p>"

if __name__ == '__main__':
    app.run(debug=True)


# To run this:
# 1. Save this code in a file, e.g., app.py
# 2. Open terminal and run: python app.py
# 3. Visit http://127.0.0.1:5000 in your browser

# Exercises:
# 1. Add a new route `/contact` that returns a contact message.
# 2. Create a dynamic route `/hello/<name>` that greets the user by name.
# 3. Try modifying the HTML returned to include basic formatting.
