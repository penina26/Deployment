from flask import Flask,render_template, redirect, url_for,request,flash,get_flashed_messages,abort
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_ckeditor import CKEditor, CKEditorField
from wtforms import StringField, SubmitField, FileField
from wtforms.fields.simple import EmailField, PasswordField
from wtforms.validators import DataRequired, URL,Email
import sqlite3
import pandas as pd
from flask_login import UserMixin,LoginManager,login_user,logout_user,current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)


#login_manager=LoginManager()
#login_manager.init_app(app)

#Login manager

#create connection
conn = sqlite3.connect('restaurant_recommender.db')
cursor = conn.cursor()


#User table


#read from db table
df = pd.read_sql("SELECT * FROM restaurants", conn)
df['restaurant'] = df['name']

def default_recommendations(df):
    random_samples = df.sample(n = 10, replace = True)
    return random_samples

#add review and rating form


#Registration form
class RegisterNewUserForm(FlaskForm):
    name=StringField('Name',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField("Register")

#Login form
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@app.route('/',methods = ["GET", "POST"])
def home():
    return render_template("index.html", recomms = default_recommendations(df))

@app.route('/login',methods=['POST','GET'])
def login():
    form = LoginForm()
    if request.method =='POST':
        username = request.form.get('Username')
        password = request.form.get('Password')
    return render_template('login.html',form = form)

@app.route('/register',methods=['POST','GET'])
def register():
    form = RegisterNewUserForm()
    if request.method =='POST':
        username = request.form.get('Name')
        password = request.form.get('Password')
    return render_template('register.html', form = form)

@app.route('/view-restaurant/<int:rest_id>',methods=['GET','POST'])
def view_restaurant(rest_id):
    rest_index = rest_id
    for index, row in df.iterrows():
        if index == rest_index:
            name = df.at[index, 'restaurant']
            image = df.at[index, 'image']
            rating = df.at[index, 'rating']
            reviews = df.at[index, 'reviews']
            pricing = df.at[index, 'pricing']
            location = df.at[index, 'location']
            cuisine = df.at[index, 'cuisine']
    return render_template('restaurant.html', image = image,name = name, rating = rating, reviews = reviews, pricing = pricing, location = location, cuisine = cuisine)


if __name__ == "__main__":
    app.run(debug=True)



