from flask import Flask, request, render_template_string
app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("<h1>Welcome to My Vulnerable App</h1>")

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == "admin" and password == "password":
        return "Login Successful"
    else:
        return "Invalid Credentials"

if __name__ == '__main__':
    app.run(debug=True)
