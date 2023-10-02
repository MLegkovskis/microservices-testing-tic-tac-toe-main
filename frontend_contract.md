
# Frontend Service Contract

## Base URL
`<Frontend-Service-URL>`

## Components

### 1. App.svelte
- Acts as a container, rendering the game board and game info.

### 2. Board.svelte
- Renders the game board and handles user interactions to make moves.

### 3. Dispatcher.svelte
- Fetches a random number from the backend and handles the UI for the same.

### 4. helpers.js
- Contains utility functions and classes to determine game status and represent game moves.

### 5. stores.js
- Manages the state and history of the game.

## Interactions

### 1. Board.svelte
- Interacts with the game state managed in `stores.js` to reflect and update the game status based on user interactions.

### 2. Dispatcher.svelte
- Makes a call to the `/number` endpoint of the backend service to fetch a random number.

## Dependencies
- Depends on the Flask application for the `/number` endpoint to get random numbers.
