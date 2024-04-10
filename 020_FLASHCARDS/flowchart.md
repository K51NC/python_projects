# Flowchart

## User Flowchart

```mermaid
    A[Start] --> B[Show word to learn]
    B --> C[Card will reveal translation in 3 seconds]
    C --> D[User clicks 'Check' or 'X' button depending on if they got it correct or not]
    D --> |'check'| E[Take card out of rotation]
    D --> |'X' | F[Put card back in rotation]
    E --> G[check if all words have been learned]
    F --> G[check if all words have been learned]
    G --> |'no'| B
    G --> |'yes'| H[End]
```

## Technical Flowchart

```mermaid

```
