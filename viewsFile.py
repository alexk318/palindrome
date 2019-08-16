from flask import redirect, request, render_template
from flask_login import current_user, login_user

from __init__ import app, user_datastore, db
from formsFile import regsforms, palnforms
from modelsFile import User


@app.route('/', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        if request.method == 'GET':
            return render_template('game.html', palnforms=palnforms)
        if request.method == 'POST':
            palindrome = request.form['palindromeform'].lower()

            if palindrome == palindrome[::-1]:
                current_user.scores += len(palindrome)

                return render
            else:
                notpalindrome = 'Введёное вами слово - не палиндром!'
                return render_template('game.html', palnforms=palnforms, notpalindrome=notpalindrome)

    else:
        return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html', regsforms=regsforms)
    if request.method == 'POST':
        email = request.form['emailform']
        password = request.form['passwordform']

        new_user = user_datastore.create_user(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        user = User.query.filter(User.email == email).first()

        login_user(user, remember=True)

        return redirect('/')