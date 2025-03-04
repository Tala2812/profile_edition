from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class EditProfileForm(FlaskForm):
    username = StringField('Имя пользователя',
                           validators=[DataRequired(message="Поле 'Имя пользователя' обязательно для заполнения.")])
    email = StringField('Почта', validators=[DataRequired(message="Поле 'Email' обязательно для заполнения."),
                                             Email(message="Введите корректный email.")])
    password = PasswordField('Пароль', validators=[DataRequired(message="Поле 'Пароль' обязательно для заполнения.")])
    password2 = PasswordField('Повторить пароль',
                              validators=[DataRequired(message="Поле 'Повторите пароль' обязательно для заполнения."),
                                          EqualTo('password', message="Пароли должны совпадать.")])
    submit = SubmitField('Сохранить изменения')


