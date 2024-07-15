from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fichaIdentificacion')
def fichaIdentificacion():
    return render_template('FichaIdentificacio.html')

@app.route('/MiemInferior')
def MiemInferior():
    return render_template('ExploracionFisicaMiemInferior.html')

@app.route('/MiemSuperior')
def MiemSuperior():
    return render_template('ExploracionFisicaMiemSuper.html')

@app.route('/CabezayTorax')
def CabezayTorax():
    return render_template('ExploracionFisicaCabezaYtorax.html')

@app.route('/PersoNoPatologicos')
def PersoNoPatologicos():
    return render_template('AtecedentesPersonalesNoPatologicos.html')

@app.route('/AnteGinecobstetricos')
def AnteGinecobstetricos():
    return render_template('AnteGinecobstetricos.html')

@app.route('/PersoPatologicos')
def PersoPatologicos():
    return render_template('AntecedentesPersonalesPatologicos.html')

@app.route('/PadecimientoActual')
def PadecimientoActual():
    return render_template('AntecedentesPadecimientoActual.html')

@app.route('/HeredoFam')
def HeredoFam():
    return render_template('AntecedentesHeredofamiliares.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
