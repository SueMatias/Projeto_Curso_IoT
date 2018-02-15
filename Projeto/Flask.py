from flask import Flask, render_template
app = Flask(__name__)
import Banco_de_Dados

@app.route("/Dados")
def sensores():
    valores = Banco_de_Dados.retorno_dados_sensores()
    return render_template("dados.html", valores=valores)

if __name__ == "__main__":
app.run(debug=True)
