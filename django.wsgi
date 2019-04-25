import os, sys
from app import socketio, app

sys.path.insert(0, '/home/sites/web/matcha.vuetube.top/public_html')
socketio.run(app, host="0.0.0.0")
