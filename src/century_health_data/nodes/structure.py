def standardize_symptoms(symptoms):
    """Extract individual symptoms into separate columns."""
    symptoms[["rash", "joint_pain", "fatigue", "fever"]] = symptoms["SYMPTOMS"].str.split(",", expand=True)
    return symptoms
