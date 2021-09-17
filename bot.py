import json
import requests

pesquisa_cep = input("digite um cep:")
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