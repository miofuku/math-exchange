# Used when testing all apps at once

import os

from mathexchange.settings import *
from mathexchange.accounts.settings import *
from mathexchange.emailer.settings import *
from mathexchange.forum.settings import *

INSTALLED_APPS = DEFAULT_APPS + FORUM_APPS + PAGEDOWN_APP + PLANET_APPS + ACCOUNTS_APPS + EMAILER_APP

TASK_RUNNER = 'block'

ROOT_URLCONF = 'mathexchange.server.urls'
