from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Register')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Save the user's registration information
        # (omitted for brevity)
        return redirect(url_for('success'))
    return render_template('register.html', form=form)


@app.route('/success')
def success():
    return '<h2>Registration successful!</h2>'


if __name__ == '__main__':
    app.run(debug=True)

# The above example creates a simple Flask application that has one route, the index route. The index route will handle both GET and POST requests.
#
# FlaskForm is imported from the flask_wtf module and the StringField and SubmitField are imported from the wtforms module.
#
#                                                                                                                                                                                                                                                           In the MyForm class, the name field is created as a StringField with the label "Name" and a DataRequired validator is added to it. A submit button is created using the SubmitField class.
#
# In the index route, an instance of MyForm is created and passed to the template for rendering. When the form is submitted, it is validated using the validate_on_submit() method. If the form is valid, the name entered by the user is extracted from the form using `form
