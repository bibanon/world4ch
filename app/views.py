#!/usr/bin/python
# views.py - generates HTML pages using templates, databases, and logic
from flask import render_template
from app import app
import sqlite3
from collections import defaultdict

# connect to the database to store image metadata
db_fname = "db.sqlite"

# initialize thread list
conn = sqlite3.connect(db_fname)
c1 = conn.cursor()
c1.execute('SELECT * FROM threads ORDER BY lastbumptime DESC;')
thread_query = c1.fetchall()

# insert thread list into dictionary
threads = []
for row in thread_query:
	threads.append(
		{
			'threadid' : row[0],
			'title' : row[1],
			'board' : row[2],
			'firstposttime' : row[3],
			'lastposttime' : row[4],
			'lastbumptime' : row[5],
			'numposts' : row[6]
		}
	)

# index page, lists all threads in database
@app.route('/')
@app.route('/index')
def index():
	
	return render_template('index.html', board="sjis", title="Shift JIS Art", threads=threads)

# threads page, figure out which thread to display from URL
@app.route('/thread/<int:url_thread_id>')
def page(url_thread_id):
	# generate list of threads
	conn = sqlite3.connect(db_fname)
	c = conn.cursor()
	c.execute("""SELECT * FROM posts WHERE threadid = ? ORDER BY postnum""", [url_thread_id])
	posts_query = c.fetchall()
	
	# insert thread list into dictionary
	posts = []
	for row in posts_query:
		posts.append(
			{
				'threadid' : row[0],
				'postnum' : row[1],
				'postername' : row[2],
				'postermeiru' : row[3],
				'postertrip' : row[4],
				'posterid' : row[5],
				'posterdate' : row[6],
				'post' : row[7]
			}
		)
	
	return render_template('thread.html', board="sjis", title="Example Thread", posts=posts)

# Database Test page
@app.route('/test')
def test():
	return(str(Posts.query_all()))