import json,ssl,requests 

nome = raw_input('Digite seu Nick :')

inf_jogador = requests.get('https://br.api.pvp.net/api/lol/br/v1.4/summoner/by-name/'+nome+'?api_key=80cf3727-4a7d-4b04-b5e4-3f62cdb47631')
inf = json.loads(inf_jogador.content)
###### INFORMAÇOES DO INVOCADOR ############
id_inv = inf[nome]['id']
nome_inv = inf[nome]['name']
lvl = inf[nome]['summonerLevel']  
###### INFORMAÇOES DO ELO ############
inf_elo = requests.get('https://br.api.pvp.net/api/lol/br/v2.5/league/by-summoner/'+str(id_inv)+'/entry?api_key=80cf3727-4a7d-4b04-b5e4-3f62cdb47631')
invo_elo = json.loads(inf_elo.content)


print 'id : ' + str(id_inv)
print 'Nome Invocador : ' +  nome_inv
print 'Lvl : ' + str(lvl)

for i in invo_elo.values():
   print 'ELO : ' + i[0]['tier']
    
for i in invo_elo.values():
    print 'Divisão : ' + str(i[0]['entries'][0]['division'])

for i in invo_elo.values():
    print 'Vitorias : ' + str(i[0]['entries'][0]['wins'])

for i in invo_elo.values():
    print 'Derrotas : ' + str(i[0]['entries'][0]['losses'])

for i in invo_elo.values():
    print 'PDL´s : ' + str(i[0]['entries'][0]['leaguePoints'])


