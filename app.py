from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')


if __name__ == '__main__':
    app.run(debug=True, port = 1111)