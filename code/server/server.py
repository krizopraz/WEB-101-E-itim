from flask import Flask, jsonify, request
app = Flask(__name__)

caylar = [
    {"cayAdi":"Siyah çay","fiyat":20,"cayID":"1"},
    {"cayAdi":"Yeşil çay","fiyat":20,"cayID":"2"},
]
@app.route('/cay')
def caylarGelsin():
    return jsonify(caylar)


@app.route('/cay', methods=['POST'])
def cayEkle():
    caylar.append(request.get_json())
    return jsonify(caylar)
@app.route('/cay', methods=['PUT'])
def cayiDegistir():
    cayID = request.args.get('cayID')
    cayAdi = request.args.get('cayAdi')
    fiyat = request.args.get('fiyat')

    cayIndex = findIndex(caylar,"cayID",cayID)
    if cayAdi != None:
        caylar[cayIndex]["cayAdi"] = cayAdi
    if fiyat != None:
        caylar[cayIndex]["fiyat"] = int(fiyat)
        print(caylar)
    return jsonify(caylar)

@app.route('/cay', methods=['DELETE'])
def caySil():
    cayID = request.args.get('cayID')
    cayIndex = findIndex(caylar,"cayID",cayID)
    caylar.pop(cayIndex)
    return jsonify(caylar)

def findIndex(dict,key,val):
    index = 0 
    for element in dict:
        if element[key] == val :
            break
        index += 1
    return index