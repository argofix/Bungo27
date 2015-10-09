  # -*- coding: cp1252 -*-

print "Bem-vindo!\n"

print "Insira as informa��es solicitadas abaixo para identificar a modalidade de manifesta��o em rela��o a empreendimentos/atividades propostos para instala��o e opera��o no interior ou no entorno de unidades de conserva��o federais. \n"

print "EIA = Com Estudo de Impacto Ambiental / SEIA = Sem Estudo de Impacto Ambiental / NALic = N�o se aplica licenciamento ambiental / CZA = Unidade de Conserva��o com Zona de Amortecimento / SZA = Unidade de Conserva��o sem Zona de Amortecimento / CZA = Unidade de Conserva��o em que n�o se aplica Zona de Amortecimento / IUC = Interior da Unidade de Conserva��o / FUC = Fora de Unidade de Conserva��o / FZPD3 = Fora da Zona de Presun��o de Danos de 3 km / IZA = Interior da Zona de Amortecimento / FZA = Fora da Zona de Amortecimento / ZPD3 = Na Zona de Presun��o de Danos de 3 km / FZPD3 = Fora da Zona de Presun��o de Danos de 3 km / ZPD2 = Na Zona de Presun��o de Danos de 2 km / FZPD2 = Fora da Zona de Presun��o de Danos de 2 km \n"

print "--------------------------------------------------------------------------------------------------- \n"

print "DIGITE A ALTERNATIVA ADEQUADA: \n"  

emp = raw_input ("Enquadramento: \n EIA \n SEIA \n NALic \n") # emp = vari�vel que informa o tipo de licenciamento

UC = raw_input ("Unidade: \n CZA \n SZA \n NAZA \n") # UC = vari�vel que informa a situa��o da UC em rela��o ao zoneamento

if UC == "CZA":
    uccza = raw_input ("Localiza��o: \n IUC; \n IZA \n FZA \n") # uccza = vari�vel que informa a localiza��o do empreendimento para UCs que possuem zona de amortecimento
	
elif UC == "SZA":
    if emp == "EIA":
        ucsza1 = raw_input ("Localiza��o: \n IUC \n ZPD3 \n FZPD3 \n") # ucsza1 = vari�vel que informa a localiza��o do empreendimento para UCs sem zona de amortecimento e com licenciamento com EIA-RIMA

    elif emp == "SEIA":
        ucsza2 = raw_input ("Localiza��o: \n IUC \n ZPD2 \n FZPD2 \n") # ucsza2 = vari�vel que informa a localiza��o do empreendimento para UCs sem zona de amortecimento e com licenciamento sem EIA-RIMA
    else:
        ucnalic = raw_input ("Localiza��o: \n IUC \n FUC \n") # ucnalic = vari�vel que informa a localiza��o do empreendimento ou atividade n�o licenci�vel
        
else:
    ucnaza = raw_input ("Localiza��o: \n IUC \n FUC \n") # ucnaza = vari�vel que informa a localiza��o do empreendimento para APAs e RPPNs

print "----------------------------------------------------------------------------------------------------- \n"

print "PROCEDIMENTO APLIC�VEL: \n"  

if (emp == "EIA" and UC == "CZA" and uccza == "IUC") or (emp == "EIA" and UC == "CZA" and uccza == "IZA") or (emp == "EIA" and UC == "CZA" and uccza == "FZA") or (emp == "SEIA" and UC == "CZA" and uccza == "IUC") or (emp == "SEIA" and UC == "CZA" and uccza == "FZA") or (emp == "EIA" and UC == "SZA" and ucsza1 == "IUC") or (emp == "EIA" and UC == "SZA" and ucsza1 == "ZPD3") or (emp == "SEIA" and UC == "SZA" and ucsza2 == "IUC"):
    print "Necessidade de AUTORIZA��O para o licenciamento ambiental em curso, nos termos do Art. 1� da Resolu��o CONAMA n� 428/2010 e Instru��o Normativa ICMBio n� 07/2014. \n"
 
elif (emp == "SEIA" and UC == "CZA" and uccza == "IZA") or (emp == "SEIA" and UC == "SZA" and ucsza2 == "ZPD2"):
    print "Necessidade de CI�NCIA do licenciamento ambiental em curso, nos termos do Art. 5� da Resolu��o CONAMA n� 428/2010 e e Instru��o Normativa ICMBio n� 07/2014. \n"

elif (emp == "NALic" and UC == "CZA" and uccza == "IUC") or (emp == "NALic" and UC == "SZA" and ucnalic == "IUC") or (emp == "EIA" and UC == "NAZA" and ucnaza == "IUC") or (emp == "SEIA" and UC == "NAZA" and ucnaza == "IUC") or (emp == "NALic" and UC == "NAZA" and ucnaza == "IUC"):
    print "O interessado (empreendedor) deve requerer autoriza��o diretamente � Unidade de Conserva��o (AUTORIZA��O DIRETA, nos termos da Instru��o Normativa ICMBio n� 04/2009). \n"

else:
    print "N�o � necess�ria manifesta��o do �rg�o gestor da Unidade de Conserva��o. \n"

print "----------------------------------------------------------------------------------------------------- \n"



if (UC == "SZA") and (emp == "EIA" or "SEIA"):
    print "Em unidades de conserva��o que n�o possuem ZA, as faixas de 3 e 2 km a partir dos limites da UC s�o entendidas como Zonas de Presun��o de Danos (exceto em APA e RPPN), aplic�veis para empreendimentos/atividades licenciados com EIA-RIMA e sem EIA-RIMA, respectivamente (conforme Resolu��o CONAMA n� 428/2010). \n"

print "OBSERVA��O: Em unidade de conserva��o com plano de manejo e/ou com zona de amortecimento legalmente institu�da, poder� haver imposi��o de limita��es administrativas e exig�ncia de autoriza��o para determinadas atividades ou �reas definidas, conforme disp�e o Art. 2�, � 5� da Resolu��o CONAMA n� 428/2010, podendo implicar eventual altera��o no presente enquadramento. \n"

print "A an�lise para determina��o do procedimento aplic�vel a cada situa��o baseia-se nos seguintes intrumentos legais: Art. 36 da Lei n� 9985/2000; Art. 1� da Lei n� 11516/07; Resolu��o CONAMA n� 428/2010; Instru��o Normativa ICMBio n� 07/2014; Instru��o Normativa ICMBio n� 04/2009 e Parecer n� 0496/2011-PFE-ICMBio-SEDE/PGF/AGU. \n"
print "Vers�o 0.1"
print "Autor: Arlindo Gomes Filho"
print "Contato: argofix@gmail.com"





    


