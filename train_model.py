import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("data.csv")

# Convert Loan_Status to numeric
df['Loan_Status'] = df['Loan_Status'].map({'Y':1,'N':0})

# Fill missing values
df['ApplicantIncome'].fillna(df['ApplicantIncome'].mean(), inplace=True)
df['LoanAmount'].fillna(df['LoanAmount'].mean(), inplace=True)
df['Credit_History'].fillna(1.0, inplace=True)

# Select only 3 features
features = ['ApplicantIncome','LoanAmount','Credit_History']
X = df[features]
y = df['Loan_Status']

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("model.pkl","wb"))

print("Model trained successfully!")
