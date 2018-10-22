#!/usr/bin/env python

from configparser import ConfigParser, NoSectionError

defaults = {
    "kiwi": {
        "SECRET_KEY": "",
        "SERVER_HOST": "0.0.0.0",
        "SERVER_PORT": 8080,
        "CSRF_ENABLED": True,
        "CSRF_SESSION_KEY": "",
        "SERVER_THREADS": 10
    }
}

def reader(conf, section, key):
    # reads configuration from the config file, if either the required section or the key 
    # in the section is not present then the default value for the key is returned
    parser = ConfigParser()
    
    # preserve case of the keys
    parser.optionxform = str
    try:
        parser.read(conf)
        options = parser.options(section)
        print options
        if key in options:
            return parser.get(section, key)
        else:
            try:
                return defaults[section][key]
            except KeyError:
                raise
    except NoSectionError:
        return defaults[section][key]