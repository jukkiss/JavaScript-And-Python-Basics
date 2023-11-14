from flask import Flask, jsonify

app = Flask(__name__)

def on_alkuluku(luku):
    if luku < 2:
        return False

    for x in range(2, luku):
        if luku % x == 0:
            return False

    return True

@app.route('/alkuluku/<int:luku>')
def tarkista_alkuluku(luku):
    tulos = on_alkuluku(luku)
    return jsonify({"Number": luku, "isPrime": tulos})

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
