str_uf        = 'Alagoas;Bahia;Ceará;Maranhão;Paraíba;Pernambuco;Piauí;Rio Grande do Norte;Sergipe'
str_siglas    = 'AL;BA;CE;MA;PB;PE;PI;RN;SE'
str_populacao = '3365351;14985284;9240580;7153262;4059905;9674793;3289290;3560903;2338474'

# Preencher as listas a partir das respectivas strings
# lst_uf        <- str_uf
# lst_siglas    <- str_siglas
# lst_populacao <- str_populacao (lembrar de converter para int)
lst_uf        = str_uf.split(";")
lst_populacao = str_populacao.split(";")
lst_siglas    = str_siglas.split(";")

maior_pop = -1
pos_maior = -1

for pos in range(len(lst_populacao)):
    pop_estado = int(lst_populacao[pos])
    if pop_estado > maior_pop:
        maior_pop = pop_estado
        pos_maior = pos
        
print ("O estado com maior população é:")
print (f"   {lst_uf[pos_maior]}({lst_siglas[pos_maior]})")
print (f"   População: {lst_populacao[pos_maior]}")
