from flask import Flask, render_template, request
from dice import Dice

# http://192.168.1.116:5000
app = Flask(__name__)

user_input_data = []  # List to store user input data

@app.route('/', methods=['GET', 'POST'])
def home():
    user_input = None

    if request.method == 'POST':
        user_input = request.form['user_input']

    return render_template('index.html', user_input=user_input)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
    
