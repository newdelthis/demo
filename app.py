import os
from flask import Flask, redirect, url_for, session, request, jsonify
from flask_oauthlib.client import OAuth
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
oauth = OAuth(app)

# Configure GitHub OAuth2
github = oauth.remote_app(
    'github',
    consumer_key=os.getenv("CLIENT_ID"),
    consumer_secret=os.getenv("CLIENT_SECRET"),
    request_token_params={
        'scope': 'user:email',
    },
    base_url='https://api.github.com/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize'
)

@app.route('/')
def index():
    return 'Welcome to the GitHub OAuth Demo! <a href="/login">Login with GitHub</a>'

@app.route('/login')
def login():
    return github.authorize(callback=url_for('authorized', _external=True))

@app.route('/callback')
def authorized():
    response = github.authorized_response()
    if response is None or response.get('access_token') is None:
        return 'Access denied: reason={} error={}'.format(
            request.args['error_reason'],
            request.args['error_description']
        )

    session['github_token'] = (response['access_token'], '')
    user_info = github.get('user')
    return jsonify(user_info.data)

@github.tokengetter
def get_github_oauth_token():
    return session.get('github_token')

if __name__ == "__main__":
    app.run(debug=True)
