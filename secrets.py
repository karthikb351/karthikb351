# Copy this file into secrets.py and set keys, secrets and scopes.

# This is a session secret key used by webapp2 framework.
# Get 'a random and long string' from here: 
# http://clsc.net/tools/random-string-generator.php
# or execute this from a python shell: import os; os.urandom(64)
SESSION_KEY = "a very long and secret session key goes here"
# Google APIs
GOOGLE_APP_ID = '498750378391-v71rsa7or67aenvj73711qr2iveq9d5k.apps.googleusercontent.com'
GOOGLE_APP_SECRET = 'tEQCCsNI0PcLlwIHkdv4pAbc'
# config that summarizes the above
AUTH_CONFIG = {
# OAuth 2.0 providers
'google': (GOOGLE_APP_ID, GOOGLE_APP_SECRET,
'https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email')
}