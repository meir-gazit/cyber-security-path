import random

# Get player's input and checksn it is valid choice
def get_player_choice(player_name):
    choices = ["rock", "paper", "scissors"]
    while True:
        try:
            choice = input(f"{player_name}, enter your choice (rock/paper/scissors): ").lower()
            if choice in choices:
                return choice
            else:
                raise ValueError("Invalid choice. Please enter rock, paper, or scissors.")
        except ValueError as e:
            print(e)

# Logic to see how won based on players choice.
def play_round(player1, player2):
    
    if player1 == player2:
        return "It's a tie!"
    elif (player1 == "rock" and player2 == "scissors") or \
         (player1 == "scissors" and player2 == "paper") or \
         (player1 == "paper" and player2 == "rock"):
        return f"{player1} wins!"
    else:
        return f"{player2} wins!"

# Display the current scores of the players.
def display_scores(scores):
    print("\n--- Scores ---")
    for player, score in scores.items():
        print(f"{player}: {score}")
    print("---------------\n")

# Saving the players scores
def save_scores(scores):
    try:
        with open("scores.txt", "w") as file:
            for player, score in scores.items():
                file.write(f"{player}:{score}\n")
        print("Scores saved successfully.")
    except IOError as e:
        print(f"Error saving scores: {e}")

# Loading player scores.
def load_scores():
    try:
        with open("scores.txt", "r") as file:
            scores = {}
            for line in file:
                player, score = line.strip().split(":")
                scores[player] = int(score)
            print("Scores loaded successfully.")
            return scores
    except FileNotFoundError:
        print("No previous scores found.")
        return {}
    except IOError as e:
        print(f"Error loading scores: {e}")
        return {}

def main():
    
	# Menu of choices: play against the computer or anther player, get player name.
    print("Welcome to Rock, Paper, Scissors!")
    player_mode = input("Do you want to play against the computer or another player? (1/2): ")
    
    if player_mode == "1":
        player_name = input("Enter your name: ")
        computer_name = "Computer"
    elif player_mode == "2":
        player_name = input("Enter Player 1's name: ")
        computer_name = input("Enter Player 2's name: ")
    else:
        print("Invalid choice. Exiting...")
        return

	# Vars init.
    scores = load_scores()
    win_count = 0
    best_of_3 = 0

    while True:
        
		# Get first player choice.
        player1_choice = get_player_choice(player_name)

		# Andles the logic for obtaining the computer's or the second player's choice.
        if player_mode == "1":
            # Using the random library to get the computer choice.
            computer_choice = random.choice(["rock", "paper", "scissors"])
        else:
            player2_choice = get_player_choice(computer_name)
            computer_choice = player2_choice

		# The computer's or the second player's choice.
        result = play_round(player1_choice, computer_choice)
        print(result)

		# Tracking wins and determining when to display the "best out of 3" result.
        if "wins" in result:
            win_count += 1

        best_of_3 += 1

        if best_of_3 == 3:
            print(f"\n{player_name}'s Win Count: {win_count}")
            best_of_3 = 0
            win_count = 0
		
		# Function that takes a dictionary scores as an argument. 
        # This dictionary is assumed to contain player names as keys and their respective scores as values.
        display_scores(scores)
        
		# Exit point: If the user chooses not to play again,
		# save scores and break out of the loop to end the program.		
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            save_scores(scores)
            break

# Run as the main program
if __name__ == "__main__":
    main()
