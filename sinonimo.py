from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Diccionario de sinónimos de ejemplo
sinonimos = {
    "fácil": "sencillo",
    "morir": "fallecer",
    "rápido": "veloz",
    "grande": "enorme",
    "pequeño": "diminuto",
    "feliz": "contento",
    "triste": "afligido",
    "inteligente": "listo",
    "amable": "cortés",
    "enojado": "irritado",
    "hermoso": "bello",
    "feo": "desagradable",
    "limpio": "aseado",
    "sucio": "mugriento",
    "fuerte": "robusto",
    "débil": "frágil",
    "viejo": "anciano",
    "nuevo": "reciente",
    "alto": "elevado",
    "bajo": "chaparro",
    "rico": "adinerado",
    "pobre": "necesitado",
    "caliente": "ardiente",
    "frío": "helado",
    "duro": "rígido",
    "blando": "suave",
    "rápido": "expedito",
    "lento": "pausado",
    "oscuro": "tenebroso",
    "claro": "luminoso",
    "fácil": "simple",
    "difícil": "complicado",
    "gracioso": "divertido",
    "serio": "formal",
    "caro": "costoso",
    "barato": "económico",
    "seguro": "confiable",
    "peligroso": "arriesgado",
    "amplio": "espacioso",
    "estrecho": "angosto",
    "cerca": "próximo",
    "lejos": "distante",
    "vacío": "desocupado",
    "lleno": "completo",
    "delgado": "flaco",
    "gordo": "obeso",
    "bueno": "bondadoso",
    "malo": "malvado",
    "silencioso": "callado",
    "ruidoso": "estridente"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analizar', methods=['POST'])
def analizar():
    texto = request.json['texto']
    lineas = texto.split('\n')
    
    resultados = []
    for i, linea in enumerate(lineas):
        resultado = {"entrada": linea, "resultado": "", "palabras_cambiadas": "", "numeros": "", "simbolos": "", "linea": i + 1}
        
        palabras = linea.split()
        palabras_resultado = []
        palabras_cambiadas = []
        
        for palabra in palabras:
            texto = palabra.lower()
            if texto in sinonimos:
                palabras_resultado.append(sinonimos[texto])
                palabras_cambiadas.append(palabra)
            else:
                palabras_resultado.append(palabra)
        
        resultado["resultado"] = ' '.join(palabras_resultado)
        resultado["palabras_cambiadas"] = 'x' if palabras_cambiadas else ''
        resultado["numeros"] = 'x' if any(char.isdigit() for char in linea) else ''
        resultado["simbolos"] = 'x' if any(char in '.,;:()[]{}!?"' for char in linea) else ''
        
        resultados.append(resultado)
    
    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=True)