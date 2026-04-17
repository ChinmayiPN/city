from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for signup page
@app.route('/')
def signup():
    return render_template('signup.html')


# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    password = request.form.get('password')
    email = request.form.get('email')
    phone = request.form.get('phone')

    # For now we just print (you can replace with DB later)
    print("User Details:")
    print("Name:", name)
    print("Password:", password)
    print("Email:", email)
    print("Phone:", phone)

    # Redirect to dashboard
    return redirect(url_for('dashboard', username=name))


# Dashboard route
@app.route('/dashboard')
def dashboard():
    username = request.args.get('username')
    return render_template('dashboard.html', name=username)

# Logout route
@app.route('/logout')
def logout():
    return redirect(url_for('signup'))

# Run the app
if __name__ == '__main__':
    app.run(debug=True)