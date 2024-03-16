# Flowcharts

## Technical Flowchart

```mermaid
[Create or load high scores file]
[create or update imdb ratings file]
[create or load player information from scores file]
[get two random movies from the imdb ratings file]
[show current high score to beat]
[ask player to guess which movie has the higher rating]
[check if the player's guess is correct]
|yes| [update player score]
|no| [end game and update high scores file]
[show the high scores file to the player]
[ask player if they want to play again]
|yes| [reset player score and go back to "get two random movies from the imdb ratings file"]
|no| [end game]
```

## User Flowchart

```mermaid
[Start]
[Pick which movie of the two has the higher rating]
[Check if the player's guess is correct]
    |yes| [Show the player their updated score]
    |no| [End game and update high scores]
[Ask the player if they want to play again]
    |yes| [Score is reset and go back to "Pick which movie of the two has the higher rating"]
    |no| [End game and show the player the high scores]
```
