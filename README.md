# Game Data Management API

## AWS Deployment

The application is deployed on AWS EC2. Due to security measures, the live link requires updated session credentials. Please contact me at `abhishek.balram@icloud.com` for access to the live demo.

## Project Overview
This project is a RESTful API built with Python and Flask for managing game data. It's containerized with Docker and deployed on AWS EC2, utilizing AWS DynamoDB for data storage. This showcase implements backend development, cloud technologies, and DevOps practices. I'm always open to discussing the technical details and design decisions behind this implementation. Please contact at `abhishek.balram@icloud.com`

## Key Features
- RESTful API for game data management
- Player and score data handling
- Docker containerization
- AWS EC2 deployment
- AWS DynamoDB integration
- Environment variable management for secure credential handling

## Technology Stack
- **Backend**: Python 3.12, Flask, Flask-RESTful
- **Database**: AWS DynamoDB
- **Containerization**: Docker
- **Cloud Platform**: AWS EC2
- **Additional Libraries**: boto3 for AWS SDK, python-dotenv for environment management

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
   - Create a `.env` file in your project root
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
3. Build the Docker image:
   ```
   docker build -t game-data-api .
   ```
4. Run the Docker container:
   ```
   docker run -it -p 5001:5000 game-data-api
   ```
5. Test the API:
   Once the container is running, you can test the API using curl commands. Here are some examples:
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
   d. Update a player's score (replace <player_id> with the ID from step b):
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

## AWS Deployment
The application is currently deployed on AWS EC2. For security reasons, the live link has been temporarily omitted. I plan to make the application publicly accessible after implementing additional security measures, contact me at `abhishek.balram@icloud.com` for early access.

## Future Enhancements
- Implement user authentication and authorization
- Add more game-specific endpoints (e.g., leaderboards, achievements)
- Integrate with a CI/CD pipeline for automated testing and deployment
- Implement caching for improved performance
- Build a frontend to make requests and visualise data

## Contact
For more information or to request access to the live demo, please contact at `abhishek.balram@icloud.com`.