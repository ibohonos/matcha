import sys
activate_this = '/home/sites/web/matcha.vuetube.top/private/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))
sys.path.insert(0, '/home/sites/web/matcha.vuetube.top/public_html')
sys.path.insert(0, '/home/sites/web/matcha.vuetube.top/private/venv/lib/python3.6/site-packages')
from app import app as application
