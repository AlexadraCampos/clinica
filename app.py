from flask import Flask, render_template
from flask_cors import CORS # 📌 Importando Flask-CORS

app = Flask(__name__)

app.config.update(
    SESSION_COOKIE_SAMESITE='None',  # Permite cookies de terceiros
    SESSION_COOKIE_SECURE=True  
)

# 🔹 Configurar CORS para permitir requisições do frontend
CORS(app, origins=["https://ecommercemodelosite-7tztgdygq-alexandras-projects-d68fae16.vercel.app"])


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

# Função compatível com Vercel
def handler(request, *args, **kwargs):
    return app(request.environ, *args, **kwargs)  # Essa linha permite que o Flask funcione no Vercel

# Para evitar app.run(), que não é necessário no Vercel
# O Vercel já gerencia a execução do Flask por trás
if __name__ == "__main__":
    app.run(debug=True)  # Remover se rodar no Vercel, mas pode ficar no local para desenvolvimento local
