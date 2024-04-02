# app.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    projects_data = [
        {'title': 'Project 1', 'description': 'Description of Project 1'},
        {'title': 'Project 2', 'description': 'Description of Project 2'},
        # Add more projects as needed
    ]
    return render_template('projects2.html', projects=projects_data)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
