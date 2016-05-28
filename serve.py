from flask import Flask, render_template, request
import convert
app = Flask(__name__)

@app.route('/')
@app.route('/main.html')
def mainPage():
	return render_template('main.html')


@app.route('/gif.html', methods=["POST"])
def serveGIF():
	try :
		gifname = convert.convert(request.form.getlist('url')[0])
	except IndexError as e :
		return render_template('gif.html', gif = None)
	else :
		return render_template('gif.html', gif = gifname)

@app.route('/gif.html')
def getGIF():
	return render_template('gif.html', gif = None)

@app.route('/three.html')
def three():
	return render_template('three.html')

@app.route('/prom.html')
def prom():
	return render_template('prom.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':

	app.run(host = '0.0.0.0', port = 8000, debug = False)

