from api import cep_consulta

cep_entrada = input("Digite o CEP: ")
resultado = cep_consulta(cep_entrada)
print(resultado)