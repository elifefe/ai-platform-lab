# AI Platform Lab

I built this project to understand what actually happens around an AI application once the model itself is done.

I wanted to learn how to take a ML model and turn it into something that can be tested, containerized, automatically validated and finally deployed to the cloud.

So instead of focusing on building the most complex AI model possible, I focused on the engineering around it.

The result is a  **FastAPI prediction API** using **scikit-learn**, **Docker**, **GitHub Actions**, **Render** and **Terraform**.



## Live Demo

The API is currently deployed on Render:

**API:** https://ai-platform-lab.onrender.com  
**Swagger UI:** https://ai-platform-lab.onrender.com/docs



## How it works

```text
                    GitHub
                       │
                  Push to main
                       │
                       ▼
               GitHub Actions
                ┌──────┴──────┐
                ▼             ▼
             pytest       Docker Build
                │             │
                └──────┬──────┘
                       │
                       ▼
                  Render Cloud
                       │
                       ▼
                 Docker Container
                       │
                       ▼
                    FastAPI
                       │
                 POST /predict
                       │
                       ▼
             scikit-learn Model
                       │
                       ▼
                   Prediction
```



## Tech Stack

- Python 3.12
- FastAPI
- Pydantic
- scikit-learn
- pytest
- Docker
- Git & GitHub
- GitHub Actions
- Render
- Terraform

## Machine-Learning-Modell 

I trained a  **Linear Regression** model with example data connecting study hours and test scores.

For example:

```json
{
  "hours_studied": 4.5
}
```

produces:

```json
{
  "hours_studied": 4.5,
  "predicted_score": 64.88
}
```


##  API

The application has two endpoints.

### `GET /`

A simple root endpoint:

```json
{
  "Hello": "World"
}
```

### `POST /predict`

Takes the number of study hours and sends it to the ML model.

Example request:

```json
{
  "hours_studied": 4.5
}
```

FastAPI and Pydantic handle the API and request validation, while scikit-learn handles the prediction.

FastAPI also automatically provides interactive Swagger documentation under:

```text
/docs
```

## Testing

I use **pytest** and FastAPI's `TestClient` to test both endpoints.

Currently the tests check:

- whether the root endpoint responds correctly
- whether `/predict` accepts the input
- whether the API returns `200 OK`
- whether the expected prediction is returned

---

## Docker

One of the things I specifically wanted to understand was the difference between an application simply working on my Mac and having a reproducible environment.

That's where Docker comes in.

Build the image:

```bash
docker build -t ai-platform-lab .
```

Run the container:

```bash
docker run -p 8080:8000 ai-platform-lab
```

The API is then available at:

```text
http://localhost:8080
```


## CI with GitHub Actions

Every push to `main` automatically starts my GitHub Actions workflow.

The workflow:

1. checks out the repository
2. sets up Python
3. installs the dependencies
4. runs the tests
5. builds the Docker image

This was probably one of my favorite parts of the project because it made the idea behind CI much clearer to me.

Instead of only knowing that everything works on my machine, the project is tested again on a fresh Ubuntu runner.

I also got to debug my first failed CI run. The application and tests were fine, but Docker Hub returned an HTTP 500 error while the runner tried to pull the Python base image.

After checking the logs and identifying it as an external registry issue, rerunning the job completed successfully. 



## Cloud Deployment

After everything worked locally and in CI, I deployed the Dockerized application to **Render**.

That was the point where the project went from:

> "It works on my Mac."

to:

> "Okay, this thing is actually running somewhere else." 

The API can now be accessed publicly and the prediction endpoint can be tested directly through Swagger.



## Terraform

The last part I wanted to explore was **Infrastructure as Code**.

I used Terraform with the Render provider and imported my existing Render web service into Terraform state.

This also gave me a very useful lesson in why `terraform plan` matters.

At one point my Terraform configuration specified:

```hcl
region = "frankfurt"
```

while the existing service was actually running in:

```hcl
region = "oregon"
```


## Project Structure

```text
ai-platform-lab/
├── .github/
│   └── workflows/
│       └── ci.yml
├── Dockerfile
├── README.md
├── main.py
├── model.py
├── main.tf
├── requirements.txt
└── test_main.py
```
