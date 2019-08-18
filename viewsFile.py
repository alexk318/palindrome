from builtins import AttributeError

from flask import redirect, request, render_template, flash
from flask_login import current_user, login_user

from formsFile import regsforms, palnforms
from __init__ import app, user_datastore, db
from modelsFile import User, Palindrome


rus_words = []

with open('russian.txt') as f:
    rus_words = f.read().splitlines()


@app.route('/', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        if request.method == 'GET':
            scores = current_user.scores
            return render_template('game.html', palnforms=palnforms, scores=scores)

        if request.method == 'POST':
            palindrome = request.form['palindromeform'].lower()
            if palindrome in rus_words:  # Существует ли это слово
                if palindrome == palindrome[::-1]:  # Палиндром ли это
                    p = Palindrome.query.filter(Palindrome.title == palindrome).first()

                    try:
                        palindrome_users = p.users
                    except AttributeError:
                        new_palindrome = Palindrome(title=palindrome)
                        db.session.add(new_palindrome)
                        db.session.commit()

                        current_user.scores += len(palindrome)
                        new_palindrome.users.append(current_user)
                        db.session.commit()

                        flash('Успешно! Вам начислено {} очко(в)'.format(len(palindrome)))
                        return redirect('/')
                    else:
                        if current_user not in palindrome_users.all(): # Не повторяет ли пользователь этот палиндром
                            current_user.scores += len(palindrome)
                            palindrome_users.append(current_user)
                            db.session.commit()

                            flash('Успешно! Вам начислено {} очко(в)'.format(len(palindrome)))
                            return redirect('/')

                        else:
                            flash('Вы уже использовали это слово!')
                            return redirect('/')
                else:
                    flash('Введёное вами слово - не палиндром!')
                    return redirect('/')
            else:
                flash('Введённого слова не существует!')
                return redirect('/')

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