# ACEest Fitness and Gym

## Setup and Run Locally

1. **Clone the repository:**

git clone https://github.com/kph27/ACEest_Fitness.git

cd ACEest_Fitness


2. **Create and activate a Python virtual environment:**

python3 -m venv venv

source venv/bin/activate


3. **Install required dependencies:**

pip install -r requirements.txt


4. **Run the Flask application:**

python app.py


5. **Access the application:**

Open your browser and visit: [http://localhost:5000](http://localhost:5000)

---

## Running Tests Locally

Run tests with Pytest:

pytest


This will execute the Pytest unit test cases to validate the API endpoints.

---

## GitHub Actions CI/CD Pipeline Overview

- A workflow is configured to automatically run on every push to the `main` branch.
- The pipeline performs:
  - **Automated Build:** Builds the Docker image for the application.
  - **Automated Testing:** Runs Pytest test cases to ensure code correctness.
- Successful completion of these steps ensures the app is valid before deployment.

You can see the pipeline runs under the **Actions** tab in this GitHub repository.

---

## Additional Information

- Dockerfile is included if you want to build and run the app in a container.
- For any issues, check GitHub Actions logs for detailed errors.

---

*Created by Prabhath Kattupalli for Introduction to DevOps Assignment 1.*
