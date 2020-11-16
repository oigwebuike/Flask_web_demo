from flask import Flask, render_template, request
##from flask_caching import Cache
import model

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        username = request.form['username']
        password = request.form['password']
        db_password = model.check_pwd(username)
        if password == db_password:
            message = model.show_email(username)
            return render_template('about.html', message = message)
        else:
            error_message = 'Error: Please, enter right credentials'
            return render_template('index.html', message = error_message)


@app.route('/football', methods = ['GET'])
def football():
    return render_template('football.html')

@app.route('/about', methods = ['GET'])
def about():
    return render_template('about.html')

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'GET':
        message = 'Please sign up'
        return render_template('signup.html', message= message)
    else:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        message = model.signup('username', 'password', 'email')
        return render_template('signup.html', message= message)



if __name__ == '__main__':
    app.run(port=7000, debug=True)
