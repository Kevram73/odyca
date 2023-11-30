from service import app, db
from flask import render_template, request, jsonify, make_response, url_for, flash, redirect
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from service.forms import LoginForm
from service.model import User
import flask_bcrypt

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

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        print(user)
        if user:
            if flask_bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('client_dashboard'))
        else:
            flash("Nom d'utilisateur ou mot de passe invalide")
    return render_template("pages/admin/login.html")

@login_required
@app.route('/admin/dashboard', methods=['GET', 'POST'])
def admin_dashboard():
    return render_template("pages/admin/dashboard.html")