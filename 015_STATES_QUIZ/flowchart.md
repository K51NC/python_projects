# Flowchart

## User Flowchart

```mermaid

```

## Technical Flowchart

```mermaid
    A[Start] --> B[Import Libraries]
    B --> C[Create Screen]
    C --> D[import data]
    D --> E[convert data to dictionary]
    E --> F[start stopwatch]
    F --> G[take user input]
    G --> H[check if input is in dictionary]
    H --> |yes| I[display state and remove from dictionary]
    H --> |no| G[take user input]
    I --> J[check if dictionary is empty]
    J --> |yes| K[win]
    J --> |no| G[take user input]
    K --> L[Display win message and time taken]
    L --> M[End]
```
