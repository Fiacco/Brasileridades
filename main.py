import requests
from acesso_cep import BuscaEnderenco


cep = '01001000'
objeto_cep = BuscaEnderenco(cep)
print(objeto_cep)


#r = requests.get('https://viacep.com.br/ws/01001000/json/')
#print(r.text)

bairro,cidade,uf = objeto_cep.acessa_via_cep()

print(bairro, cidade, uf)
