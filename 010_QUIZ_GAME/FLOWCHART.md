# Flowcharts

## User Flowchart

```mermaid
    A[Start] --> B[User selects a category]
    B --> C[User selects a difficulty]
    C --> D[Ask user how many questions they want to answer]
    D --> E[Question is asked to user]
    E --> F[User answers the question]
    F --> G{User is correct?}
    G --> |Yes| H[User earns points]
    G --> |No| H[User does not earn points]
    H --> J[Are all questions answered?]
    J --> |Yes| K[User wants to play again?]
    J --> |No| E
    K --> |Yes| B
    K --> |No| L[End]
```

## Technical Flowchart
