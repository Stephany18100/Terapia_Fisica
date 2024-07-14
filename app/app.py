from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # return "Hola mundo!"
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

# hola
if __name__ =='__main__' : 
    app.run(debug=True, port=5000)
