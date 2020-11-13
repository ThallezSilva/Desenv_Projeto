from flask import Flask
from flask import render_template, request, url_for, redirect

app = Flask(__name__)

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/info")
def info():
    return render_template("info.html")
    
@app.route("/athleticopr")
def athleticopr():
    return render_template("athleticopr.html")

@app.route("/atleticogo")
def atleticogo():
    return render_template("atleticogo.html")

@app.route("/atleticomg")
def atleticomg():
    return render_template("atleticomg.html")

@app.route("/bahia")
def bahia():
    return render_template("bahia.html")

@app.route("/botafogo")
def botafogo():
    return render_template("botafogo.html")

@app.route("/bragantinosp")
def bragantinosp():
    return render_template("bragantinosp.html")

@app.route("/cearasc")
def cearasc():
    return render_template("cearasc.html")

@app.route("/corinthians")
def corinthians():
    return render_template("corinthians.html")

@app.route("/coritiba")
def coritiba():
    return render_template("coritiba.html")

@app.route("/flamengo")
def flamengo():
    return render_template("flamengo.html")

@app.route("/fluminense")
def fluminense():
    return render_template("fluminense.html")

@app.route("/fortaleza")
def fortaleza():
    return render_template("fortaleza.html")

@app.route("/goias")
def goias():
    return render_template("goias.html")

@app.route("/gremio")
def gremio():
    return render_template("gremio.html")

@app.route("/internacional")
def internacional():
    return render_template("internacional.html")

@app.route("/palmeiras")
def palmeiras():
    return render_template("palmeiras.html")

@app.route("/santos")
def santos():
    return render_template("santos.html")

@app.route("/saopaulo")
def saopaulo():
    return render_template("saopaulo.html")

@app.route("/sportrecife")
def sportrecife():
    return render_template("sportrecife.html")

@app.route("/vascodagama")
def vascodagama():
    return render_template("vascodagama.html")


app.run(debug=True)