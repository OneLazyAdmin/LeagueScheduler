###Written by Face###

import requests
import json
apikey = '0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z'

url = "https://esports-api.lolesports.com/persisted/gw/getSchedule?hl=en-GB&leagueId=98767991302996019"

payload={}
headers = {'hl': 'en-US', 'x-api-key': '0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z'}

response = (requests.get(url, headers=headers, data=payload))
data = response.json()
schedule_pretty = json.dumps(data, indent=4)
schedule = json.dumps(data)

print(schedule_pretty)

with open('./schedule.json', 'w') as f:
   json.dump(schedule, f)


with open('./schedule_pretty.json', 'w') as f:
   json.dump(schedule_pretty.strip(), f)
print(schedule_pretty)
myEvents = data["data"]["schedule"]["events"]
print(myEvents)
#How to get the data
#for n_event in myEvents:
#    print(n_event["blockName"])
for n_event in myEvents:
    #if n_event["blockName"] =='Week 6':
        print(n_event["blockName"])
        print(n_event["match"]["teams"])
        team1 = n_event["match"]["teams"][0]["name"]
        team2 = n_event["match"]["teams"][1]["name"]
        result = n_event["match"]["teams"][0]["result"]["outcome"]
        if result == "win":
            winner = "Winner: " + team1
        elif result == "loss":
            winner = "Winner: " + team2
        elif result == None:
            winner = "Winner: TBD"
        print(team1 + " vs. " + team2)
        print(winner)





