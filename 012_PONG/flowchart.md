# Flowchart

## User Flowchart

## Technical Flowchart

```mermaid
    A[Start] --> B[Create and initialize Screen, Paddle, Ball, Boundary, Scoreboard, and Countdown timer]
    B --> C[Select player to start serving and begin countdown timer]
    C --> D[Move the ball]
    D --> E[Check for collisions with paddles and boundaries]
    E --> |Paddle| G[Change ball 'x' direction]
    E --> |Top/Bottom boundary| H[Change ball 'y' direction]
    E --> F[Check for ball collision past paddle]
    F --> |No| C
    F --> |Yes| I[Update scoreboard]
    G --> C
    H --> C
    I --> J[Check for winner]
    J --> |No| K[Reset ball]
    J --> |Yes| M[Announce winner]
    K --> L[Select round winner to serve]
    L --> C
    M --> N[End Game]
```
