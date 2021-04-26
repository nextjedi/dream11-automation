import json
import itertools
import time
with open("team.json") as team:
    data = json.load(team)

def combination(arr, size):
    return list(itertools.chain(itertools.combinations(arr, size)))


players = data['players']
print(len(players))
kol_bat=[]
kol_must=[]
kol_bowl=[]
pun_open=[]
pun_bat=[]
pun_must=[]
pun_bowl=[]
for player in players:
    if player['name'] == "R Tripathi" or player['name']== "E Morgan":
        kol_bat.append(player)
    elif player['name'] == "A Russel" or player['name'] == "S Narine":
        kol_must.append(player)
    elif player['name'] == "P Cummins" or player['name'] == "V chakrabarthy" or player['name'] == "S Mavi"or player['name'] == "P krishna":
        kol_bowl.append(player)
    elif player['name'] == "L Rahul" or player['name'] == "M Agrawal":
        pun_open.append(player)
    elif player['name'] == "N Pooran" or player['name'] == "S Khan":
        pun_bat.append(player)
    elif player['name'] == "D Hooda":
        pun_must.append(player)
    elif player['name'] == "R Bishnoi" or player['name'] == "M Shami"or player['name'] == "C Jordan":
        pun_bowl.append(player)

kol_ba = combination(kol_bat, 2)
kol_ba.append(combination(kol_bat,0))


kol_mus = combination(kol_must,1)
kol_mus.append(combination(kol_must,2))

kol_bow = combination(kol_bowl, 2)
kol_bow.append(combination(kol_bowl,3))

pun_ope = combination(pun_open, 1)
pun_ope.append(combination(pun_open,2))

pun_ba = combination(pun_bat, 1)

pun_mus = combination(pun_must, 1)

pun_bow = combination(pun_bowl,3)

print(len(kol_ba))
print(len(kol_mus))
print(len(kol_bow))
print(len(pun_ope))
print(len(pun_ba))
print(len(pun_mus))
print(len(pun_bow))

# create all combination
teams=[]
for a in kol_ba:
    for b in kol_mus:
        for c in kol_bow:
            for d in pun_ope:
                for e in pun_ba:
                    for f in pun_mus:
                        for g in pun_bow:
                            teams.append(list(itertools.chain(a,b,c,d,e,f,g)))
final_teams=[]
print(len(teams))
for team in teams:
    final_team = []
    for player in team:
        if type(player) is not dict:
            # print(type(player))
            for p in player:
                final_team.append(p)
        else:
            final_team.append(player)
    final_teams.append(final_team)

valid_teams = []
for team in final_teams:
    # validate team
    if len(team) != 11:
        # print("invalid")
        continue

    total_credit=0
    bat_count=0
    bowl_count=0
    ar_count=0
    wk_count=0
    pbks_count = 0
    kol_count = 0
    
    for player in team:
        total_credit+=player['credit']
        if player['team'] == "pbks":
            pbks_count +=1
            
        else:
            kol_count +=1
        if player['type'] == "ar":
            ar_count +=1
        elif player['type'] == "bat":
            bat_count +=1
        elif player['type'] == "wk":
            wk_count +=1
        elif player['type'] == "bowl":
            bowl_count +=1
    if pbks_count<8 and kol_count<8 and total_credit<=100 and wk_count>0 and wk_count <=5 and bat_count >2 and bat_count <7 and bowl_count >2 and bowl_count <7 and ar_count > 0 and ar_count<5:
        valid_teams.append(team)

        
    # print(team)
    # time.sleep(5)
print(len(final_teams))
teamtomake=[]
top_score = 0 
for team in valid_teams:
    captain=0
    vc=0
    temp_maX=0
    score = 0
    for player in team:
        score +=player['point']
        if player['point'] > captain:
            captain = player['point']
        if player['point']>temp_maX:
            vc=temp_maX
            temp_maX =player['point']
        elif player['point']>vc :
            vc=player['point']



    score= score +captain+vc/2 
    
    if score > top_score:
        top_score = score
print("captain score is ",captain)
print("vC score is ",vc)
print("Top score is ", top_score)

for team in valid_teams:
    teamn=[]
    for player in team:
        teamn.append(player['name'])
    teamtomake.append(teamn)

print("NUMBER OF TEAMS ASSUMING CAPTAIN IS SELECTED PERFECTLY - " , len(teamtomake))

# for i in range(len(teamtomake)):
#     if i>44 and i < 56:
#         print("team ",i)
#         print(teamtomake[i])