
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

kmeans, scaler, selected_features, cluster_to_tier = joblib.load("cluster_model.pkl")

app = FastAPI(
    title="Research Center Quality Classifier",
    description="Classifies research centers into Premium, Standard, or Basic categories",
    version="1.0.0"
)

class ResearchCenterInput(BaseModel):
    internalFacilitiesCount: float
    hospitals_10km: float
    pharmacies_10km: float
    facilityDiversity_10km: float
    facilityDensity_10km: float

@app.post("/predict")
def predict_quality(data: ResearchCenterInput):
    try:
        input_df = pd.DataFrame([data.dict()])
        input_df = input_df[selected_features]
        X_scaled = scaler.transform(input_df)
        cluster_label = kmeans.predict(X_scaled)[0]
        tier = cluster_to_tier.get(cluster_label, "Unknown")
        return {"predictedCluster": int(cluster_label), "predictedCategory": tier}
    except Exception as e:
        return {"error": str(e)}
