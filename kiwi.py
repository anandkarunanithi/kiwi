#!/usr/bin/env python

import os
import sys


if __name__ == "__main__":
    from argparse import ArgumentParser

    argparser = ArgumentParser()
    argparser.add_argument("--debug",
                            help="start the application in debug mode",
                            action="store_true")
    argparser.add_argument("--config",
                            dest="CONFIG",
                            help="path to the configuration file")
    argparser.add_argument("--logpath",
                            dest="LOGPATH",
                            help="directory path for the log files")
    args = argparser.parse_args()

    BASEDIR = os.path.dirname(os.path.abspath(__file__))

    CONFIG = os.path.join(BASEDIR, "kiwi.ini")
    if args.CONFIG:
        # checks whether the user provided configuration 
        # file path exists and has the extension of '.ini'   
        if args.CONFIG.endswith('.ini'):
            if os.path.isfile(os.path.abspath(args.CONFIG)):
                CONFIG = os.path.abspath(args.CONFIG)
            else:
                print "Configuration file %s does not exist" % os.path.abspath(args.CONFIG)
                sys.exit(1)
        else:
            print "Configuration file must be an INI file with extension .ini"
            sys.exit(1)

    LOGDIR = os.path.join(BASEDIR, "logs")
    if args.LOGPATH:
        LOGDIR = os.path.abspath(args.LOGPATH)
    
    if not os.path.isdir(LOGDIR):
        try:
            os.makedirs(os.path.abspath(LOGDIR), mode=0755)
        except:
            raise

    runtime_args = {
        "DEBUG": args.debug,
        "BASEDIR": BASEDIR,
        "CONFIG": CONFIG,  
        "LOGDIR": LOGDIR
    }

    from kiwi import server

    server.start(runtime_args)