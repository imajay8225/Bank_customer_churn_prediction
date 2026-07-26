from services.model_service import check_model, predict_customer
from utils import load_dataset, validate_dataset

sample_customer = {
    "CreditScore": 650,
    "Age": 35,
    "Tenure": 5,
    "Balance": 50000.0,
    "NumOfProducts": 2,
    "HasCrCard": 1,
    "IsActiveMember": 1,
    "EstimatedSalary": 75000.0,
    "Geography": "France",
    "Gender": "Male",
}


def main():
    status = check_model()
    print("Model status:", status)

    df = load_dataset()
    valid, message = validate_dataset(df)
    print("Dataset validation:", valid, message)

    result = predict_customer(sample_customer)
    print("Sample prediction:", result)


if __name__ == "__main__":
    main()