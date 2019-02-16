# regex \[(\d+)-(\d+)-(\d+) (\d+):(\d+)] (\w+) #(\d+)
from datetime import datetime
import re
import operator

regex = "\[(\d+-\d+-\d+ \d+:\d+)] (wakes|falls|Guard) (\w+|#(\d+))"
entries = []

with open("./Input/day4.txt") as f:
    for line in f:
        entry = {}
        match = re.match(regex, line)
        entry['datetime'] = match.group(1)
        entry['type'] = match.group(2)
        if match.group(4):
            entry['guard_id'] = match.group(4)
        entries.append(entry)

sortedEntries = sorted(entries, key=lambda x: datetime.strptime(x['datetime'], '%Y-%m-%d %H:%M'))

guardsTotalSleepTime = {}
onMinutesAsleep = {}
currentGuard = 0
sleepyTime = ''
wakeyTime = ''

for entry in sortedEntries:
    entryType = entry['type']
    if entryType == 'Guard':
        if entry['guard_id'] not in guardsTotalSleepTime:
            guardsTotalSleepTime[entry['guard_id']] = 0
        
        currentGuard = entry['guard_id']
        sleepyTime = ''
        wakeyTime = ''
    elif entryType == 'falls':
        sleepyTime = entry['datetime']
    elif entryType == 'wakes':
        if currentGuard not in onMinutesAsleep:
            onMinutesAsleep[currentGuard] = {}


        wakeyTime = entry['datetime']
        d1 = datetime.strptime(wakeyTime, '%Y-%m-%d %H:%M')
        d2 = datetime.strptime(sleepyTime, '%Y-%m-%d %H:%M')
        for min in range(d2.minute, d1.minute):
            if min not in onMinutesAsleep[currentGuard]:
                onMinutesAsleep[currentGuard][min] = 1
            else:
                onMinutesAsleep[currentGuard][min] += 1

        timeAsleep = (d1 - d2)
        minutes = timeAsleep.total_seconds() / 60
        guardsTotalSleepTime[currentGuard] += minutes
        
guardMaxTimeAsleep = max(guardsTotalSleepTime.items(), key=operator.itemgetter(1))[0]
mostOnMinute = max(onMinutesAsleep[guardMaxTimeAsleep].items(), key=operator.itemgetter(1))[0]
print(mostOnMinute)
print(guardMaxTimeAsleep)
print('answer1: ' +  str(int(guardMaxTimeAsleep) * int(mostOnMinute)))

#part 2 of day 4
# guardsMax = {}
# for guard in onMinutesAsleep:
#     maxValues = [k for k, v in onMinutesAsleep[guard].items() if v == max(onMinutesAsleep[guard].values())]
#     guardMax = max(maxValues)
#     print(maxValues, guardMax, guard)
#     if guard not in guardsMax:
#         guardsMax[guard] = guardMax


print(guardsMax)

maxOnMinuteOfAllGuards = max(guardsMax.items(), key=operator.itemgetter(1))[0]
print("guard: " + str(maxOnMinuteOfAllGuards))
print("minute: " + str(guardsMax[maxOnMinuteOfAllGuards]))
print("answer2: " + str(int(maxOnMinuteOfAllGuards) * int(guardsMax[maxOnMinuteOfAllGuards])))