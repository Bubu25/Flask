from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#@app.route('/')
#def index():
    #return "Hello, World"

@app.route('/coucou')
def coucou():
    return "coucou salut!"

@app.route('/json')
def json():
    return jsonify({'key':'value','listkey':[1,2,3]})

@app.route('/valeur/<valeur1>')
def afficherValeur(valeur1):
    return str(valeur1)

@app.route('/somme/<valeur1>/<valeur2>')
def somme(valeur1,valeur2):
    resultat = int(valeur1)+int(valeur2)
    return str(resultat)

# @app.route('/home',defaults={'name':'defaults'})
# @app.route('/home/<string:name>')
# def home(name):
#     return'<h1>Hello {}, you are on the home page!</h1>'.format(name)

#from flask import Flask, jsonify, request
# on saisira qans l'explorateur http://localhost:5000/query?name=Pierre&location=Toulouse
@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return '<h1>Hi {}. You are from {}. You are on the query page!</h1>'.format(name,location)

@app.route('/theform')
def theform():
    return '''<form method="POST" action="/process">
                    Nom:
                    <input type="text" name="name">
                    Lieu:
                    <input type="text"  name="location">
                    <input type="submit" value="Envoyer">
                </form>'''
@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']

    return '<h1>Hello {}. You are from {}. you have submitted the form succesfully!<h1>'.format(name,location)

@app.route('/theform2', methods=['GET','POST'])
def theform2():

    if request.method =='GET':
        return '''<form method="POST" action="/theform2">
                        Nom:
                        <input type="text" name="name">
                        Lieu:
                        <input type="text"  name="location">
                        <input type="submit" value="Envoyer">
                    </form>'''
    else:
        name = request.form['name']
        location = request.form['location']

        return '<h1>Hello {}. You are from {}. you have submitted the form succesfully!</h1>'.format(name, location)

@app.route('/affiche_somme/<valeur1>/<valeur2>')
def affiche_somme(valeur1,valeur2):
    from datetime import date
    d = date.today().isoformat()
    resultat= int(valeur1)+int(valeur2)
    return render_template("somme.html", la_date=d, v1=valeur1, v2=valeur2, res=resultat)

@app.route('/home',methods=['POST','GET'], defaults={'name':'Default'})
@app.route('/home/<string:name>',methods=['POST','GET'])
def home(name):
    return render_template('home.html', name=name, display=False)

@app.route('/home2',methods=['POST','GET'], defaults={'name':'Default'})
@app.route('/home2/<string:name>',methods=['POST','GET'])
def home2(name):
    return render_template('home2.html', name=name, display=False,
                           mylist=['one','two','three','four'],
                           listofdictionnaries=[{'name':'Zach'},{'name':'Zoe'}])

if __name__=='__main__':
    app.run(host='0.0.0.0', port = 5000, debug =True)