# routes.py

from flask import render_template, request, redirect, url_for
from . import app, db
from .forms import ContactForm
from .models import ContactMessage

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        new_message = ContactMessage(name=name, email=email, message=message)
        db.session.add(new_message)
        db.session.commit()
        return redirect(url_for('contact_success'))
    return render_template('contact.html', form=form)

@app.route('/contact/success')
def contact_success():
    return render_template('contact_success.html')
