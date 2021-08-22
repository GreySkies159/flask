from flask import Flask, render_template, request, session, redirect, url_for, g
import model

app = Flask(__name__)
app.secret_key = "n$653odjenSFol3mCkrjw5"

ID = '00000000'
user =model.check_users()

@app.before_request
def before_request():
    g.ID = None
    if 'ID' in session:
        g.ID = session['ID']


# homepage
@app.route('/', methods=['GET'])
def home():
    print('session ID       ', session['ID'], "Current ID  ", ID)
    if 'ID' in session:
        g.user=session['ID']
        fullname=model.full_name(str(g.user))
        message="You are logged in as " + fullname
        return render_template('examResults.html', message=message)
    return render_template('homepage.html', message='Login to page or sign up')
    
@app.route('/login', methods=['GET', 'POST'])    
def login():
     if request.method=='POST':
         session.pop('ID', None)
         areyouuser = request.form['ID']
         pwd = model.check_pw(areyouuser, request.form['password'])
         if pwd =="True":
             session['ID'] = request.form['ID']
             g.ID=session['ID']
             return redirect(url_for('home'))
         elif pwd =="ID not found":
             return render_template('login.html', message = "ID not found")
         elif pwd == "False":
             return render_template('login.html', message = "Wrong password")
         else:
             return render_template('login.html', message = "Something went wrong")
     return render_template('login.html', message = "Please log in")         
        
     


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        message = 'Please sign up'
        return render_template('signup.html', message = message)
    else:
        ID = request.form["ID"]
        password = request.form["password"]
        fullName = request.form["full_name"]
        if len(ID) == 8:
            message = model.signup(ID, password, fullName)
            return render_template('signup.html', message = message)
        else:
            message="ID must be 8 digits"
            return render_template('signup.html', message = message)


@app.route('/getsession')
def getsession():
    if 'ID' in session:
        return session['ID']
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('ID', None)
    return redirect(url_for('home'))

if __name__ =='__main__':
    app.run(port=7000, debug=True)
