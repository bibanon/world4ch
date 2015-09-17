from app import db

"""
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
"""

# table containing all thread information
class Threads(db.Model):
	threadid = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String)
	board = db.Column(db.String)
	firstposttime = db.Column(db.Integer)
	lastposttime = db.Column(db.Integer)
	lastbumptime = db.Column(db.Integer)
	numposts = db.Column(db.Integer)
	
	def __repr__(self):
		return '<Thread /%s/%s>' % (self.board, self.threadid)
	
"""
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
"""

# Posts per thread, relationally linked to Threads database
class Posts(db.Model):
	threadid = db.Column(db.Integer, db.ForeignKey('threads.threadid'), primary_key=True)
	postnum = db.Column(db.Integer, primary_key=True)
	postername = db.Column(db.String)
	postermeiru = db.Column(db.String)
	postertrip = db.Column(db.String)
	posterid = db.Column(db.String)
	posterdate = db.Column(db.Integer)
	post = db.Column(db.String)