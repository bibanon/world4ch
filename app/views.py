#!/usr/bin/python
# views.py - generates HTML pages using templates, databases, and logic
from flask import render_template
from app import app

# index page, lists all threads in database
@app.route('/')
@app.route('/index')
def index():
	# generate this object using the SQL command:
	# SELECT * FROM threads ORDER BY lastbumptime DESC;
	threads = [	# example thread objects
		{
			'threadid' : 123456,
			'title': 'This thread is an example of the first thread.',
			'firstposttime' : '1993-01-01 00:00',
			'lastposttime': '1993-01-01 00:10',
			'numposts' : '2'
		},
		{
			'threadid' : 123457,
			'title': 'This thread is an example of the second thread.',
			'firstposttime' : '1993-01-01 12:00',
			'lastposttime': '1993-01-01 23:00',
			'numposts' : 21
		}
	]

	return render_template('index.html', board="sjis", title="Shift JIS Art", threads=threads)

# threads page
@app.route('/thread')
@app.route('/thread/123456')
@app.route('/thread/123457')
def threads():
	# generate this object using the SQL command:
	# SELECT * FROM posts WHERE threadid='<threadid>' ORDER BY postnum;
	posts = [	# example post objects
		{
			'postnum' : 1,
			'postername': 'Anonymous',
			'postertrip' : '',
			'posterdate': '1993-01-01 00:00',
			'post': 'Beautiful day in Portland!'
		},
		{
			'postnum' : 2,
			'postername': 'tanasinn',
			'postertrip' : '!h430d09s',
			'posterdate': '1993-01-01 00:10',
			'post': 'don\'t think, feel... </br></br> <strong>and you will be tanasinn</strong>'
		}
	]
	return render_template('thread.html', board="sjis", title="Example Thread", posts=posts)