# Research Center Quality Classification

## Overview
Machine learning project to classify UK research centers into quality tiers (Premium, Standard, Basic) using K-Means clustering and FastAPI.

## Project Structure
```
research-center-assignment/
├── app.py
├── cluster_model.pkl
├── requirements.txt
├── Dockerfile
├── docker-compose.yaml
├── .dockerignore
├── EDA_and_Model.ipynb
├── research_centers.csv
└── research_centers_clustered.csv
```

## How to Run

### Option 1 — With Docker (recommended)
```bash
docker compose up --build
```

### Option 2 — Without Docker
```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

## API Usage
POST `http://localhost:8000/predict`
```json
{
  "internalFacilitiesCount": 9,
  "hospitals_10km": 3,
  "pharmacies_10km": 2,
  "facilityDiversity_10km": 0.82,
  "facilityDensity_10km": 0.45
}
```

## Response
```json
{
  "predictedCluster": 1,
  "predictedCategory": "Premium"
}
```

## Quality Tiers
| Tier | Description |
|------|-------------|
| Premium | High internal facilities and strong healthcare access |
| Standard | Moderate facilities and average healthcare access |
| Basic | Low facilities and limited healthcare access |

## Tech Stack
- Python 3.10
- FastAPI
- Scikit-learn (K-Means)
- Docker
