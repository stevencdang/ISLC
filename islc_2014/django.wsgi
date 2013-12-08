import os
import sys
import site

#Add virtual environment
site.addsitedir('/var/venv/main_site/lib/python2.7/site-packages')

# activate_this = '/web/venv/main_site/bin/activate_this.py')
# execfile(activate_this, dict(__file__=activate_this)

# Configure PYTHONPATH
paths = ["/var/web/ISLC/islc_2014",
]
for path in paths:
    if path not in sys.path:
	    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'islc_2014.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
