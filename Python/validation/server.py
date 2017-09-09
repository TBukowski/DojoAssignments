from flask import Flask, render_template, redirect, session, flash, request
from mysqlconnection import MySQLConnector
from datetime import datetime

app = Flask(__name__)
mysql = MySQLConnector(app,validation)