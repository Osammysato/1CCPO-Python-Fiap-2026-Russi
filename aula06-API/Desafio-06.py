
endpoints = ["/login", "/produtos", "/pedidos"]
status = [
    [200, 200, 401, 200, 500],
    [200, 200, 200, 200, 200],
    [201, 500, 502, 201, 500]
]

# print(endpoints[1])
# print(status[2])

# Função que verifica se um codigo HTTP da REQ é sucesso ou não

def eh_sucesso(codigo):
    return codigo >= 200 and codigo <= 299

# print(sucesso(200))

# Função que verifica um EndPoint no Vetor

qtd_maior_erro = -1
endpoints_maior_erro = 0

def err_seguido(lista_req):
    for i in range(len(lista_req) -1):
        codigo_atual = lista_req[i]
        prox_codigo = lista_req[i + 1]

        if not eh_sucesso(codigo_atual) and not eh_sucesso(prox_codigo):
            return True
    return False


# print(err_seguido(status[0]))

def analisa_end(lista_req):
    qnt_sucesso = 0

    for codigo in lista_req:
        if eh_sucesso(codigo):
            qnt_sucesso += 1

    qtd_total_req = len(lista_req)
    qtn_erros = qtd_total_req - qnt_sucesso
    percentual_sucesso = (qnt_sucesso / qtd_total_req) * 100

    tem_erro_seguindo = err_seguido(lista_req)

    if tem_erro_seguindo:
        classificacao = 'Critico'
    elif percentual_sucesso > 80:
        classificacao = 'Estavel'
    else:
        classificacao = 'Instavel'

    return (qnt_sucesso, qtn_erros, percentual_sucesso, classificacao)


# Percorrer a Matriz

for i in range(len(endpoints)):
    nome_endpoint = endpoints[i]
    print(nome_endpoint)
    reqs_endpoints = status[i]

sucessos, erros, percentual, classificacao = analisa_end(reqs_endpoints)

print(f"Endpoint': {nome_endpoint}")
print(f"Status': {reqs_endpoints}")
print("-" * 30)
print()
print(f"Sucessos: {sucessos}")
print(f"Erros: {erros}")
print(f"Percentual: {percentual}")
print(f"Classificacao: {classificacao}")
print("-" * 30)
print()

if erros > qtd_maior_erro:
    qtd_maior_erro = erros
    endpoints_maior_erro = nome_endpoint

print(f"Endpoints maior erro: {endpoints_maior_erro}   ({qtd_maior_erro})")
