from flask import Flask, request, redirect, render_template
import cgi
import os
import re

app = Flask(__name__)
app.config['DEBUG'] = True

signup_form = """
<!doctype html>
<html>
<head>
	<style>
		form {
				bacground-color: #eee;
                width: 150px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
   
    </style>
        }
</head>
<body>
	<h1>Signup</h1>
	<form method='POST' action='/validate-input'>
        <!-- Username -->
		<label for="u-name" style="display:inline;">Username</label>
		<input id="u-name"  name="uname" type="text" autofocus/>
        <!-- Password -->
		<label for="p-word" class="inlne">Password</label>
		<input id="p-word" name="pword" type="password" />
        
        <!-- Password Verify -->
		<label for="v-pword" class="inlne">Verify Password</label>
		<input id="v-pword" name="v_pword" type="password" />
        
        <!-- E-mail -->
		<label for="e-mail" class="inlne">Email (optional)</label>
		<input id="e-mail" name="email" type="text" />
        
		<input type="submit" value="Submit" />
	</form>	
</body>
</html>
	"""

@app.route("/")
def index():
	return signup_form

@app.route('/validate-input')
def display_valid_form():
	return form.format('input_form.html', uname='', pword='', v_pword='', email='')

@app.route('/validate-input', methods=['POST'])
def validate_info():
    uname = request.form['uname']
    print(len(uname))
    pword = request.form['pword']
    v_pword = request.form['v_pword']
    email = request.form['email']

    uname_error = ''
    pword_error = ''
    v_pword_error = ''
    email_error = ''

    if uname == '':
        uname_error = 'Please enter a Username'
        uname = ''
    if uname.isalpha() == False:
        uname_error = 'Username is charcters only'
        uname = ''
    else:
        if len(uname) > 20 or len(uname) < 3:
            uname_error = 'Username length out of range (3 to 20)'
            uname = ''
   
    if pword == '':
        pword_error = 'Please enter a password (3 to 20 charcters only)'
        pword = ''
   
    if v_pword == '':
        v_pword_error = 'Please verify your password'
        v_pword = ''
    else:
    	v_pword = v_pword
    	if v_pword != pword:
    	   v_pword_error = 'Password does not match, please re-enter both'
    	   pword = ''
    	   v_pword = ''

    pattern = re.compile("^[?A-Z0-9._%+-]+@[?A-Z0-9.-]+\.[?A-Z]{3}$")
    print(pattern)
    print(email)
    if pattern.match(email):
        email_error = 'Email isn\'t properly formatted (alphanumeric@alpha.abc)'


    if not uname_error and not pword_error and not v_pword_error and not email_error:
        return render_template('welcome.html', user=uname)
    else:
        return render_template('input_form.html', uname_error = uname_error, pword_error = pword_error, 
            v_pword_error = v_pword_error, email_error = email_error)


app.run()