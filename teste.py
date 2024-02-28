# dados manipulado por pandas
# acesso a base de dados por sqlite

import pandas as pd
from pandas import DataFrame

# lendo as quantidades brutas

df_dado_bruto = pd.read_excel('dados_brutos.xlsx', sheet_name=0,  engine='openpyxl', index_col=0)

f_dado_bruto_peso = pd.read_excel('dados_brutos.xlsx', sheet_name=1,  engine='openpyxl', index_col=0)

df_dado_padronizado = df_dado_bruto.apply(lambda x: x / x.sum() * 100, axis=0)

# indicadores transversais
# Pr1-Transversal – PRISÕES E TERMOS CIRCUNSTANCIADOS DE OCORRÊNCIA
# Pr2-Transversal – DESCAPITALIZAÇÃO
# Pr3-Transversal – OPERAÇÕES DE POLÍCIA JUDICIÁRIA
# Pr4-Transversal – BUSCA E APREENSÃO
# Pr5-Transversal – OUTRAS MEDIDAS CAUTELARES DISTINTAS DA PRISÃO
# Pr6-Transversal – INDICIAMENTOS
# Pr7-Transversal – RELATÓRIOS FINAIS DE OPERAÇÕES DE POLÍCIA JUDICIÁRIA
# Pr8-Transversal – COOPERAÇÃO INTERNACIONAL
# Pr9-Transversal – APOIO OPERACIONAL (MOBILIZAÇÃO DE SERVIDORES)
# Pr10-Transversal – APOIO OPERACIONAL (FORNECIMENTO DE INFORMAÇÕES)

# Sigla
# trvsl - transversal
# pr    - produtividade
# ps    - peso


pr_trvsl_01 = 1
ps_trvsl_01 = 1
pr_trvsl_02 = 1
ps_trvsl_02 = 1
pr_trvsl_03 = 1
ps_trvsl_03 = 1
pr_trvsl_04 = 1
ps_trvsl_04 = 1
pr_trvsl_05 = 1
ps_trvsl_05 = 1
pr_trvsl_06 = 1
ps_trvsl_06 = 1
pr_trvsl_07 = 1
ps_trvsl_07 = 1
pr_trvsl_08 = 1
ps_trvsl_08 = 1
pr_trvsl_09 = 1
ps_trvsl_09 = 1
pr_trvsl_10 = 1
ps_trvsl_10 = 1


pr_trvsl = ((
             pr_trvsl_01 * ps_trvsl_01 + pr_trvsl_02 * ps_trvsl_02 + pr_trvsl_03 * ps_trvsl_03 +
             pr_trvsl_04 * ps_trvsl_04 + pr_trvsl_05 * ps_trvsl_05 + pr_trvsl_06 * ps_trvsl_06 +
             pr_trvsl_07 * ps_trvsl_07 + pr_trvsl_08 * ps_trvsl_08 + pr_trvsl_09 * ps_trvsl_09 +
             pr_trvsl_10 * ps_trvsl_10) /
            (
             ps_trvsl_01 + ps_trvsl_02 + ps_trvsl_03 + ps_trvsl_04 + ps_trvsl_05 +
             ps_trvsl_06 + ps_trvsl_07 + ps_trvsl_08 + ps_trvsl_09 + ps_trvsl_10))

# salvar os resultados