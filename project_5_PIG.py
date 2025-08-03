# multiplayer game
# gameplay
"""
Each turn, a player repeatedly rolls a die until a 1 is rolled or the player decides to "hold":

. If the player rolls a 1, they score nothing and it becomes the next player's turn.

. If the player rolls any other number, it is added to their turn total and the player's turn continues.

. If a player chooses to "hold", their turn total is added to their score, and it becomes the next player's turn.

The first player to score 100 or more points wins.

For example, the first player, Donald, begins a turn and rolls a 5. Donald could hold and score 5 points, but chooses to roll again. Donald rolls a 2, and could hold with a turn total of 7 points, but chooses to roll again. Donald rolls a 1, and must end his turn without scoring. The next player, Alexis, rolls the sequence 4, 5, 3, 5, 6, after which she chooses to hold, and adds her turn total of 23 points to her score."""

from random import randint

# Step 1: Get number of players (between 2 and 4)
while True:
    try:
        players = int(input("Enter number of players (2 to 4): "))
        if players < 2 or players > 4:
            print("Number of players must be between 2-4.")
        else:
            break
    except ValueError:
        print("Enter a valid number!")

# Step 2: Initialize scores
max_score = 50
player_score = {}

for i in range(1, players + 1):
    player_name = f"Player {i}"
    player_score[player_name] = 0  # Start all players at 0

# Step 3: Play game in rounds
winner = None
round_num = 1

print("\n🎯 Game Started! First to reach 50 wins.\n")

while not winner:
    print(f"--- Round {round_num} ---")
    
    for player in player_score:
        input(f"{player}, press Enter to roll the dice...")
        dice_roll = randint(1, 6)
        player_score[player] += dice_roll
        print(f"{player} rolled {dice_roll} -> Total: {player_score[player]}")

        if player_score[player] >= max_score:
            winner = player
            break
    
    # 🧾 Leaderboard after each round
    if not winner:
        print("\n📊 Leaderboard after Round", round_num)
        sorted_scores = sorted(player_score.items(), key=lambda x: x[1], reverse=True)
        for rank, (pname, pscore) in enumerate(sorted_scores, start=1):
            print(f"{rank}. {pname} - {pscore} points")
            
    round_num += 1
    print("")  # Blank line between rounds

# Step 4: Declare Winner
print(f"🏆 {winner} wins the game with {player_score[winner]} points!")

# ✅ Final Leaderboard
print("\n🎉 Final Leaderboard")
sorted_scores = sorted(player_score.items(), key=lambda x: x[1], reverse=True)
for rank, (pname, pscore) in enumerate(sorted_scores, start=1):
    print(f"{rank}. {pname} - {pscore} points")