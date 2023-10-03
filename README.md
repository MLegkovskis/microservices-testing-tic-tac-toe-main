# Tic Tac Toe Microservices Project

This project is a microservices-based implementation of the Tic Tac Toe game, utilizing Flask for the backend and Svelte for the frontend, orchestrated using Docker.

## Project Structure

### Microservices
1. **Frontend Service (Svelte):**
   - Responsible for rendering the game UI.
   - Located in the `/front` directory.
   - A placeholder test is included within this directory.

2. **Backend Service (Flask):**
   - Handles the game logic.
   - Located in the `/flask` directory.
   - Unit tests are included in `test_app.py` within this directory and are run during the Docker image build process.

3. **NGINX Service:**
   - Acts as a reverse proxy to route requests to the appropriate services.
   - Configuration can be found in `nginx.conf` and `nginx-lb.conf`.

### Directories
- **/front:** Contains the Svelte frontend service code and placeholder test.
- **/flask:** Contains the Flask backend service code and unit tests.
- **/tests:** Contains the contract tests written using the Pact framework.

### Testing
1. **Contract Tests:**
   - Located in the `/tests` directory.
   - Written using the Pact framework to define and verify interactions between services.

2. **Unit Tests:**
   - Backend (Flask) unit tests are located in `test_app.py` within the `/flask` directory.
   - These tests are executed during the Docker image build process to ensure code integrity before the container is run.
   - If you need to run the Flask unit tests manually, navigate to the `/flask` directory and execute the command: `python -m unittest test_app.py`.

## Getting Started

### Prerequisites
- Docker
- Docker Compose

### Running the Application

1. **Clone the Repository:**
   ```sh
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Build and Run the Services:**
   ```sh
   docker-compose up --build (on docker-compose.yml)
   ```

3. **Access the Application:**
   - Open a web browser and navigate to [http://localhost:8080](http://localhost:8080) to access the Tic Tac Toe game.

### Running Pact Tests

After the services are fully started and ready, you can manually run the Pact tests:

1. **Generate Consumer Pact:**
   - Execute the `consumer-pact.js` file inside the frontend container to generate the Pact contract file.
   ```sh
   docker exec -it <frontend_container_id_or_name> node src/consumer-pact.js
   ```

2. **Verify Provider Pact:**
   - Execute the `provider-pact.py` file inside the backend container to verify the generated Pact contract against the running Flask application.
   ```sh
   docker exec -it <backend_container_id_or_name> python3 flask/provider-pact.py
   ```

Make sure to replace `<frontend_container_id_or_name>` and `<backend_container_id_or_name>` with the actual container ID or name of your running frontend and backend containers, respectively.

### Fault Tolerance and Load Balancing

To experiment with fault tolerance and load balancing:

1. **Run the Load Balanced Services:**
   ```sh
   docker-compose -f docker-compose-lb.yml up --build
   ```

2. **Access the Application:** 
   - As before, navigate to [http://localhost:8081](http://localhost:8081) to access the game.

3. **Perform Chaos Experiments:**
   - To test fault tolerance and load balancing, you can stop one of the backend services and observe the behavior:
     ```sh
     docker stop backend1
     ```
   - Monitor how the load balancer handles requests when one of the backend services is down.

### Viewing Logs

- To view the logs of any service, use the `docker logs <service-name>` command. For example, to view the logs of the load balancer, run:
  ```sh
  docker logs nginx-lb
  ```
- To follow the logs in real-time, use the `-f` or `--follow` option:
  ```sh
  docker logs -f nginx-lb
  ```

---