# dados manipulado por pandas
# acesso a base de dados por sqlite
# testando o git

import pandas as pd
import sqlite3 as bd


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
ps_trvsl_10 = 10


pr_trvsl = (
             pr_trvsl_01 * ps_trvsl_01 + pr_trvsl_02 * ps_trvsl_02 + pr_trvsl_03 * ps_trvsl_03 +
             pr_trvsl_04 * ps_trvsl_04 + pr_trvsl_05 * ps_trvsl_05 + pr_trvsl_06 * ps_trvsl_06 +
             pr_trvsl_07 * ps_trvsl_07 + pr_trvsl_08 * ps_trvsl_08 + pr_trvsl_09 * ps_trvsl_09 +
             pr_trvsl_10 * ps_trvsl_10
            )
                /
           (
             ps_trvsl_01 + ps_trvsl_02 + ps_trvsl_03 + ps_trvsl_04 + ps_trvsl_05 +
             ps_trvsl_06 + ps_trvsl_07 + ps_trvsl_08 + ps_trvsl_09 + ps_trvsl_10
           )