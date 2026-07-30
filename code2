# Sample data: dictionary of players
players = {
    "Player A": {"runs": 450, "balls_faced": 300, "wickets": 2},
    "Player B": {"runs": 620, "balls_faced": 380, "wickets": 0},  # Highest Runs
    "Player C": {"runs": 150, "balls_faced": 90, "wickets": 15},  # Highest Wickets
    "Player D": {"runs": 280, "balls_faced": 200, "wickets": 5}
}

# 1. Calculate Strike Rate & add it to the dataset
# Formula: (Runs / Balls Faced) * 100
for name, stats in players.items():
    if stats["balls_faced"] > 0:
        stats["strike_rate"] = (stats["runs"] / stats["balls_faced"]) * 100
    else:
        stats["strike_rate"] = 0.0

# 2. Find Orange Cap (Most Runs) and Purple Cap (Most Wickets)
orange_cap_winner = max(players, key=lambda p: players[p]["runs"])
purple_cap_winner = max(players, key=lambda p: players[p]["wickets"])

# 3. Rank players by runs (highest to lowest)
ranked_players = sorted(players.items(), key=lambda item: item[1]["runs"], reverse=True)

# Display Results
print("--- CRICKET PLAYER STATISTICS ---")
print(f"Orange Cap Winner (Most Runs): {orange_cap_winner} ({players[orange_cap_winner]['runs']} runs)")
print(f"Purple Cap Winner (Most Wickets): {purple_cap_winner} ({players[purple_cap_winner]['wickets']} wickets)")

print("\nPlayers with Strike Rate above 150:")
high_sr_found = False
for name, stats in players.items():
    if stats["strike_rate"] > 150:
        print(f"  - {name}: {stats['strike_rate']:.2f}")
        high_sr_found = True
if not high_sr_found:
    print("  - None")

print("\nPlayer Rankings (By Runs):")
for rank, (name, stats) in enumerate(ranked_players, start=1):
    print(f"  {rank}. {name} — Runs: {stats['runs']}, SR: {stats['strike_rate']:.2f}, Wickets: {stats['wickets']}")
