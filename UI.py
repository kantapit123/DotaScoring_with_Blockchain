#Add New Match
print("===== This is Dota2 Scoring with Blockchain =====")
team_list = ['OG', 'Fnatic', 'PSG', 'Team Spirit']

n = 0
teamA = ""
teamB = ""
for i in team_list:
    n += 1
    print("[%d]" % (n) + i)
while True:
    team1 = int(input("Pick the first team : "))
    if team1 > len(team_list):
        print("please enter team name in tournaments!!!")
        continue
    team2 = int(input("Pick the second team : "))
    if team2 > len(team_list):
        print("please enter team name in tournaments!!!")
        continue
    teamA = team_list[team1-1]
    teamB = team_list[team2-1]
    if teamA != teamB:
        break
    else:
        print("Do not enter the same Team!!!")

print("===== "+ teamA +" VS "+ teamB +" =====")
while True:
    bo = int(input("This match is Best of (1|3|5) : "))
    if bo == 1 or bo == 3 or bo == 5:
        break
    else:
        print("please insert best of 1 or 3 or 5!!!")

while True:
    score1 = int(input("Insert " + teamA + " score : "))
    score2 = int(input("Insert " + teamB + " score : "))
    total_score = score1 + score2
    if bo == 1:
        if (score1 == 1 or score2 == 1) and (total_score == 1):
            if score1 > score2:
                 print("===== The Winner is " + teamA + " =====")
            else:
                print("===== The Winner is " + teamB + " =====")
            break
    if bo == 3:
        if (score1 == 2 or score2 == 2) and (total_score == 3):
            if score1 > score2:
                print("===== The Winner is " + teamA + " =====")
            else:
                print("===== The Winner is " + teamB + " =====")
            break
    if bo == 5:
        if (score1 == 3 or score2 == 3) and (total_score == 5):
            if score1 > score2:
                print("===== The Winner is " + teamA + " =====")
            else:
                print("===== The Winner is " + teamB + " =====")
            break
    else:
        print("please enter correct score!!!")
