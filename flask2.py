from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/calculatrice')
def query():
    operation = request.args.get('operation')
    name = request.args.get('name')
    val1 = request.args.get('val1')
    val2 = request.args.get('val2')

    if name == None:
        return 'vous êtes un inconnu!!'

    if operation == None:
        return 'veuillez renseigner l opéraration!!'

    operations=['addition', 'soustraction', 'multiplication','division']
    resultat = ""
    if val1 == None or val2 ==None:
        return 'valeurs incorrectes!!'

    if operation == operations[0]:
        resultat =str(int(val1)+int(val2))

    if operation == operations[1]:
        resultat =str(int(val1)-int(val2))

    if operation == operations[2]:
        resultat =str(int(val1)*int(val2))

    if operation == operations[3]:
        resultat =int(val1)/int(val2)

    return '<h1>Hi {}. le résultat de l opération {} est {} </h1>'.format(name,operation,resultat)


if __name__=='__main__':
    app.run(host='0.0.0.0', port = 5000, debug =True)