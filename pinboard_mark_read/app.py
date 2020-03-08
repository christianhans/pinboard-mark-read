import os
import sys
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
    if request.args.get('s') != os.environ.get('PINBOARD_MARK_READ_SECRET'):
        return ''
    url = request.args.get('url')
    if not url:
        return ''
    try:
        pb = Pinboard(os.environ.get('PINBOARD_TOKEN'))
        bookmark = pb.posts.get(url=url)['posts'][0]
        bookmark.toread = False
        bookmark.save()
    except:
        return ''
    return 'Success'