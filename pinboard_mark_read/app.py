import os
import hashlib
from urllib.parse import unquote
from pinboard import Pinboard
from flask import Flask, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["30 per day"]
)

@app.route('/')
def index():
    return ''

@app.route('/pb/mark/read')
def mark_as_read():
    h = request.args.get('h')
    url = unquote(request.args.get('url'))
    if not h or not url:
        return '<h1>Error</h1>'
    if not validate_secret(h, url):
        return '<h1>Error</h1>'
    try:
        pb = Pinboard(os.environ.get('PINBOARD_TOKEN'))
        bookmark = pb.posts.get(url=url)['posts'][0]
        bookmark.toread = False
        bookmark.save()
    except:
        return '<h1>Error</h1>'
    return '<h1>Successfully marked as read.</h1>'

def get_hash(s):
    return hashlib.sha256(s.encode()).hexdigest()[:32]

def validate_secret(hash, url):
    secret = os.environ.get('PINBOARD_MARK_READ_SECRET')
    expected_hash = get_hash('{}{}'.format(secret, url))
    return hash == expected_hash