from requests import post,get

def cep_consulta(cep):
    req =get('https://viacep.com.br/ws/{}/json/'.format(cep))
    resultado = req.json()
    if "erro" in resultado:
        print("CEP inválido")
        exit()
    else:
        print(f'CEP: {resultado["cep"]}')
        print(f'Logradouro: {resultado["logradouro"]}')
        print(f'Complemento: {resultado["complemento"]}')
        print(f'Bairro: {resultado["bairro"]}')
        print(f'Localidade: {resultado["localidade"]}')
        print(f'Uf: {resultado["uf"]}')