from flask import Flask, render_template, redirect, url_for, flash
from forms import LoginForm, RegisterForm



app = Flask(__name__)
app.config['SECRET_KEY'] = 'wddwqidj qpwdijwqi jdwqidjwqidjwqidj'

@app.route('/',methods=['POST',"GET"])
def home():
    return render_template('index.html', title="Home", style='home.css')

@app.route("/about")
def about():
    return render_template('about.html',title="About" )

@app.route('/login', methods=['GET','POST'])
def login():
    obj = LoginForm()
    if obj.validate_on_submit(): 
        if obj.email.data == "dwd@gmail.com" and obj.password.data == "123456":
            flash('Logged In Successfully', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid Credentials', 'danger')

    return render_template('login.html',title='Login', form=obj)

@app.route('/register', methods=['GET','POST'])
def register():
    obj = RegisterForm()
    if obj.validate_on_submit():
        flash(f'Account created successfully {obj.username.data}', 'success')
        return redirect(url_for('home')) 
    return render_template('register.html',title='Signup', form=obj)

if __name__ =="__main__":
    app.run(debug=True, port=3000)