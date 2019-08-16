from wtforms import Form, StringField, PasswordField


class RegistrationForms(Form):
    emailform = StringField('Email: ', render_kw={'required': True})
    passwordform = PasswordField('Password: ', render_kw={'required': True})

class PalindromeForms(Form):
    palindromeform = StringField(render_kw={'required': True})


regsforms = RegistrationForms()
palnforms = PalindromeForms()
