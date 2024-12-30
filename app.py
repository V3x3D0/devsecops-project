from flask import Flask, request, render_template_string
app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("<h1>Welcome to My Vulnerable App</h1>")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template_string("""
            <form method="POST">
                <label for="username">Username:</label>
                <input type="text" name="username" required><br><br>
                <label for="password">Password:</label>
                <input type="password" name="password" required><br><br>
                <input type="submit" value="Login">
            </form>
        """)
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "admin" and password == "password":
            return "Login Successful"
        else:
            return "Invalid Credentials"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

