# Blackjack

## 3-2-2024

**NOT A WORKING VERSION YET.**

I made this much more extensive than the "100 days of code" assigned project on purpose. This allows me to improve my Python problem solving. I also wanted to practice better organization and documentation with markdown and mermaid for flow charts. I should be able to finish this project in the next few days.

Initial code commit. Udemy 100 days of code. Practice with:

* markdown formatting (this document compared to my previous ones is much more detailed, organized and readable)
* deepcopy
* manipulating nested dictionaries in dictionaries
* manipulating nested lists in dictionaries

### **Flow Chart:**

```mermaid
graph TD;
    A[Start of Round] --> Build Title;
    Build Title --> B[How Many Players?];
    B --> C[Players Purchases Chips];
    C --> D[Player Bets];
    D --> E[Deal Players and Dealer 2 Cards];
    E --> F[Show Players Their Cards and Dealer's Second Dealt Card];
    F --> G[Check for Dealer Blackjack];
    G --> |no| I[Player Turn];
    G --> |yes| H[players with blackjack get their bet back, all others lose their bet];
    H --> U[End of Round];
    I --> J[Check for player blackjack];
    J --> |no| L[Player 'h' or 's'];
    J --> |yes| K[Player Wins their bet + 1.5x their bet];
    K --> O[All Players Done?];
    L --> |'h'| M[Deal Another Card and Check for Bust];
    L --> |'s'| O[All Players Done?];
    M --> |no| L;
    M --> |yes| N[Player Busts and Loses Bet];
    O --> |no| I;
    O --> |yes| P[Check if all players bust];
    P --> |yes| U[End of Round];
    P --> |no| Q[Dealer Turn];
    Q --> |<17| Q[Dealer Must Hit];
    Q --> |>=17| S[Dealer Must Stop];
    Q --> |>21| S[Dealer Busts and must stop];
    S --> T[Compare Dealer score to each player and Declare Winners];
    T --> |player wins| [Payout players 2x their bet];
    T --> |dealer wins| [Player loses their bet];
    T --> |push| [Player keeps their bet];
    U[End of Round] --> V[Ask if players want to play again];
    V --> |yes| C[Players Purchases Chips];
    V --> |no| W[Display Chip Balance for Each Player and say goodbye];
    W --> X[End of game];
```

### **Rules:**

* Value cards are face value, 'A' can be 1 or 11, all other face cards are 10 points each (J, Q, K)

* Highest to 21 without going over wins

* Player can hit as many times as they wish without going over 21 or stand whenever they want to stop hitting and let the other players and dealer play out their hand

* If player gets blackjack (21 on first 2 cards), they win 1.5x their bet

* If dealer gets blackjack, all players lose their bet unless they also have blackjack, then it's a push

* If player busts (>21), they lose their bet and are out of the round

* If dealer busts, all players still in the round win their bet

* If dealer and player have the same score, player keeps their bet unless previously busted

* Dealer must hit if < 17, must stop if >= 17 (unless all players bust before dealer's turn)

### **Add in Future:**

1. blackjack payout?
2. surrender option?
3. split option?
4. double down?
5. insurance?
6. AI for computer player?
    1. betting strategy?
    2. hit/stand strategy?
7. betting limits?

### **To-Do:**

1. Error handling for invalid bets
2. Error handling for invalid player count
3. Error handling for invalid chip count
4. Error handling for invalid player names
5. Error handling for invalid player actions
6. Error handling for invalid player bets
7. Fix value of "A" card to be 1 or 11 (currently only 11)
8. Move all functions to a different .py file (I'll have to look this up)
9. Polish up the code and make it more appealing during gameplay

### **Bugs:**

* None
