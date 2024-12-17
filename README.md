# Tuple Out Dice Game

A turn-based dice game where players accumulate points while avoiding "Tuple Out". The first player to reach the target score wins.

## How to Run

- Ensure Python is installed on your computer.
- Install required libraries:
  ```
  pip install seaborn matplotlib
  ```
- Run the game:
  ```
  python tuple_out_game.py
  ```
- Follow the prompts to play the game.

## Features

- **Turn-Based Scoring**: Players roll dice to score points. Fixed dice cannot be rerolled.
- **Tuple Out Rule**: If all three dice show the same value, the player scores zero for the turn.
- **Score Visualization**: At the end of the game, a line chart displays each player's scores over the turns using Seaborn.
- **Game History Tracking**: Records and displays the scores for every turn.

## Example Gameplay

1. **Player 1** rolls `2, 2, 4`:  
   - Fixed `2`s, rerolls `4`, and scores `2 + 2 + 3 = 7` points.  

2. **Player 2** rolls `5, 5, 5`:  
   - "Tuple Out!" Scores `0` points.  

3. **Player 3** rolls `1, 4, 6`:  
   - Rerolls all, fixes `2, 2`, scores `2 + 2 + 5 = 9` points.  
