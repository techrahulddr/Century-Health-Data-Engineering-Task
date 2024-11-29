import pandas as pd

def load_datasets(patients, encounters, symptoms, medications, conditions):
    """Load all datasets into memory."""
    return {
        "patients": patients,
        "encounters": encounters,
        "symptoms": symptoms,
        "medications": medications,
        "conditions": conditions,
    }
