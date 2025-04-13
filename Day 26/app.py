from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Hello, Flask!</h1>
    <p><strong>Welcome</strong> to your first Flask app.</p>
    <ul>
        <li><a href='/about'>About</a></li>
        <li><a href='/contact'>Contact</a></li>
        <li><a href='/hello/yourname'>Say Hello</a></li>
    </ul>
    """

@app.route('/about')
def about():
    return """
    <h2>About Page</h2>
    <p>This is a <em>simple</em> about page built using Flask.</p>
    <ul>
        <li>Easy to use</li>
        <li>Lightweight</li>
        <li>Flexible</li>
    </ul>
    """

@app.route('/contact')
def contact():
    return """
    <h3>Contact Page</h3>
    <p><strong>Email us</strong> at: <a href='mailto:contact@example.com'>contact@example.com</a></p>
    <p>Or visit our <a href='/'>homepage</a>.</p>
    """

@app.route('/hello/<name>')
def hello(name):
    return f"""
    <h2>Hello, {name.title()}!</h2>
    <p>Welcome to our <strong>dynamic route</strong> example.</p>
    """

if __name__ == '__main__':
    app.run(debug=True)