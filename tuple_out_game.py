import random
import seaborn as sns
import matplotlib.pyplot as plt

class TupleOutGame:
    def __init__(self, players, target_score=50):
        self.players = players
        self.target_score = target_score
        self.scores = {player: 0 for player in players}
        self.history = []  # Track scores per turn
        self.current_player_index = 0

    def play_turn(self, player):
        print(f"\n{player}'s turn!")
        dice = [random.randint(1, 6) for _ in range(3)]
        print(f"Roll: {dice}")
        
        counts = {x: dice.count(x) for x in set(dice)}
        if 3 in counts.values():
            print("Tuple Out! No points.")
            self.history.append((player, self.scores[player]))  # Add current score
            return 0

        total_score = sum(dice)
        self.scores[player] += total_score
        self.history.append((player, self.scores[player]))  # Add updated score
        return total_score

    def check_winner(self):
        for player, score in self.scores.items():
            if score >= self.target_score:
                return player
        return None

    def visualize_scores(self):
        # Convert history to usable data for Seaborn
        players = [entry[0] for entry in self.history]
        scores = [entry[1] for entry in self.history]
        turns = list(range(1, len(scores) + 1))

        # Plot the scores over turns
        plt.figure(figsize=(10, 6))
        sns.lineplot(x=turns, y=scores, hue=players)
        plt.title("Player Scores Over Turns")
        plt.xlabel("Turn Number")
        plt.ylabel("Total Score")
        plt.legend(title="Players")
        plt.show()

    def play_game(self):
        print(f"Welcome to Tuple Out! Target Score: {self.target_score}")
        while True:
            player = self.players[self.current_player_index]
            self.play_turn(player)

            winner = self.check_winner()
            if winner:
                print(f"Congratulations, {winner} wins with {self.scores[winner]} points!")
                self.visualize_scores()  # Show the visualization at the end
                break

            self.current_player_index = (self.current_player_index + 1) % len(self.players)

# Game setup
num_players = int(input("Enter the number of players: "))
players = [input(f"Enter name for Player {i + 1}: ") for i in range(num_players)]
game = TupleOutGame(players)
game.play_game()
