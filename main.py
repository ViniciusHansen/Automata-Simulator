import afns


geral = afns.geral
manutencao = afns.manutencao
pagamento = afns.pagamento
existe_no_alfabeto = afns.existe_no_alfabeto
transicao_possivel = afns.transicao_possivel
evoluir = afns.evoluir
estado_atual = afns.estado_atual


automatos = [geral, manutencao, pagamento]

# Gerar Buffers
for i in range(20):
    automatos.append(afns.factory_buffer(str(i)))

afns.escalar_automatos()

while True:
    marcados = []
    evento = input('Informe o evento desejado: ')

    for automato in automatos:
        if existe_no_alfabeto(automato, evento) and transicao_possivel(automato, evento):
            marcados.append(automato)
        
        elif existe_no_alfabeto(automato, evento) and not transicao_possivel(automato, evento):
            marcados = []
            break

    if len(marcados) == 0:
        print('>> Transição impossível para o estado corrente da máquina <<')

    for automato in marcados:
        evoluir(automato, evento)

    tuplas = ''

    for automato in automatos:
        tuplas += '({}), '.format(estado_atual(automato)[0] + ', ' + estado_atual(automato)[1])
    
    print('>> Estado corrente: {} <<'.format(tuplas))
    

            
            