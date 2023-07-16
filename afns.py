
#descrição dos automatos com suporte a 1 produto 
#(o resto é gerado pela função escalar_automatos)
geral = {
    # AFN Moore, tupla (estado, mensagem)
    'estado': ('0_sel', 'Selecione o produto: '),
    'alfabeto': [
                 'ini_man', 'fim_man', '1_sel', 'tem_p1', 
                 'ini_pg_p1', 'conf_pg_p1', 'ini_ent_p1', 
                 'ven_p1', 'fim_ent_p1', 'n_tem_p1',
                 'n_conf_pg_p1'
                 ],
    # Tabela de transições, tupla (estado, transição) -> (estado, mensagem)
    'transicoes': {
        ('0_sel', '1_sel'): ('1_se', 'Produto 1 selecionado'),
        ('1_se', 'tem_p1'): ('1_te', 'Produto em estoque'),
        ('1_se', 'n_tem_p1'): ('0_sel', 'Produto sem estoque'),
        ('1_te', 'ini_pg_p1'): ('1_ip', 'Selecione a forma de pagamento: '),
        ('1_ip', 'n_conf_pg_p1'): ('0_sel', 'Pagamento não configurado'),
        ('1_ip', 'conf_pg_p1'): ('1_cp', 'Pagamento aceito'),
        ('1_cp', 'ini_ent_p1'): ('1_ie', 'Iniciando entrega'),
        ('1_ie', 'ven_p1'): ('1_fe', 'Finalizando entrega'),
        ('1_fe', 'fim_ent_p1'): ('0_sel', 'Selecione o produto:'),
        ('0_sel', 'ini_man'): ('man', 'Modo de manuteção'),
        ('man', 'fim_man'): ('0_sel', 'Selecione o produto:')
    }
}



manutencao = {
    'estado': ('0_mt', ''),
    'alfabeto': [
                 'ini_man', 'fim_man', 'ini_rep_p1',
                 'rep_p1', 'fim_rep_p1'
                ],
    'transicoes': {
        ('0_mt', 'ini_man'): ('1_mt', ''),
        ('1_mt', 'ini_rep_p1'): ('1_rp', ''),
        ('1_rp', 'rep_p1'): ('1_rp', ''),
        ('1_rp', 'fim_rep_p1'): ('1_mt', ''),
        ('1_mt', 'fim_man'): ('0_mt', '')
    }
}

pagamento = {
    'estado': ('0_vd', ''),
    'alfabeto': [
                    'ini_pg_p1', 'pf_cash_p1', 'pg_cartao_p1',
                    'pg_ok_p1', 'pg_nok_p1', 'conf_pg_p1',
                    'troco_p1', 'n_troco_p1', 'n_conf_pg_p1'
                ],
    'transicoes': {
        ('0_vd', 'ini_pg_p1'): ('1_vd1', ''),
        ('1_vd1', 'pg_cash_p1'): ('2_vd1', ''),
        ('2_vd1', 'pg_nok_p1'): ('5_vd1', ''),
        ('1_vd1', 'pg_cartao_p1'): ('3_vd1', ''),
        ('3_vd1', 'pg_nok_p1'): ('5_vd1', ''),
        ('3_vd1', 'pg_ok_p1'): ('7_vd1', ''),
        ('5_vd1', 'n_conf_pg_p1'): ('0_vd', ''),
        ('2_vd1', 'pg_ok_p1'): ('4_vd1', ''),
        ('4_vd1', 'troco_p1'): ('6_vd1', ''),
        ('4_vd1', 'n_troco_p1'): ('6_vd1', ''),
        ('7_vd1', 'conf_pg_p1'): ('0_vd', ''),
        ('6_vd1', 'conf_pg_p1'): ('0_vd', '')
    }
}

# função para gerar as transições e estados que foram
# omitidos no modelo que o prof passou
def escalar_automatos():
    for produto in range(2, 21):
        temp = [f'{produto}_sel', f'tem_p{produto}', 
                 f'ini_pg_p{produto}', f'conf_pg_p{produto}', f'ini_ent_p{produto}', 
                 f'ven_p{produto}', f'fim_ent_p{produto}', f'n_tem_p{produto}',
                 'n_conf_pg_p1']
        for i in temp:
            geral['alfabeto'].append(i)
        
        geral['transicoes'].update({
            ('0_sel', f'{produto}_sel'): (f'{produto}_se', f'Produto {produto} selecionado'),
            (f'{produto}_se', f'tem_p{produto}'): (f'{produto}_te', 'Produto em estoque'),
            (f'{produto}_se', f'n_tem_p{produto}'): ('0_sel', 'Produto sem estoque'),
            (f'{produto}_te', f'ini_pg_p{produto}'): (f'{produto}_ip', 'Selecione a forma de pagamento: '),
            (f'{produto}_ip', f'n_conf_pg_p{produto}'): ('0_sel', 'Pagamento não configurado'),
            (f'{produto}_ip', f'conf_pg_p{produto}'): (f'{produto}_cp', 'Pagamento aceito'),
            (f'{produto}_cp', f'ini_ent_p{produto}'): (f'{produto}_ie', 'Iniciando entrega'),
            (f'{produto}_ie', f'ven_p{produto}'): (f'{produto}_fe', 'Finalizando entrega'),
            (f'{produto}_fe', f'fim_ent_p{produto}'): ('0_sel', 'Selecione o produto:'),
        })

        manutencao['alfabeto'].extend([f'ini_rep_p{produto}', f'rep_p{produto}', f'fim_rep_p{produto}'])
        manutencao['transicoes'].update({
            ('1_mt', f'ini_rep_p{produto}'): (f'1_{produto}_rp', ''),
            (f'1_{produto}_rp', f'rep_p{produto}'): (f'1_{produto}_rp', ''),
            (f'1_{produto}_rp', f'fim_rep_p{produto}'): ('1_mt', '')
        })
        
        pagamento['alfabeto'].extend([f'ini_pg_p{produto}', f'pf_cash_p{produto}', f'pg_cartao_p{produto}', 
                                     f'pg_ok_p{produto}', f'pg_nok_p{produto}', f'conf_pg_p{produto}',
                                     f'troco_p{produto}', f'n_troco_p{produto}', f'n_conf_pg_p{produto}'])
        pagamento['transicoes'].update({
            ('0_vd', f'ini_pg_p{produto}'): (f'1_vd{produto}', ''),
            (f'1_vd{produto}', f'pf_cash_p{produto}'): (f'2_vd{produto}', ''),
            (f'2_vd{produto}', f'pg_nok_p{produto}'): (f'5_vd{produto}', ''),
            (f'1_vd{produto}', f'pg_cartao_p{produto}'): (f'3_vd{produto}', ''),
            (f'3_vd{produto}', f'pg_nok_p{produto}'): (f'5_vd{produto}', ''),
            (f'3_vd{produto}', f'pg_ok_p{produto}'): (f'7_vd{produto}', ''),
            (f'5_vd{produto}', f'n_conf_pg_p{produto}'): ('0_vd', ''),
            (f'2_vd{produto}', f'pg_ok_p{produto}'): (f'4_vd{produto}', ''),
            (f'4_vd{produto}', f'troco_p{produto}'): (f'6_vd{produto}', ''),
            (f'4_vd{produto}', f'n_troco_p{produto}'): (f'6_vd{produto}', ''),
            (f'7_vd{produto}', f'conf_pg_p{produto}'): ('0_vd', ''),
            (f'6_vd{produto}', f'conf_pg_p{produto}'): ('0_vd', '')
        })

# Uma factory para criar os buffers
def factory_buffer(num_buffer : str) -> dict: 
    buffer = {
        'estado': ('0', ''),
        'alfabeto': ['rep_p' + num_buffer, 'ven_p' + num_buffer, 'tem_p' + num_buffer],
        'transicoes': {
            ('0', 'rep_p' + num_buffer): ('1', ''),
            ('1', 'rep_p' + num_buffer): ('2', ''),
            ('2', 'rep_p' + num_buffer): ('3', ''),
            ('3', 'rep_p' + num_buffer): ('4', ''),
            ('4', 'rep_p' + num_buffer): ('5', ''),
            ('5', 'ven_p' + num_buffer): ('4', ''),
            ('4', 'ven_p' + num_buffer): ('3', ''),
            ('3', 'ven_p' + num_buffer): ('2', ''),
            ('2', 'ven_p' + num_buffer): ('1', ''),
            ('1', 'ven_p' + num_buffer): ('0', ''),
            ('0', 'tem_p' + num_buffer): ('0', ''),
            ('1', 'tem_p' + num_buffer): ('1', ''),
            ('2', 'tem_p' + num_buffer): ('2', ''),
            ('3', 'tem_p' + num_buffer): ('3', ''),
            ('4', 'tem_p' + num_buffer): ('4', ''),
            ('5', 'tem_p' + num_buffer): ('5', ''),
        }
    }
    return buffer

# Retorna uma tupla com o novo estado (e mensagem, se o automato for o geral)
def evoluir(afn : dict, evento : str) -> tuple:
    if not existe_no_alfabeto(afn, evento) or not transicao_possivel(afn, evento):
        return False

    estado = afn['estado'][0]
    afn['estado'] = afn['transicoes'].get((estado, evento))
    return True
    

# Identifica possíveis transições a partir do estado corrente
def eventos_aceitos(afn1 : dict) -> list:
    estado = afn1['estado'][0]
    transicoes = afn1['transicoes'].items()
    aceitos = []

    for transicao in transicoes:
        if transicao[0][0] == estado:
            aceitos.append(transicao[0][1])
    
    return aceitos

def interseccao_alfabeto(afn1 : dict, afn2 : dict) -> list:
    alfabeto1 = afn1['alfabeto']
    alfabeto2 = afn2['alfabeto']
    return list(set(alfabeto1) & set(alfabeto2))

def existe_no_alfabeto(afn : dict, evento : str) -> bool:
    return evento in afn['alfabeto']

def transicao_possivel(afn : dict, evento : str) -> bool:
    return evento in afn['alfabeto'] and evento in eventos_aceitos(afn)


def estado_atual(afn : dict) -> str:
    return afn['estado']

