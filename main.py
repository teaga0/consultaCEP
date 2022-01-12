
import os


os.system('clear') or None
os.system('pip install requests') or None
os.system('pip install json') or None
os.system('clear') or None

import json
import requests
import time
txt = """
╔════╦╗░╔╗░░░╔═══╗░░░░░░░░░░ ╔╗╔╗
║╔╗╔╗║║░║║░░░║╔═╗║░░░░░░░░░░░║╠╝╚╗
╚╝║║╚╣╚═╝╠═══╣║░╚╬══╦═╗╔══╦╗╔╣╠╗╔╬══╗
░░║║░║╔═╗╠══║║║░╔╣╔╗║╔╗╣══╣║║║║║║║╔╗║
░░║║░║║░║║║══╣╚═╝║╚╝║║║╠══║╚╝║╚╣╚╣╔╗║
░░╚╝ ╚╝░╚╩═══╩═══╩══╩╝╚╩══╩══╩═╩═╩╝╚╝

"""
print(txt)
pesquisa_cep = input("digite um cep:")

os.system('clear') or None

dados = requests.get("https://cep.awesomeapi.com.br/json/{}".format(pesquisa_cep))
dados = dados.json()
cep = dados['cep']
rua = dados['address_name']
estado = dados['state']
bairro = dados['district']
latitude = dados['lat']
longitude = dados['lng']
cidade = dados['city']
ibge = dados['city_ibge']
ddd = dados['ddd']
print("CEP:{}\nRua:{}\nEstado:{}\nBairro:{}\nLatitude:{}\nLongitude:{}\nCidade:{}\nIBGE:{}\nDDD:{}".format(cep, rua, estado, bairro, latitude, longitude, cidade, ibge, ddd))

inpu = input("\nRealizar nova consulta? [s][n]\n")
if inpu == 's':
  os.system('python bot.py') or None
elif inpu == 'n':
  varad = "Adeus em 3.."
  print(varad)
  time.sleep(1)
  varad = "Adeus em 32."
  print(varad)
  time.sleep(1)
  varad = "Adeus em 321"
  print(varad, 'fechando..')
  time.sleep(1)
  os.system('clear') or None
