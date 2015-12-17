#coding:utf-8
from flask import Flask, url_for, redirect, flash, jsonify
from flask import request, make_response
from urllib import urlencode
from flask import render_template
from . import main
from models import db
from datetime import datetime, date, time
import string
import uuid
import requests
import simplejson
import hashlib
import json
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

@main.route('/')
def index():
    return render_template('index.html')





