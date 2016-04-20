import os, sys

PROJECT_DIR = '/var/nyt/de-github-webhooks/service/python-github-webhooks'

activate_this = os.path.join(PROJECT_DIR, 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))
sys.path.append(PROJECT_DIR)

from webhooks import app as application