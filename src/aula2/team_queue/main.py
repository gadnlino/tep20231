testn = 0

while True:

    testn += 1

    nteams = int(input())

    if(nteams == 0):
        break

    team_queue = []
    teams_orders = []
    member_to_team = {}

    for __ in range(0, 1000):
        team_queue.append([])

    for i in range(0, nteams):
        team = list(map(lambda x : int(x), str(input()).split(" ")[1:]))

        for tm in team:
            member_to_team[tm] = i

    print(f'Scenario #{testn}')

    while True:
        operations = str(input()).split(" ")

        if(operations[0] == "STOP"):
            break
        elif (operations[0] == "ENQUEUE"):
            ele = int(operations[1])
            team_ele = member_to_team[ele]

            team_queue[team_ele].insert(0, ele)

            if(team_ele not in teams_orders):
                teams_orders.insert(0, team_ele)
        elif (operations[0] == "DEQUEUE"):
            next_team = teams_orders[len(teams_orders)-1]
            #print('next_team', next_team)
            next_ele = team_queue[next_team][len(team_queue[next_team])-1]

            print(next_ele)

            team_queue[next_team].pop()

            if(len(team_queue[next_team]) == 0):
                team_queue.pop(0)
    
    print()