
# Backend Service Contract

## Base URL
`<Backend-Service-URL>`

## Endpoint

### 1. Get Random Number
- **Path:** `/number`
- **Method:** `GET`
- **Description:** Returns a random number between 0 and 8.
- **Response Format:** Plain text representing the generated number.
- **Consumed By:** `Dispatcher.svelte` in the Frontend Application to get a random number.
