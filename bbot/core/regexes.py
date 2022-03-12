import re
from collections import OrderedDict

# for extracting words from strings
word_regexes = [re.compile(r, re.I) for r in [
    # alphanumeric, underscore
    r'[\w]+',
    # alphanumeric, underscore, dash
    r'[\w-]+',
    # alpha
    r'[a-z]{3,}',
    # alpha, dash
    r'[a-z]+[a-z-]+[a-z]+',
    # alpha, underscore
    r'[a-z]+[a-z_]+[a-z]+',
    # alpha, underscore, dash
    r'[a-z]+[a-z_-]+[a-z]+',
]]

event_type_regexes = OrderedDict([(k, re.compile(r, re.I)) for k, r in [
    ('EMAIL_ADDRESS', r'^([A-Z0-9][\w\-\.\+]{,100})@([A-Z0-9][\w\-\.]{,100})\.([A-Z]{2,8})$'),
    ('HOSTNAME', r'^(([A-Z0-9]|[A-Z0-9][A-Z0-9\-]*[A-Z0-9])\.)+([A-Z0-9]|[A-Z0-9][A-Z0-9\-]*[A-Z0-9])$'),
    ('OPEN_TCP_PORT', r'^(([A-Z0-9]|[A-Z0-9][A-Z0-9\-]*[A-Z0-9])\.)+([A-Z0-9][A-Z0-9\-]*[A-Z0-9]|[A-Z0-9]):[0-9]{1,5}$'),
    ('URL', r'^([A-Z]){2,}://(([A-Z0-9]|[A-Z0-9][A-Z0-9\-]*[A-Z0-9])\.)+([A-Z0-9][A-Z0-9\-]*[A-Z0-9]|[A-Z0-9])(:[0-9]{1,5}){0,1}.*$'),
    ('USERNAME', r'^[\w\-_]+$')
]])

event_id_regex = re.compile(r'[0-9a-f]{40}:[A-Z0-9_]+')