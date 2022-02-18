# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 22:22:54 2022

@author: alomo
"""

from flask import Flask, request

app = Flask(__name__)

@app.route('/hello_canada')
def hello():
    return "Hello Israel"

'''http://127.0.0.1:5000/add?a=3&b=5'''
@app.route('/add',methods=['GET'])
def add_GET():
    a = request.args.get('a')
    b= request.args.get('b')
    return str(int (a) + int (b))


@app.route('/add', methods=['POST'])
def add_POST():
    data = request.get_json()
    a = data['a']
    b= data['b']
    return str(int (a) + int (b))

app.run()