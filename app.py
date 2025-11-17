from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    error = None

    nota1 = nota2 = nota3 = asistencia = ''

    if request.method == 'POST':
        nota1 = request.form.get('nota1', '')
        nota2 = request.form.get('nota2', '')
        nota3 = request.form.get('nota3', '')
        asistencia = request.form.get('asistencia', '')

        if not nota1 or not nota2 or not nota3 or not asistencia:
            error = "Debes completar todas las cajas de texto."
        else:
            try:
                n1 = float(nota1)
                n2 = float(nota2)
                n3 = float(nota3)
                asis = float(asistencia)
            except ValueError:
                error = "Debes ingresar solo números en las notas y la asistencia."
            else:
                if not (10 <= n1 <= 70 and 10 <= n2 <= 70 and 10 <= n3 <= 70):
                    error = "Las notas deben estar entre 10 y 70."
                elif not (0 <= asis <= 100):
                    error = "La asistencia debe estar entre 0 y 100."
                else:
                    promedio = round((n1 + n2 + n3) / 3, 2)
                    estado = "APROBADO" if promedio >= 40 and asis >= 75 else "REPROBADO"

                    resultado = {
                        'promedio': promedio,
                        'asistencia': asis,
                        'estado': estado
                    }

    return render_template(
        'ejercicio1.html',
        resultado=resultado,
        error=error,
        nota1=nota1,
        nota2=nota2,
        nota3=nota3,
        asistencia=asistencia
    )


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None
    error = None

    nombre1 = nombre2 = nombre3 = ''

    if request.method == 'POST':
        nombre1 = request.form.get('nombre1', '').strip()
        nombre2 = request.form.get('nombre2', '').strip()
        nombre3 = request.form.get('nombre3', '').strip()

        if not nombre1 or not nombre2 or not nombre3:
            error = "Debes ingresar los tres nombres."
        else:
            nombres = [nombre1, nombre2, nombre3]
            nombre_largo = max(nombres, key=len)
            cantidad = len(nombre_largo)

            resultado = {
                'nombre': nombre_largo,
                'cantidad': cantidad
            }

    return render_template(
        'ejercicio2.html',
        resultado=resultado,
        error=error,
        nombre1=nombre1,
        nombre2=nombre2,
        nombre3=nombre3
    )


if __name__ == '__main__':
    app.run(debug=True)
