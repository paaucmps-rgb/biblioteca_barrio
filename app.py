from flask import Flask, render_template, request, redirect, url_for
import catalogo
import socios

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', libros=catalogo.listar_libros(), socios=socios.listar_socios())

@app.route('/agregar', methods=['POST'])
def agregar():
    titulo = request.form.get('titulo')
    if titulo:
        catalogo.agregar_libro(titulo)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)