\# ml-app 🚀



Production-ready ML application with AWS CI/CD pipeline.



\## Features

\- ML model prediction

\- Dockerized application

\- CI/CD using AWS CodePipeline

\- ECS Fargate deployment

\- CloudWatch monitoring



\## API Endpoints



\### GET /

Health check



\### GET /health

Service status



\### POST /predict

Input:

{

&#x20; "features": \[1,2,3,4]

}



Output:

{

&#x20; "prediction": 1

}



\## Run Locally



```bash

pip install -r requirements.txt

python app.py

