from flask import Blueprint, render_template, redirect, url_for, flash
from app.forms import EditProfileForm

# Создаем Blueprint
bp = Blueprint('main', __name__)

# Храним данные пользователя в памяти (в словаре)
user_data = {
    'username': 'testuser',
    'email': 'test@example.com',
    'password': 'password123'
}

# Корневой маршрут
@bp.route('/')
def index():
    return redirect(url_for('main.edit_profile'))

# Маршрут для редактирования профиля
@bp.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    form = EditProfileForm()

    # Заполняем форму текущими данными пользователя
    if form.is_submitted():
        if form.validate():
            # Обновляем данные пользователя
            user_data['username'] = form.username.data
            user_data['email'] = form.email.data
            user_data['password'] = form.password.data

            flash('Your changes have been saved.')
            return redirect(url_for('main.edit_profile'))

    # Предзаполняем форму текущими данными
    form.username.data = user_data['username']
    form.email.data = user_data['email']

    return render_template('edit_profile.html', title='Edit Profile', form=form)


