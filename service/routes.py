from service import app, db
from flask import render_template, request, jsonify, make_response, url_for, flash
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from service.model import User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/test", methods=['GET'])
def test():
    return jsonify({"message": "Hello World!"})

@app.route('/', methods=['GET'])
def home():
    return render_template('pages/home.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('pages/about.html')

@app.route('/services', methods=['GET'])
def services():
    return render_template("pages/services.html")

@app.route('/blog', methods=['GET'])
def blog():
    return render_template("pages/blog.html")

@app.route('/contact', methods=['GET'])
def contact():
    return render_template("pages/contact.html")