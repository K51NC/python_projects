# Flowchart

## User Flowchart

## Technical Flowchart

```mermaid
    A[Start] --> B[create gameboard with color, size and boundaries]
    B --> C[create scoreboard]
    C --> D[create snake]
    D --> E[create food]
    E --> F[move snake]
    F --> G[control snake and constantly check for collision with boundaries, self, and food]
    G --> |collision with food| H[add to snake length and update score]
    G --> |collision with self or boundary| I[game over]
    H --> F
    I --> J[End]    
```
