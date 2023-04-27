# Variáveis
rq = ''
opr = 1, 2, 3, 4, 5
res = ''


# Defs
def lin():
    print('-' * 45)
    
    
# Operações
operacao = {1: 'Operador de Conjunção', 2: 'Disjunção Simples', 3: 'Operador Condicional',
            4: 'Operador Bicondicional', 5: 'Disjunção Exclusiva'}

# Bom dia
lin()
print(' '*8, 'BOM DIA ESTUDANTE DO SENAI!\n', ' '*2, 'Tabela Verdade SENAI by Henrique Souza')
lin(), print('\n')

# Selecione a operação desejada
print('Qual lógica está sendo aplicada?', operacao)
log = int(float(input('> ')))

# Mensagem de Confirmação da operação
if log in opr:
    opr = int(log)
    print('Certo, vamos trabalhar com ', operacao[int(opr)], '.', sep='')

# Pergunte pela Antecedente 'p'
p = input('A antecedente é V ou F? ').lower()
while p not in ('v', 'f'):
    p = input("Desculpe, não entendi. A antecedente é V ou F? ").lower()
if p in v:
    rp = True
elif p in f:
    rp = False

# Pergunte pela Consequente 'q'
q = input('A consequente é V ou F? ').lower()
while q not in ('v', 'f'):
    q = input("Desculpe, não entendi. A consequente é V ou F? ").lower()
if q in v:
    rq = True
elif q in f:
    rq = False

# Operador de Conjunção
if log == 1:
    if rp is True and rp is rq:
        res = 'V'
    else:
        res = 'F'

# Disjunção Simples
if log == 2:
    if rp is False and rp is rq:
        res = 'F'
    else:
        res = 'V'

# Operador Condicional
if log == 3:
    if rp is True and rq is False:
        res = 'F'
    else:
        res = 'V'

# Operador Bicondicional
if log == 4:
    if rp is rq:
        res = 'V'
    else:
        res = 'F'

# Disjunção Exclusiva
if log == 5:
    if rp is not rq:
        res = 'V'
    else:
        res = 'F'

# Resultado Final

if res == 'V':
    res = 'Verdadeira'
if res == 'F':
    res = 'Falsa'
print(' \n', '[A proposição é ', res, ']', '\n', sep='')
