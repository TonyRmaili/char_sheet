from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def submit_form():
    result = None
    username = request.form.get('username')
    password = request.form.get('password')
    action = request.form.get('action')

    if action == 'login':
        # Handle login logic
        result = f'Logged in as {username}'
    elif action == 'register':
        # Handle registration logic
        result = f'Registered as {username}'
    elif action == 'reset_password':
        # Handle password reset logic
        result = f'Password reset requested for {username}'
    
    # Render the template with the updated data
    return render_template('form.html', username=username, password=password, action=action, result=result)

if __name__ == '__main__':
    app.run(debug=True)
