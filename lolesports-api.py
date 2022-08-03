###Written by Face###

import requests
import json

# non-changing variables
apikey = '0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z'


# print(schedule_pretty)

# with open('./schedule.json', 'w') as f:
#    json.dump(schedule_file, f)

# with open('./schedule_pretty.json', 'w') as f:
#    json.dump(schedule_pretty.strip(), f)
# print(schedule_pretty)


# print(myEvents)
# How to get the data
# for n_event in myEvents:
#    print(n_event["blockName"])

def get_schedule():
    url = "https://esports-api.lolesports.com/persisted/gw/getSchedule?hl=en-GB&leagueId=98767991302996019"

    payload = {}
    headers = {'hl': 'en-US', 'x-api-key': '0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z'}

    response = (requests.get(url, headers=headers, data=payload))
    data = response.json()
    schedule_pretty = json.dumps(data, indent=4)
    schedule_file = json.dumps(data)
    print(data)
    my_events = data["data"]["schedule"]["events"]
    schedule = []
    for n_event in my_events:
        # if n_event["blockName"] =='Week 6':
        start_time = n_event["startTime"].split("T")[1].split("Z")[0]
        week = n_event["blockName"].split(" ")[1]
        print(week)
        # print(n_event["match"]["teams"])
        team1 = n_event["match"]["teams"][0]["name"]
        team2 = n_event["match"]["teams"][1]["name"]
        result = n_event["match"]["teams"][0]["result"]["outcome"]
        if result == "win":
            winner = team1
        elif result == "loss":
            winner = team2
        elif result is None:
            winner = "TBD"
        match = team1 + " vs. " + team2
        # print(team1 + " vs. " + team2)
        print(winner)
        temp = {"week": week, "match": match, "winner": winner, "startTime": start_time}
        schedule.append(temp)
    print(schedule)


get_schedule()
