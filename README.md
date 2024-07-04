# Game Data Management API

## AWS Deployment

The application is deployed on AWS EC2. Due to security measures, the live link requires updated session credentials. Please contact me at `abhishek.balram@icloud.com` for access to the live demo.

## Project Overview

This project is a RESTful API built with Python and Flask for managing game data. It's containerized with Docker and deployed on AWS EC2, utilizing AWS DynamoDB for data storage. This showcase demonstrates proficiency in backend development, cloud technologies, and DevOps practices. I'm always open to discussing the technical details and design decisions behind this implementation. Please contact at `abhishek.balram@icloud.com`

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

## Setup and Deployment

1. Clone the repository
2. Set up AWS credentials in a `.env` file
3. Build the Docker image:
   ```
   docker build -t game-data-api .
   ```
4. Run the Docker container:
   ```
   docker run -d -p 5000:5000 --restart unless-stopped game-data-api
   ```


## Future Enhancements

- Implement user authentication and authorization
- Add more game-specific endpoints (e.g., leaderboards, achievements)
- Integrate with a CI/CD pipeline for automated testing and deployment
- Implement caching for improved performance
- Build a frontend to make requests and visualise data

## Contact

For more information or to request access to the live demo, please contact  at `abhishek.balram@icloud.com`.


