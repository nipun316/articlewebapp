from flask import Flask,render_template,url_for,request,redirect
import csv

app = Flask(__name__)


@app.route('/')
def hello():
	return render_template('createaccount.html')

@app.route('/<string:pagename>')
def pagename(pagename):
	return render_template(pagename)




usernames=[]

def writetofile(data):
	with open('database.csv',mode='a')as csvf:
		username=data["username"]
		password=data["password"]
		usernames.append(username)
		csv_writer=csv.writer(csvf,delimiter=",",quotechar=".",quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([username,password])



@app.route('/login',methods=['POST','GET'])
def login():
	if request.method=='POST':
		data=request.form.to_dict()
		if data["check"]==data["password"]:
			writetofile(data)
			return render_template('login.html')
		else:
			return render_template('createaccount.html')


def readthefile(info):
	with open('database.csv','rt')as csvf:
		csvreader=csv.reader(csvf,delimiter=",")
		for row in csvreader:
			for field in row:
				if field ==info["username"]:
					return True
					

		
							

@app.route('/checklogin',methods=['POST','GET'])
def getin():
	if request.method=='POST':
		info=request.form.to_dict()
		if (readthefile(info)):
			return render_template('home.html')
		else:
			return render_template('createagain.html')

articlenames=[]
articles=[]
themes=[]

def lifesaver(knowledge):
	articlenames.append(knowledge["articlename"])
	articles.append(knowledge["article"])
	themes.append(knowledge["theme"])
	
	






@app.route('/article',methods=['POST','GET'])
def article():
	if request.method=='POST':
		knowledge=request.form.to_dict()
		lifesaver(knowledge)
		return render_template('article.html',articlename=knowledge["articlename"],article=knowledge["article"],theme=knowledge["theme"])
	



def rep(report):
	with open('complain.txt',mode='a') as fir:
			username=report["reportuser"]
			complain=report["report"]
			file=fir.write(f'\n username:{username}\n report:{complain}')

@app.route('/report',methods=['POST','GET'])
def report():
	if request.method=='POST':
		report=request.form.to_dict()
		rep(report)
		return render_template('home.html')



def nipun(i):
	abc=articlenames.copy()
	xyz=articles.copy()
	mno=themes.copy()
	tot=len(abc)
	fin=tot-2+i
	print(mno)
	if fin>tot-1:
		fin=tot-1
	render_template('feed.html',articlename=abc[0],article=xyz[0],theme=mno[0])

	

		
@app.route('/valuer',methods=['POST','GET'])
def feed():
	i=0
	if request.method=='POST':
		val=request.form.to_dict()
		get=val["factor"]
		if get=="back":
			nipun(-1)
		else:
			nipun(+1)




app.run(debug=True)


