from flask import Flask, render_template

app = Flask(__name__)

# Route for the Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the Privacy Policy Page
@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

# Route for the Terms of Service Page
@app.route('/terms')
def terms():
    return render_template('terms.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)