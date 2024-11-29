def clean_patients(patients):
    """Clean and preprocess the patients dataset."""
    patients = patients.dropna(subset=["id"])
    patients["gender"] = patients["gender"].str.title()
    return patients
