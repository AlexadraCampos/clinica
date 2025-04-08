from flask import Flask, render_template

app = Flask(__name__)

app.config.update(
    SESSION_COOKIE_SAMESITE='None',  # Permite cookies de terceiros
    SESSION_COOKIE_SECURE=True  
)

@app.route('/')
@app.route('/quemsomos')
def quemsomos():
    return render_template("quemsomos.html")

@app.route('/tratamentos')
def tratamentos():
    return render_template("tratamentos.html")

@app.route('/antes-depois')
def antes_depois():
    return render_template("antesdepois.html")

@app.route('/novidades')
def novidades():
    return render_template("novidades.html")

@app.route('/agenda')
def agenda():
    return render_template("agenda.html")

if __name__ == "__main__":
    app.run(debug=True)  
