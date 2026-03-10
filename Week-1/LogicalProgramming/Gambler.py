import random
stake = int(input("Enter Stake: "))
goal = int(input("Enter Goal: "))
trials = int(input("Enter Number of Trials: "))

wins = 0
bets = 0
for t in range(trials):
    cash = stake
    while cash > 0 and cash < goal:
        bets += 1
        if random.random() < 0.5: #505 win or lose
            cash += 1
        else:
            cash -= 1

    if cash == goal:
        wins += 1

losses = trials - wins
win_percent = (wins / trials) * 100
loss_percent = (losses / trials) * 100

print("Total Wins:", wins)
print("Total Losses:", losses)
print("Total Bets Made:", bets)
print("Win Percentage:", win_percent, "%")
print("Loss Percentage:", loss_percent, "%")
