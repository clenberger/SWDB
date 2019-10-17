from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    return 'Hello, welcome to SWDB!'

if __name__ == '__main__':
    app.run(debug=True)