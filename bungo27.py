  # -*- coding: cp1252 -*-

print "Bem-vindo!\n"

print "Insira as informações solicitadas abaixo para identificar a modalidade de manifestação em relação a empreendimentos/atividades propostos para instalação e operação no interior ou no entorno de unidades de conservação federais. \n"

print "EIA = Com Estudo de Impacto Ambiental / SEIA = Sem Estudo de Impacto Ambiental / NALic = Não se aplica licenciamento ambiental / CZA = Unidade de Conservação com Zona de Amortecimento / SZA = Unidade de Conservação sem Zona de Amortecimento / CZA = Unidade de Conservação em que não se aplica Zona de Amortecimento / IUC = Interior da Unidade de Conservação / FUC = Fora de Unidade de Conservação / FZPD3 = Fora da Zona de Presunção de Danos de 3 km / IZA = Interior da Zona de Amortecimento / FZA = Fora da Zona de Amortecimento / ZPD3 = Na Zona de Presunção de Danos de 3 km / FZPD3 = Fora da Zona de Presunção de Danos de 3 km / ZPD2 = Na Zona de Presunção de Danos de 2 km / FZPD2 = Fora da Zona de Presunção de Danos de 2 km \n"

print "--------------------------------------------------------------------------------------------------- \n"

print "DIGITE A ALTERNATIVA ADEQUADA: \n"  

emp = raw_input ("Enquadramento: \n EIA \n SEIA \n NALic \n") # emp = variável que informa o tipo de licenciamento

UC = raw_input ("Unidade: \n CZA \n SZA \n NAZA \n") # UC = variável que informa a situação da UC em relação ao zoneamento

if UC == "CZA":
    uccza = raw_input ("Localização: \n IUC \n IZA \n FZA \n") # uccza = variável que informa a localização do empreendimento para UCs que possuem zona de amortecimento
	
elif UC == "SZA":
    if emp == "EIA":
        ucsza1 = raw_input ("Localização: \n IUC \n ZPD3 \n FZPD3 \n") # ucsza1 = variável que informa a localização do empreendimento para UCs sem zona de amortecimento e com licenciamento com EIA-RIMA

    elif emp == "SEIA":
        ucsza2 = raw_input ("Localização: \n IUC \n ZPD2 \n FZPD2 \n") # ucsza2 = variável que informa a localização do empreendimento para UCs sem zona de amortecimento e com licenciamento sem EIA-RIMA
    else:
        ucnalic = raw_input ("Localização: \n IUC \n FUC \n") # ucnalic = variável que informa a localização do empreendimento ou atividade não licenciável
        
else:
    ucnaza = raw_input ("Localização: \n IUC \n FUC \n") # ucnaza = variável que informa a localização do empreendimento para APAs e RPPNs

print "----------------------------------------------------------------------------------------------------- \n"

print "PROCEDIMENTO APLICÁVEL: \n"  

if (emp == "EIA" and UC == "CZA" and uccza == "IUC") or (emp == "EIA" and UC == "CZA" and uccza == "IZA") or (emp == "EIA" and UC == "CZA" and uccza == "FZA") or (emp == "SEIA" and UC == "CZA" and uccza == "IUC") or (emp == "SEIA" and UC == "CZA" and uccza == "FZA") or (emp == "EIA" and UC == "SZA" and ucsza1 == "IUC") or (emp == "EIA" and UC == "SZA" and ucsza1 == "ZPD3") or (emp == "SEIA" and UC == "SZA" and ucsza2 == "IUC"):
    print "Necessidade de AUTORIZAÇÃO para o licenciamento ambiental em curso, nos termos do Art. 1º da Resolução CONAMA nº 428/2010 e Instrução Normativa ICMBio nº 07/2014. \n"
 
elif (emp == "SEIA" and UC == "CZA" and uccza == "IZA") or (emp == "SEIA" and UC == "SZA" and ucsza2 == "ZPD2"):
    print "Necessidade de CIÊNCIA do licenciamento ambiental em curso, nos termos do Art. 5º da Resolução CONAMA nº 428/2010 e e Instrução Normativa ICMBio nº 07/2014. \n"

elif (emp == "NALic" and UC == "CZA" and uccza == "IUC") or (emp == "NALic" and UC == "SZA" and ucnalic == "IUC") or (emp == "EIA" and UC == "NAZA" and ucnaza == "IUC") or (emp == "SEIA" and UC == "NAZA" and ucnaza == "IUC") or (emp == "NALic" and UC == "NAZA" and ucnaza == "IUC"):
    print "O interessado (empreendedor) deve requerer autorização diretamente à Unidade de Conservação (AUTORIZAÇÃO DIRETA, nos termos da Instrução Normativa ICMBio nº 04/2009). \n"

else:
    print "Não é necessária manifestação do órgão gestor da Unidade de Conservação. \n"

print "----------------------------------------------------------------------------------------------------- \n"



if (UC == "SZA") and (emp == "EIA" or "SEIA"):
    print "Em unidades de conservação que não possuem ZA, as faixas de 3 e 2 km a partir dos limites da UC são entendidas como Zonas de Presunção de Danos (exceto em APA e RPPN), aplicáveis para empreendimentos/atividades licenciados com EIA-RIMA e sem EIA-RIMA, respectivamente (conforme Resolução CONAMA nº 428/2010). \n"

print "OBSERVAÇÃO: Em unidade de conservação com plano de manejo e/ou com zona de amortecimento legalmente instituída, poderá haver imposição de limitações administrativas e exigência de autorização para determinadas atividades ou áreas definidas, conforme dispõe o Art. 2º, § 5º da Resolução CONAMA nº 428/2010, podendo implicar eventual alteração no presente enquadramento. \n"

print "A análise para determinação do procedimento aplicável a cada situação baseia-se nos seguintes intrumentos legais: Art. 36 da Lei nº 9985/2000; Art. 1º da Lei nº 11516/07; Resolução CONAMA nº 428/2010; Instrução Normativa ICMBio nº 07/2014; Instrução Normativa ICMBio nº 04/2009 e Parecer nº 0496/2011-PFE-ICMBio-SEDE/PGF/AGU. \n"
print "Versão 0.1"
print "Autor: Arlindo Gomes Filho"
print "Contato: argofix@gmail.com"





    


