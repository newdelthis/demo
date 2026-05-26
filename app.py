import os
from flask import Flask, redirect, url_for, session, jsonify
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Secret key for session management
app.secret_key = os.getenv("SECRET_KEY")

# OAuth setup
oauth = OAuth(app)

github = oauth.register(
    name='github',
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize',
    api_base_url='https://api.github.com/',
    client_kwargs={
        'scope': 'user:email'
    }
)

@app.route('/')
def index():
    return '''
        Welcome to the GitHub OAuth Demo!
        <br><br>
        <a href="/login">Login with GitHub</a>
    '''

@app.route('/login')
def login():
    redirect_uri = url_for('authorize', _external=True)
    return github.authorize_redirect(redirect_uri)

@app.route('/callback')
def authorize():
    # Get access token
    token = github.authorize_access_token()

    # Store token in session
    session['github_token'] = token

    # Fetch user info
    response = github.get('user')
    user_info = response.json()

    return jsonify(user_info)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)