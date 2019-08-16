from __init__ import app

app.config['SECRET_KEY'] = 'secret_key'


app.config['SECURITY_PASSWORD_SALT'] = 'egor-loh'
app.config['SECURITY_PASSWORD_HASH'] = 'sha512_crypt'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:microlabm666@localhost/palindrome'
