#!/usr/bin/env python2

import os.path
import json

config_file = "config.json"

if not os.path.isfile(config_file) :
    exit()

with open(config_file) as f:
    config = json.load(f)

for key in config:
    name = key.strip().upper()
    value = config[key]

    print '-D%s="\\"%s\\""' % (name, value),
