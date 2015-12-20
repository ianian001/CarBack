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

@main.route("/post_account_list")
def post_account_list():
    return render_template('post_account_list.html')

@main.route("/add_account")
def add_account():
    return render_template('add_account.html')





