# Import the app variable from the init
from chicodes_blog_app import app

# Import specific packages from flask
from flask import render_template,request

# Import Our Form(s)
from chicodes_blog_app.forms import UserInfoForm

# Default Home Route
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/test')
def testRoute():
    names = ['Robert','David','Bill','Jessy']
    return render_template('test.html',list_names = names)

# GET == Gathering Info
# POST == Sending Info
@app.route('/register', methods = ['GET','POST'])
def register():
    # Init our Form
    form = UserInfoForm()
    # Validation of our form
    if request.method == 'POST' and form.validate():
        # Get Information from the form
        username = form.username.data
        email = form.email.data
        password = form.password.data
        #print the data to the server that comes from the form
        print(username,email,password)

    return render_template('register.html',user_form = form)

