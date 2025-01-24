'''
Arquivo que contém as regras de transformação dos dados para os
clientes que utilizam o Fórmula Certa. 
'''

# model = {
#     'name': '',
#     'branch_name': {},
#     'file_cashflow': {
#         'columns_to_date': [],
#         'columns_to_float': [],
#         'columns_to_int': [],
#     },
#     'file_invoicing': {
#         'columns_to_date': [],
#         'columns_to_float': [],
#         'columns_to_int': [],
#         'replace_values': {},
#         'sector': [],
#         'report': [],
#         'fill_above': []
#     },
#     'file_cost': {
#         'columns_to_date': [],
#         'columns_to_float': [],
#         'columns_to_int': [],
#         'replace_values': {},
#         'sector': [],
#         'fill_above': []
#     },
#     'file_sales_per_employee': {
#         'columns_to_date': [],
#         'columns_to_float': [],
#         'columns_to_int': [],
#         'replace_values': {},
#         'sector': [],
#         'report': [],
#         'fill_above': []
#     },
#     'file_rejected_budgets': {
#         'columns_to_date': [],
#         'columns_to_float': [],
#         'columns_to_int': [],
#         'replace_values': {},
#         'sector': [],
#         'report': [],
#         'fill_above': []
#     },
#     'file_rejected_per_employee': {
#         'columns_to_date': [],
#         'columns_to_float': [],
#         'columns_to_int': [],
#         'replace_values': {},
#         'sector': [],
#         'report': [],
#         'fill_above': []
#     }
# }

example = {
    'name': 'Example',
    'branch_name': {
        1: 'EXAMPLE BRANCH 1',
        2: 'EXAMPLE BRANCH 2',
        3: 'EXAMPLE BRANCH 3'
    },
    'file_cashflow': {
        'columns_to_date': [
            'Data de Vencimento',
            'Data de Operação',
            'Data de Baixa'
        ],
        'columns_to_float': [
            'Valor'
        ],
        'columns_to_int': [

        ],
    },
    'file_invoicing': {
        'columns_to_date': [
            'Data'
        ],
        'columns_to_float': [
            'Quantidade',
            '% Quantidade',
            'Total Bruto',
            'Total Desconto',
            'Total Taxa',
            'Total Liquido',
            '% Total Liquido'
        ],
        'columns_to_int': [
            'Nº Filial'
        ],
        'replace_values': {
            'NUTRIï¿½ï¿½O ': 'NUTRIEÇO',
            'Cï¿½psula': 'Capsula',
            'C psula': 'Capsula',
            'Loï¿½ï¿½o': 'Locao',
            'Soluï¿½ï¿½o Oral': 'Solucao Oral',
            'NUTRIÇO': 'NUTRIEÇO',
            'SoluÆo Oral': 'Solução Oral',
            'C psula': 'Capsula',
            'LoÆo': 'Loção',
            'EPIïS': 'EPIIS',
            'MATï¿½RIAS-PRIMAS': 'MATERIAS-PRIMAS',
            'MATRIAS-PRIMAS': 'MATERIAS-PRIMAS', 
            'Ä': '',
            'À': '',
            'Ù': '',
            'ï¿½': ''
        },
        'sector': [
            'OUTROS',
            'REVENDAS',
            'R E Q U I S I C O E S',
            'EMBALAGENS',
            'MATERIAS-PRIMAS'
        ],
        'report': [
            'RESUMO DO MOVIMENTO - GERAL',
            'DETALHES - VENDA DIARIA POR FUNCIONARIO'
        ],
        'fill_above': [
            'Tipo de Relatório',
            'Nº Filial',
            'Nome Filial',
            'Setor'
        ]
    },
    'file_cost': {
        'columns_to_date': [
            'Data'
        ],
        'columns_to_float': [
            'Quantidade',
            '% Quantidade',
            'Valor (Custo)',
            '% Valor (Custo)'
        ],
        'columns_to_int': [
            'Nº Filial'
        ],
        'replace_values': {
            'NUTRIï¿½ï¿½O ': 'NUTRIEÇO',
            'Cï¿½psula': 'Capsula',
            'C psula': 'Capsula',
            'Loï¿½ï¿½o': 'Locao',
            'Soluï¿½ï¿½o Oral': 'Solucao Oral',
            'NUTRIÇO': 'NUTRIEÇO',
            'SoluÆo Oral': 'Solução Oral',
            'C psula': 'Capsula',
            'LoÆo': 'Loção',
            'EPIïS': 'EPIIS',
            'MATï¿½RIAS-PRIMAS': 'MATERIAS-PRIMAS',
            'MATRIAS-PRIMAS': 'MATERIAS-PRIMAS', 
            'Ä': '',
            'À': '',
            'Ù': '',
            'ï¿½': ''
        },
        'sector': [
            'OUTROS',
            'REVENDAS',
            'R E Q U I S I C O E S',
            'EMBALAGENS',
            'MATERIAS-PRIMAS'
        ],
        'fill_above': [
            'Nº Filial',
            'Nome Filial',
            'Setor'
        ]
    },
    'file_sales_per_employee': {
        'columns_to_date': [
            'Data'
        ],
        'columns_to_float': [
            'Varejo',
            'Formulas'
        ],
        'columns_to_int': [],
        'replace_values': {},
        'sector': [
            'OUTROS',
            'REVENDAS',
            'R E Q U I S I C O E S',
            'EMBALAGENS',
            'MATERIAS-PRIMAS'
        ],
        'report': [
            'RESUMO DO MOVIMENTO - GERAL',
            'DETALHES - VENDA DIARIA POR FUNCIONARIO'
        ],
        'fill_above': [
            'Tipo de Relatório'
        ]
    },
    'file_rejected_budgets': {
        'columns_to_date': [],
        'columns_to_float': [
            'F.F',
            'Volume',
            'P. Venda',
            'P. Custo',
            'Fator'
        ],
        'columns_to_int': [
            ''
        ],
        'replace_values': {
            'NUTRIï¿½ï¿½O ': 'NUTRIEÇO',
            'Cï¿½psula': 'Capsula',
            'C psula': 'Capsula',
            'Loï¿½ï¿½o': 'Locao',
            'Soluï¿½ï¿½o Oral': 'Solucao Oral',
            'NUTRIÇO': 'NUTRIEÇO',
            'SoluÆo Oral': 'Solução Oral',
            'C psula': 'Capsula',
            'LoÆo': 'Loção',
            'EPIïS': 'EPIIS',
            'MATï¿½RIAS-PRIMAS': 'MATERIAS-PRIMAS',
            'MATRIAS-PRIMAS': 'MATERIAS-PRIMAS', 
            'Ä': '',
            'À': '',
            'Ù': '',
            'ï¿½': ''
        },
        'sector': [
            ''
        ],
        'report': [
            'ORCAMENTOS REJEITADOS',
            'TOTAIS POR FUNCIONARIO'
        ],
        'fill_above': [
            'Tipo de Relatório',
            'Nº Filial',
            'Nome Filial'
        ]
    },
    'file_rejected_per_employee': {
        'columns_to_date': [
            'Data'
        ],
        'columns_to_float': [],
        'columns_to_int': [],
        'replace_values': {
            'NUTRIï¿½ï¿½O ': 'NUTRIEÇO',
            'Cï¿½psula': 'Capsula',
            'C psula': 'Capsula',
            'Loï¿½ï¿½o': 'Locao',
            'Soluï¿½ï¿½o Oral': 'Solucao Oral',
            'NUTRIÇO': 'NUTRIEÇO',
            'SoluÆo Oral': 'Solução Oral',
            'C psula': 'Capsula',
            'LoÆo': 'Loção',
            'EPIïS': 'EPIIS',
            'MATï¿½RIAS-PRIMAS': 'MATERIAS-PRIMAS',
            'MATRIAS-PRIMAS': 'MATERIAS-PRIMAS', 
            'Ä': '',
            'À': '',
            'Ù': '',
            'ï¿½': ''
        },
        'sector': [
            ''
        ],
        'report': [
            'ORCAMENTOS REJEITADOS',
            'TOTAIS POR FUNCIONARIO'
        ],
        'fill_above': [
            'Tipo de Relatório',
            'Nº Filial',
            'Nome Filial'
        ]
    }
}

clients = {
    'Example': example,
}