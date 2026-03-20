# Research Center Quality Classification

A machine learning project that classifies UK research centers into quality tiers based on internal infrastructure and access to external healthcare services.

## What This Project Does

Given information about a research center such as how many internal facilities it has and how many hospitals or pharmacies are nearby, this system automatically classifies it into one of three quality tiers:

**Premium** — Well-equipped centers with excellent healthcare access

**Standard** — Moderately equipped centers with average healthcare access

**Basic** — Limited facilities with minimal healthcare access

This is useful for funding bodies, researchers, and healthcare organisations to quickly assess and compare research center quality across UK cities.

## How It Works

1. Exploratory Data Analysis to understand patterns in the data across UK cities
2. Feature Selection to identify the most important indicators of quality
3. K-Means Clustering to group centres into 3 tiers without labelled data
4. FastAPI Deployment to serve the model as a REST API endpoint
5. Docker to containerise the entire application for easy deployment

## Project Structure
```
research-center/
├── app.py                          # FastAPI application
├── cluster_model.pkl               # Trained K-Means model
├── requirements.txt                # Python dependencies
├── Dockerfile                      # Docker build instructions
├── docker-compose.yaml             # Docker Compose configuration
├── .dockerignore                   # Files excluded from Docker image
├── EDA_and_Model.ipynb             # Full analysis and model training
├── research_centers.csv            # Original dataset
└── research_centers_clustered.csv  # Dataset with predicted tiers
```

## Getting Started

**Option 1: Run with Docker (Recommended)**

Make sure Docker is installed, then run:
```bash
docker compose up --build
```

**Option 2: Run Locally Without Docker**
```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

The API will be available at `http://localhost:8000`

## API Usage

Endpoint: `POST http://localhost:8000/predict`

Example Request:
```json
{
  "internalFacilitiesCount": 9,
  "hospitals_10km": 3,
  "pharmacies_10km": 2,
  "facilityDiversity_10km": 0.82,
  "facilityDensity_10km": 0.45
}
```

Example Response:
```json
{
  "predictedCluster": 1,
  "predictedCategory": "Premium"
}
```

Once running, visit `http://localhost:8000/docs` for the full interactive Swagger UI.

## Dataset

The dataset contains synthetic data representing research centers across UK cities. Each record includes:

| Feature | Description |
|---|---|
| `internalFacilitiesCount` | Number of internal labs and workstations |
| `hospitals_10km` | Number of hospitals within 10km |
| `pharmacies_10km` | Number of pharmacies within 10km |
| `facilityDiversity_10km` | Diversity index of nearby facilities (0-1) |
| `facilityDensity_10km` | Density of nearby facilities per area |

## Tools and Technologies

- Python 3.10 as the core language
- FastAPI to build and serve the REST API
- Scikit-learn for K-Means clustering and model evaluation
- Pandas and NumPy for data processing and analysis
- Docker to containerise and deploy the application
- Joblib to save and load the trained model

## Author

Rasheed Rashid
