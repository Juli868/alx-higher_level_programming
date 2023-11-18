#!/usr/bin/python3
import MySQLdb as db
conn = db.connect( host='localhost', user='root', password='root', database='hbtn_0e_0_usa')
cursor = conn.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa')
