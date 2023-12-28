from service import app, db, csrf
from flask import render_template, request, jsonify, make_response, url_for, flash, redirect
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from service.forms import LoginForm
from service.model import User, Document, Article, BoxItem, Comment, UsefulData
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
        user = User.query.filter_by(email=form.email.data).first()
        print(user)
        if user:
            if flask_bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('admin_dashboard'))
        else:
            flash("Email ou mot de passe invalide")
    return render_template("pages/admin/login.html", form=form)

@app.route('/admin/register', methods=['POST'])
@csrf.exempt
def admin_register():
    if request.method == "POST":
        data = request.get_json()
        username = data['username']
        email = data['email']
        new_user = User(username=username, email=email, password=flask_bcrypt.generate_password_hash("password").decode('utf-8'))

        db.session.add(new_user)
        db.session.commit()
        
        return f'User {username} added to the database with hashed password!'
    
@login_required
@app.route('/admin/dashboard', methods=['GET', 'POST'])
def admin_dashboard():

    return render_template("pages/admin/dashboard.html", user=current_user.username)

@login_required
@app.route('/admin/mybox', methods=['GET', 'POST'])
def admin_mybox():
    boxes = BoxItem.query.all()
    return render_template("pages/admin/pages/mybox.html", user=current_user.username, data=boxes)


@login_required
@app.route('/admin/data', methods=['GET', 'POST'])
def admin_data():
    useful_data = UsefulData.query.all()
    return render_template("pages/admin/pages/data.html", user=current_user.username, data=useful_data)

@login_required
@app.route('/admin/articles', methods=['GET', 'POST'])
def admin_articles():
    articles = Article.query.all()
    return render_template("pages/admin/pages/articles.html", user=current_user.username, data=articles)

@login_required
@app.route('/admin/documents', methods=['GET', 'POST'])
def admin_documents():
    documents = Document.query.all()
    return render_template("pages/admin/pages/documents.html", user=current_user.username, data=documents)

@login_required
@app.route('/admin/users', methods=['GET', 'POST'])
def admin_users():
    users=User.query.all()
    return render_template("pages/admin/pages/users/index.html", user=current_user.username, data=users)


@login_required
@app.route('/admin/users/add', methods=['GET', 'POST'])
def admin_users_add():
    if request.method == "POST":
        data = request.form
        username = data['username']
        email = data['email']
        new_user = User(username=username, email=email, password=flask_bcrypt.generate_password_hash("password").decode('utf-8'))

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('admin_users'))
    return render_template("pages/admin/pages/users/new.html", user=current_user.username)

@login_required
@app.route('/admin/users/edit/<int:id>', methods=['GET', 'POST'])
def admin_users_edit(id):
    user = User.query.get(id)
    if request.method == "POST":
        data = request.form
        
        user.username = data['username']
        user.email = data['email']
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('admin_users'))

    return render_template("pages/admin/pages/users/edit.html", user=current_user.username, data=user)

@login_required
@app.route('/admin/users/delete/<int:id>', methods=['DELETE'])
def admin_users_delete(id):
    user = User.query.get(id)
    if request.form == "DELETE":
        user.delete()
        db.session.add(user)
        db.session.commit()

        return redirect(url_for="admin_users")