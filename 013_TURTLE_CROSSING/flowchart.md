# Flowchart

## User Flowchart

```mermaid

```

## Technical Flowchart

```mermaid
    A[Start] --> B[Create the screen]
    B --> C[Ask user for difficulty]
    C --> D[Create and init gameboard, player, cars list, lives remaining]
    D --> E[Set car speed and spawn rate]
    E --> F[Display "Get Ready", freeze player and populate initial cars]
    F --> G[Remove "Get Ready" and start round loop]
    G --> H[Unfreeze player, move player on key input]
    H --> I[Move cars]
    I --> J[Remove cars that have moved off screen]
    J --> K[Check for collision]
    K --> |yes| L[Reset player position, decrement lives remaining]
    K --> |no| M[Check for finish line collision]
    L --> N[Check for 0 lives remaining]
    M --> |yes| O[Stop round loop, display "You Win"]
    M --> |no| I[Move cars]
    N --> |yes| P[Stop round loop, display "Game Over"]
    N --> |no| I[Move cars]
    O --> Q[End Game]
    P --> Q[End Game]
```
