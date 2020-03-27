from flask import Flask, escape, request, render_template, redirect
import json


app = Flask(__name__)


empleados = []

def guardar_datos():
    json_data = json.dumps(empleados)
    f = open('db_empleados.json', 'w')
    f.write(json_data)
    f.close()

def recuperar_datos():
    try:
        f = open('db_empleados.json', 'r')
        json_data = f.read()
        data = json.loads(json_data)
        f.close()
        return data
    except:
        pass



@app.route('/')
def home():
    return render_template('Index.html', lista_empleados=empleados)


@app.route('/agregar', methods=['GET', 'POST'])
def agregar_empleado():
    if request.method == 'POST':
        emp = {
            'nombre': request.form['nombre'],
            'apellido': request.form['apellido'],
            'cargo': request.form['puesto'],
            'sueldo': request.form['sueldo']
        }
        empleados.append(emp)
        guardar_datos()
        return redirect('/')

    return render_template('Add.html')


@app.route('/eliminar/<int:codigo>', methods=['GET', 'POST'])
def eliminar_empleado(codigo):
    if request.method == 'POST':
        del empleados[codigo]
        guardar_datos()
        return redirect('/')

    return render_template('Remove.html', emp=empleados[codigo])


@app.route('/editar/<int:codigo>', methods=['GET', 'POST'])
def editar_empleado(codigo):
    if request.method == 'POST':
        emp = {
            'nombre': request.form['nombre'],
            'apellido': request.form['apellido'],
            'cargo': request.form['puesto'],
            'sueldo': request.form['sueldo']
        }
        
        empleados[codigo] = emp
        guardar_datos()
        return redirect('/')
    
    return render_template('Edit.html', empleado=empleados[codigo])



if __name__ == '__main__':
    empleados = recuperar_datos()
    app.run(host='0.0.0.0')