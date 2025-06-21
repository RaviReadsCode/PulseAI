def explain_prediction(prediction: str) -> str:
    if prediction == "Flatline":
        return "Very low signal variation detected — this may indicate missing data or asystole."
    elif prediction == "Normal":
        return "The heart rhythm appears consistent and regular within expected variation."
    elif prediction == "Arrhythmia Suspected":
        return "Slight irregularities found — may warrant further screening."
    elif prediction == "Irregular/Artifact":
        return "High signal fluctuation — could be due to movement or lead issues."
    else:
        return "No explanation available."
