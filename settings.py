#!/usr/bin/python
#-*- coding:utf-8 -*-

from pymongo import Connection
import logging.config

DEBUG = True

#database define
db = Connection().assessment
chermongapp = '/chermong/'

logging.config.fileConfig("./log/logging.conf")
log = logging.getLogger('server')
