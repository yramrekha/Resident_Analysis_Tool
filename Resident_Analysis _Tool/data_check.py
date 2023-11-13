import csv

# This was a simple check to ensure all data in the csv were corrent
# Any missing data were omitted in the new saved file
# As a result, 2 set of data were omitted in the new file, since they has missing values

def check_data(record):
    # Define valid ranges and values for each field
    valid_ranges = {
        'location': ['Chartwell', 'Bridlewood', 'Revera', 'Redwoods', 'Maplewood'],
        'Age': ['60-69', '70-79', '80-89', '90+'],
        'food': ['1', '2', '3', '4', '5'],
        'entertainment': ['1', '2', '3', '4', '5'],
        'staff': ['1', '2', '3', '4', '5'],
        'amenities': ['1', '2', '3', '4', '5'],
        'cleanliness': ['1', '2', '3', '4', '5'],
        'recommend': ['Yes', 'No', 'Maybe'],
        'move': ['Yes', 'No', 'Maybe']
    }

    # Check if values are within the required range
    for field, valid_values in valid_ranges.items():
        if field in record and record[field] not in valid_values:
            return False

    return True

# Read the data from resident_satisfaction_survey_data_raw.csv
with open('resident_satisfaction_survey_data_raw.csv', 'r') as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames

    # Filter out records with missing or corrupted data
    valid_records = [record for record in reader if check_data(record)]
    
#######################################
# If ever we wanted to filter and copy the results for a particular section
#for example only Age=60-69 or a particular location or gender
#we could add the following condition:

# Let's say we want to copy only location= Chartwell:

# chartwell_records = [record for record in reader if check_data(record) and record.get('location') == 'Chartwell']

# It will then Write the valid records to resident_satisfaction_survey_data.csv
############################################

with open('resident_satisfaction_survey_data.csv', 'w', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(valid_records)

print("Data check and cleanup completed. Valid data saved to resident_satisfaction_survey_data.csv.")
