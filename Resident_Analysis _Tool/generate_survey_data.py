import numpy as np
import pandas as pd

# Set seed for reproducibility
np.random.seed(42)

# Generate random demographic data
num_residents = 1000
locations = np.random.choice(['Chartwell', 'Bridlewood', 'Redwoods', 'Revera', 'Maplewood'], num_residents, 
p=[0.465, 0.046, 0.102, 0.231, 0.156])
Gender = np.random.choice(['Male', 'Female'], num_residents , p= [0.23 , 0.77])
ages = np.random.choice(['60-69', '70-79', '80-89', '90+'], num_residents , p=[0.023, 0.143, 0.56, 0.274])


# Generate satisfaction scores
satisfaction_scores = {
    'Food': np.random.randint(1, 6, num_residents),
    'Entertainment': np.random.randint(1, 6, num_residents),
    'Cleanliness': np.random.randint(1, 6, num_residents),
    'Amenities': np.random.randint(1, 6, num_residents),
    'Staff': np.random.randint(1, 6, num_residents),
}

# Generate recommendations and moving intentions
recommendations = np.random.choice(['Yes', 'No', 'Maybe'], num_residents , p= [0.443 , 0.271, 0.286] )
moving_intentions = np.random.choice(['Yes', 'No', 'Maybe'], num_residents , p= [0.173 , 0.561, 0.266])

# Create a DataFrame
df = pd.DataFrame({
    'Location': locations,
    'Gender' : Gender,
    'Age': ages,
    'Food_Satisfaction': satisfaction_scores['Food'],
    'Entertainment_Satisfaction': satisfaction_scores['Entertainment'],
    'Cleanliness_Satisfaction': satisfaction_scores['Cleanliness'],
    'Amenities_Satisfaction': satisfaction_scores['Amenities'],
    'Staff_Satisfaction': satisfaction_scores['Staff'],
    'Recommendation': recommendations,
    'Thinking_of_Moving': moving_intentions,
})

# Save to CSV
df.to_csv('data/resident_satisfaction_survey_data_raw.csv', index=False)
