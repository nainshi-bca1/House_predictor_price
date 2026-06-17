import pickle
import joblib
import sklearn
# Load old pickle
with open("RidgeModel.pkl", "rb") as f:
    model = pickle.load(f)

# Re-save with joblib
joblib.dump(model, "RidgeModel_new.joblib")
print("Done!")