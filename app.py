import time
import redis
import requests
import datetime
import hashlib
import sys

from flask import Flask,jsonify,json,send_file,request

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
   return 'Hola estas en el Home'

@app.route('/searchComics/',methods = ['GET'])
def searchcomics():
    name = request.args.get('name',default=None)
    pagination  = request.args.get('pagination',default=1)
    comic  = request.args.get('comic',default=2)

    datetoday = datetime.datetime.now()
    datestr=str(datetoday)
    publickey='190ba0e94cb7d968b76a6b03e482a2b2'
    privatekey='321192e08efdc820c84cef3b246cda1c844decc3'
    combine=datestr+privatekey+publickey
    hash=hashlib.md5(combine.encode())
    hashstr=str(hash.hexdigest())
    pagination=int(pagination)
    if pagination > 1:
             offset= pagination * 100
             offsett=str(offset)
             if name == None:
                url='https://gateway.marvel.com:443/v1/public/characters?orderBy=name&limit=100&offset='+offsett+'&ts='+datestr+'&apikey='+publickey+'&hash='+hashstr
                response = requests.get(url)
                json_data = response.json()
                caracter_list = []
                datos=json_data['data']['results']
                for caracter in datos:
                    caracter_details = {"id":None,"name":None,"image":None,"appareances":None}
                    caracter_details['id'] = caracter['id']
                    caracter_details['name'] = caracter['name']
                    caracter_details['image'] = caracter['thumbnail']['path']+'.jpg'
                    caracter_details['appareances'] =  caracter['comics']['available']
                    caracter_list.append(caracter_details)

                return jsonify({'name':caracter_list})
             else:
                 name=str(name)
                 url='https://gateway.marvel.com:443/v1/public/characters?name='+name+'&orderBy=name&limit=100&&ts='+datestr+'&apikey='+publickey+'&hash='+hashstr
                 response = requests.get(url)
                 json_data = response.json()
                 caracter_list = []
                 datos=json_data['data']['results']
                 for caracter in datos:
                    caracter_details = {"id":None,"name":None,"image":None,"appareances":None}
                    caracter_details['id'] = caracter['id']
                    caracter_details['name'] = caracter['name']
                    caracter_details['image'] = caracter['thumbnail']['path']+'.jpg'
                    caracter_details['appareances'] =  caracter['comics']['available']
                    caracter_list.append(caracter_details)

                 return jsonify({'name':caracter_list})
            
    else:
            if comic != None:
                comic=str(comic)
                url='https://gateway.marvel.com:443/v1/public/comics?title='+comic+'&orderBy=title&limit=100&ts='+datestr+'&apikey='+publickey+'&hash='+hashstr
                response = requests.get(url)
                json_data = response.json()
                caracter_list = []
                datos=json_data['data']['results']
                for caracter in datos:
                    caracter_details = {"title":None,"id":None,"image":None,"onsaleDate":None}
                    caracter_details['id'] = caracter['id']
                    caracter_details['title'] = caracter['title']
                    caracter_details['image'] = caracter['thumbnail']['path']+'.jpg'
                    caracter_details['onsaleDate'] = caracter['dates'][0]['date']
                    caracter_list.append(caracter_details)
                return jsonify({'name':caracter_list})
            if name == None:
                url='https://gateway.marvel.com:443/v1/public/characters?orderBy=name&limit=100&ts='+datestr+'&apikey='+publickey+'&hash='+hashstr
                response = requests.get(url)
                json_data = response.json()
                caracter_list = []
                datos=json_data['data']['results']
                for caracter in datos:
                    caracter_details = {"id":None,"name":None,"image":None,"appareances":None}
                    caracter_details['id'] = caracter['id']
                    caracter_details['name'] = caracter['name']
                    caracter_details['image'] = caracter['thumbnail']['path']+'.jpg'
                    caracter_details['appareances'] =  caracter['comics']['available']
                    caracter_list.append(caracter_details)
                return jsonify({'name':caracter_list})
            else:
                name=str(name)
                url='https://gateway.marvel.com:443/v1/public/characters?name='+name+'&orderBy=name&limit=100&ts='+datestr+'&apikey='+publickey+'&hash='+hashstr
                response = requests.get(url)
                json_data = response.json()
                caracter_list = []
                datos=json_data['data']['results']
                for caracter in datos:
                    caracter_details = {"id":None,"name":None,"image":None,"appareances":None}
                    caracter_details['id'] = caracter['id']
                    caracter_details['name'] = caracter['name']
                    caracter_details['image'] = caracter['thumbnail']['path']+'.jpg'
                    caracter_details['appareances'] =  caracter['comics']['available']
                    caracter_list.append(caracter_details)

                return jsonify({'name':caracter_list})