import json
from datetime import datetime

if __name__ == "__main__":
    fname = "leaderboard.json"
    with open(fname, "r") as f:
        data = json.load(f)
    members = data["members"]
    for k in members.keys():
        m = members[k]
        name = m['name']
        stars = m['stars']
        days = m['completion_day_level']
        for i in range(1,26):
            istr = str(i)
            if istr in days.keys():
                print(name,'\tDay',istr,end='')
                if '1' in days[istr].keys():
                    d = days[istr]['1']
                    print('\tPart 1:',datetime.fromtimestamp(int(d['get_star_ts'])),end='')
                if '2' in days[istr].keys():
                    d = days[istr]['2']
                    print('\tPart 2:',datetime.fromtimestamp(int(d['get_star_ts'])),end='')
                print()