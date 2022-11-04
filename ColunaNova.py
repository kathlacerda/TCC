import pandas as pd
import numpy as np

data = pd.read_csv(r'C:\Users\kathl\Documents\Unicap\TCC\Censo2018\tabelaAlunosFundamentalEscolas.csv', sep=';',
                   low_memory=False)

# data['RPA'] = np.where(data['ebairrnome'] == "SANTO AMARO", "RPA1")


condList = [
    # RPA1
    (data['ebairrnome'] == "SANTO AMARO") | (data['ebairrnome'] == "BOA VISTA")
    | (data['ebairrnome'] == "RECIFE")
    | (data['ebairrnome'] == "CABANGA") | (data['ebairrnome'] == "ILHA DO LEITE")
    | (data['ebairrnome'] == "PAISSANDU") | (data['ebairrnome'] == "SANTO ANTONIO")
    | (data['ebairrnome'] == "SAO JOSE") | (data['ebairrnome'] == "COELHOS")
    | (data['ebairrnome'] == "SOLEDADE") | (data['ebairrnome'] == "ILHA JOANA BEZERRA")
    # RPA2
    , (data['ebairrnome'] == "ARRUDA") | (data['ebairrnome'] == "CAMPINA DO BARRETO")
    | (data['ebairrnome'] == "ENCRUZILHADA") | (data['ebairrnome'] == "HIPODROMO")
    | (data['ebairrnome'] == "PEIXINHOS") | (data['ebairrnome'] == "PONTO DE PARADA")
    | (data['ebairrnome'] == "ROSARINHO") | (data['ebairrnome'] == "TORREAO")
    | (data['ebairrnome'] == "AGUA FRIA") | (data['ebairrnome'] == "ALTO SANTA TEREZINHA")
    | (data['ebairrnome'] == "BOMBA DO HEMETERIO") | (data['ebairrnome'] == "CAJUEIRO")
    | (data['ebairrnome'] == "FUNDAO") | (data['ebairrnome'] == "PORTO DA MADEIRA")
    | (data['ebairrnome'] == "BEBERIBE") | (data['ebairrnome'] == "DOIS UNIDOS")
    | (data['ebairrnome'] == "LINHA DO TIRO") | (data['ebairrnome'] == "CAMPO GRANDE")
    # RPA3
    , (data['ebairrnome'] == "AFLITOS") | (data['ebairrnome'] == "ALTO DO MANDU")
    | (data['ebairrnome'] == "BREJO DE BEBERIBE")
    | (data['ebairrnome'] == "ALTO JOSE BONIFACIO") | (data['ebairrnome'] == "ALTO JOSE DO PINHO")
    | (data['ebairrnome'] == "APIPUCOS") | (data['ebairrnome'] == "BREJO DA GUABIRABA")
    | (data['ebairrnome'] == "CASA AMARELA") | (data['ebairrnome'] == "CASA FORTE")
    | (data['ebairrnome'] == "CORREGO DO JENIPAPO") | (data['ebairrnome'] == "DERBY")
    | (data['ebairrnome'] == "DOIS IRMAOS") | (data['ebairrnome'] == "ESPINHEIRO")
    | (data['ebairrnome'] == "GRACAS") | (data['ebairrnome'] == "GUABIRABA")
    | (data['ebairrnome'] == "JAQUEIRA") | (data['ebairrnome'] == "MACAXEIRA")
    | (data['ebairrnome'] == "MONTEIRO") | (data['ebairrnome'] == "NOVA DESCOBERTA")
    | (data['ebairrnome'] == "PARNAMIRIM") | (data['ebairrnome'] == "PASSARINHO")
    | (data['ebairrnome'] == "POCO DA PANELA") | (data['ebairrnome'] == "SANTANA")
    | (data['ebairrnome'] == "SITIO DOS PINTOS") | (data['ebairrnome'] == "TAMARINEIRA")
    | (data['ebairrnome'] == "MANGABEIRA") | (data['ebairrnome'] == "MORRO DA CONCEICAO")
    | (data['ebairrnome'] == "VASCO DA GAMA")
    # RPA4
    , (data['ebairrnome'] == "ILHA DO RETIRO") | (data['ebairrnome'] == "CORDEIRO")
    | (data['ebairrnome'] == "IPUTINGA") | (data['ebairrnome'] == "MADALENA")
    | (data['ebairrnome'] == "PRADO") | (data['ebairrnome'] == "TORRE")
    | (data['ebairrnome'] == "ZUMBI") | (data['ebairrnome'] == "ENGENHO DO MEIO")
    | (data['ebairrnome'] == "TORROES") | (data['ebairrnome'] == "CAXANGA")
    | (data['ebairrnome'] == "CANXANGA") | (data['ebairrnome'] == "VARZEA")
    # RPA5
    , (data['ebairrnome'] == "AFOGADOS") | (data['ebairrnome'] == "AREIAS")
    | (data['ebairrnome'] == "BARRO") | (data['ebairrnome'] == "BONGI")
    | (data['ebairrnome'] == "CACOTE") | (data['ebairrnome'] == "COQUEIRAL")
    | (data['ebairrnome'] == "CURADO") | (data['ebairrnome'] == "ESTANCIA")
    | (data['ebairrnome'] == "JARDIM SAO PAULO") | (data['ebairrnome'] == "JIQUIA")
    | (data['ebairrnome'] == "MANGUEIRA") | (data['ebairrnome'] == "MUSTARDINHA")
    | (data['ebairrnome'] == "SAN MARTIN") | (data['ebairrnome'] == "SANCHO")
    | (data['ebairrnome'] == "TEJIPIO") | (data['ebairrnome'] == "TOTO")
    # RPA6
    , (data['ebairrnome'] == "BOA VIAGEM") | (data['ebairrnome'] == "BRASILIA TEIMOSA")
    | (data['ebairrnome'] == "IMBIRIBEIRA") | (data['ebairrnome'] == "IPSEP")
    | (data['ebairrnome'] == "PINA") | (data['ebairrnome'] == "IBURA")
    | (data['ebairrnome'] == "JORDAO") | (data['ebairrnome'] == "COHAB")
]

choicelist = ["RPA1", "RPA2", "RPA3", "RPA4", "RPA5", "RPA6"]

data['RPA'] = np.select(condList, choicelist, default='NaN')

condition_list = [#N
    (data['situ'] == "AP") | (data['situ'] == "TR") | (data['situ'] == "TA") | (data['situ'] == "MO")
    | (data['situ'] == "TS"),
    #Y
    (data['situ'] == "RT") | (data['situ'] == "RF")| (data['situ'] == "RTTA")
    | (data['situ'] == "D") | (data['situ'] == "DERN") | (data['situ'] == "DETA")
]
choice_list = ["n", "y"]
print(data)

data['FALHOU'] = np.select(condition_list, choice_list, default='xxx')

data.to_csv("tabelaAlunosEscolasRPA.csv")
