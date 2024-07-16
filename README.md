# Game Data Management API

## Project Overview
This project is a RESTful API built with Python and Flask for managing game data. It's containerized with Docker and designed to be deployed on AWS EC2, utilizing AWS DynamoDB for data storage. This showcase implements backend development, cloud technologies, and DevOps practices. I'm always open to discussing the technical details and design decisions behind this implementation. Please contact at `abhishek.balram@icloud.com`

## Key Features
- RESTful API for game data management
- Player and score data handling
- Docker containerization
- Designed for AWS EC2 deployment
- AWS DynamoDB integration
- Environment variable management for secure credential handling
- Separate frontend and API structure

## Technology Stack
- **Backend (API)**: Python 3.12, Flask, Flask-RESTful
- **Frontend**: HTML, CSS, JavaScript
- **Database**: AWS DynamoDB
- **Containerization**: Docker, Docker Compose
- **Cloud Platform**: Designed for AWS EC2 (not yet deployed)
- **Additional Libraries**: boto3 for AWS SDK, python-dotenv for environment management

## Project Structure
```
project_root/
│
├── api/
│   ├── app.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── script.js
│
├── Dockerfile
└── docker-compose.yml
```

## API Endpoints
1. **Players**
   - GET /players - Retrieve all players
   - POST /players - Create a new player
   - GET /players/<player_id> - Retrieve a specific player
   - PUT /players/<player_id> - Update a player's data
2. **Scores**
   - GET /scores/<player_id> - Retrieve a player's score
   - PUT /scores/<player_id> - Update a player's score

## AWS Setup
1. Create an IAM user:
   - Log in to the AWS Management Console
   - Navigate to IAM (Identity and Access Management) and create a new user for programmatic access
   - Attach the necessary policies (e.g., AmazonDynamoDBFullAccess)
   - Complete the user creation process
   - **Important**: Save the Access Key ID and Secret Access Key securely

2. Set up environment variables:
   - Create a `.env` file in your `api` directory
   - Add the following lines:
     ```
     AWS_ACCESS_KEY_ID=your_access_key_id
     AWS_SECRET_ACCESS_KEY=your_secret_access_key
     AWS_DEFAULT_REGION=your_aws_region
     ```
   - Replace `your_access_key_id`, `your_secret_access_key`, and `your_aws_region` with your actual AWS credentials and preferred region

## Local Setup
1. Clone the repository
2. Set up AWS credentials in a `.env` file as described above
3. Ensure Docker and Docker Compose are installed on your system
4. Build and run the Docker containers:
   ```
   docker compose up --build
   ```
5. Access the application:
   - Frontend: http://localhost:8080
   - API: http://localhost:5001

6. To stop the application:
   ```
   docker compose down
   ```

## Testing the API
Once the containers are running, you can test the API using curl commands or through the frontend interface. Here are some curl examples:

a. Test the root endpoint:
```
curl http://localhost:5001/
```
Expected output: "Hello! This is a Docker application"

b. Create a new player:
```
curl -X POST -d "data=Player1Data" http://localhost:5001/players
```
Expected output: A JSON object with a new player ID and the data you provided

c. Get all players:
```
curl http://localhost:5001/players
```
Expected output: A JSON object with all players and their data

d. Update a player's score (replace <player_id> with an actual player ID):
```
curl -X PUT -d "score=100" http://localhost:5001/scores/<player_id>
```
Expected output: A JSON object with the player ID and the new score

e. Get a player's score:
```
curl http://localhost:5001/scores/<player_id>
```
Expected output: A JSON object with the player ID and their score

Note: This setup uses the production database even for local testing. Be cautious about the data you input during testing.

## Future Enhancements
- Improve the frontend to more fully utilise the API endpoints 
- Deploy the updated version with frontend to AWS EC2
- Secure environment variables in production, using one of these options:
   a. Use AWS Secrets Manager to store secrets, and modify app to retrieve them at runtime.
   b. Use IAM roles instead of hardcoding AWS credentials when deployed on EC2.
- Implement user authentication and authorization
- Add more game-specific endpoints (e.g., leaderboards, achievements)
- Integrate with a CI/CD pipeline for automated testing and deployment
- Implement caching for improved performance
- Build a simple game that can be played in the web browser, to obtain real data to use with the API

## Contact
For more information or to discuss this project further, please contact at `abhishek.balram@icloud.com`.