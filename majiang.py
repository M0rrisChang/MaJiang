# encoding: utf-8
import sys
money = [0, 0, 0, 0]
loss = [0, 0, 0, 0]
win = [0, 0, 0, 0]
lineCount = 0
lastLoser = lastWinner = totallyLoser = totallyWinner = maxLoseCombo = maxWinCombo = -1
tmpLoseCombo = tmpWinCombo = 0
for line in sys.stdin:
    if lineCount == 0:  #get players' names
        players = line
    else:
        i = 0
        for tmp in line.replace('\n', '').split(' '):
            money[i] += int(tmp)
            if int(tmp) < 0:
                loss[i] -= 1
                if lastLoser == i:
                    tmpLoseCombo += 1
                    if tmpLoseCombo > maxLoseCombo:
                        maxLoseCombo = tmpLoseCombo
                        totallyLoser = lastLoser
                else:
                    lastLoser = i
                    tmpLoseCombo = 1
            elif int(tmp) > 0:
                win[i] += 1
                if lastWinner == i:
                    tmpWinCombo += 1
                    if tmpWinCombo > maxWinCombo:
                        maxWinCombo = tmpWinCombo
                        totallyWinner = lastWinner
                else:
                    lastWinner = i
                    tmpWinCombo = 1
            i += 1
            i %= 4
    lineCount += 1

gameCount = lineCount - 1
print "         Total:", gameCount, "games"

for name in (players.replace('\n', '')).split(' '):
    print '{:>7}'.format(name),
print
for record in money:
    print '{0:7d}'.format(record),
print
print "              Losses"
for record in loss:
    print '{0:7d}'.format(record),
print
print "              Wins"
for record in win:
    print '{0:7d}'.format(record),
print
print "              Combo"
print "    ", maxLoseCombo, "losses, made by", (players.replace('\n', '')).split(' ')[totallyLoser]
print "    ", maxWinCombo, "wins, made by", (players.replace('\n', '')).split(' ')[totallyWinner]
