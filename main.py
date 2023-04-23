from datetime import datetime
from flask import Flask, render_template, redirect, url_for,request,flash,get_flashed_messages,abort
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.fields.simple import EmailField, PasswordField
from wtforms.validators import DataRequired, URL,Email
from flask_ckeditor import CKEditor, CKEditorField
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin,LoginManager,login_user,logout_user,current_user


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

login_manager=LoginManager()
# login_manager.init_app(app)
login_manager = LoginManager(app)
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

##add review
class CreatePostForm(FlaskForm):
    photo = FileField("Add image", validators=[DataRequired()])
    review = CKEditorField("Review", validators=[DataRequired()])
    rating = StringField("Rating out of 5", validators=[DataRequired()])
    submit = SubmitField("Submit")

#Register new user
class RegisterNewUserForm(FlaskForm):
    name=StringField('Name',validators=[DataRequired()])
    email=EmailField('E-mail Address',validators=[Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField("Register")

#Login existing user
class LoginForm(FlaskForm):
    email=EmailField('E-mail Address',validators=[Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField("Login")



@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register',methods=['GET','POST'])
def register():
    form=RegisterNewUserForm()
    if request.method=='POST':
        hashed_password=generate_password_hash(form.password.data,method='pbkdf2:sha256',salt_length=8)

        #if the user tries to register with an existing email
        if User.query.filter_by(email=request.form.get('email')).first():
            flash('The email you entered already exists.Login instead!')
            return redirect(url_for('login'))
        
        else:
            new_user=User(
            name=form.name.data, 
            email=form.email.data,
            password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return render_template('index.html',logged_in=current_user.is_authenticated)
    return render_template('register.html',form=form)


@app.route('/login',methods=['POST','GET'])
def login():
    form=LoginForm()
    if request.method =='POST':
        email=request.form.get('email')
        password=request.form.get('password')
        user_to_login=User.query.filter_by(email=email).first()
        print(user_to_login)

        #if the user's email is in the db
        if user_to_login:
            if check_password_hash(user_to_login.password,password) == True:
                #if the user's password matches that in the db
                login_user(user_to_login) 
                flash('You have succesfully been logged in!')
                return render_template('index.html',logged_in=current_user.is_authenticated)
            else:
                flash('Incorrect credentials! Try again.')
                return redirect(url_for('login'))


        #if the user's email does not exist in the db
        elif not user_to_login:
            flash('Sorry,the Email you entered does not exist.Try again.')
            return redirect(url_for('login'))

        else:
            flash('Incorrect credentials!Try again.')
            return redirect(url_for('login'))

    return render_template('login.html',form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))




@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/github")
def github():
    return render_template("contact.html")



if __name__ == "__main__":
    app.run(debug=True)


