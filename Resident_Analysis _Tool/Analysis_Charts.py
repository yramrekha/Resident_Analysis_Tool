import matplotlib.pyplot as plt
import seaborn as sns
import os
import pandas as pd
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# Below are the codes of some of the ways we extracted and presented the original set of data
# There were many more graphs but more or less, they had the same principles used
# Load the dataset after the data has been cleaned and checked

df = pd.read_csv('data/resident_satisfaction_survey_data.csv')

# Create a directory to save visualizations
if not os.path.exists('visualizations'):
    os.makedirs('visualizations')

# Filter data for Chartwell residents
chartwell_df = df[df['Location'] == 'Chartwell']

# Plotting Pie chart for gender distribution in Chartwell

plt.figure(figsize=(8, 8))
chartwell_df['Gender'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, colors=['pink', 'lightblue'])
plt.title('Gender Distribution in Chartwell', fontweight='bold')
plt.ylabel('')

plt.legend(chartwell_df['Gender'].value_counts().index, title='')

# A key showing which color represents which data
legend_labels = {'pink': 'Female', 'lightblue': 'Male'}
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=label, markerfacecolor=color, markersize=10) for color, label in legend_labels.items()]
plt.legend(handles=legend_elements, loc='lower left')

#Adding an image/illustration to the graph
img_path = 'pictures/gender.jpg'
img = plt.imread(img_path)
imagebox = OffsetImage(img, zoom=0.5)
ab = AnnotationBbox(imagebox, (1.0, 1.0), frameon=False, xycoords='axes fraction', boxcoords='axes fraction', pad=0)
plt.gca().add_artist(ab)

plt.savefig('visualizations/chartwell_gender_distribution.png')
plt.show()

# Plotting bar chart for age distribution in Chartwell
# Displaying the highest age group count to target the right audience to grow the business
plt.figure(figsize=(10, 6))
sns.countplot(x='Age', data=chartwell_df)
plt.title('Age Distribution in Chartwell', fontweight='bold')
def get_most_common_age_group(data):
    return data['Age'].mode().iloc[0]
most_common_age_group = get_most_common_age_group(chartwell_df)

# Get the count of the most common age group
count_most_common_age = chartwell_df['Age'].value_counts().max()

total_count = len(chartwell_df)

# Calculate the percentage of the most common age group and display it in a box
percentage_most_common_age = (count_most_common_age / total_count) * 100

plt.text(2.3, 250 , f'The targeted age group\nat this moment seems to be\n"{most_common_age_group}"\n({percentage_most_common_age:.1f}%)',
         fontsize=10, ha='left', va='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

plt.savefig('visualizations/chartwell_age_distribution.png')
plt.show()

# Plotting bar chart for satisfaction scores comparing all locations
# and comparing where Chartwell ranks in every category

sns.set(style="whitegrid")

# Define the satisfaction columns
satisfaction_columns = ['Food_Satisfaction', 'Entertainment_Satisfaction', 'Cleanliness_Satisfaction',
                         'Amenities_Satisfaction', 'Staff_Satisfaction']

# Create a custom color palette
custom_palette = {'Chartwell': "#D3ACE8", 'Bridlewood': "lightgrey", 'Redwoods': "lightgrey",
                  'Revera': "lightgrey", 'Maplewood': "lightgrey"}


for col in satisfaction_columns:
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Location', y=col, data=df, palette=custom_palette, capsize=0, errwidth=0)
    plt.title(f'{col} Comparison between Locations', fontweight='bold')
    
   # Adding rank at the top right corner for Chartwell
    ax = sns.barplot(x='Location', y=col, data=df, palette=custom_palette, capsize=0, errwidth=0)
    avg_scores = df.groupby('Location')[col].mean().sort_values(ascending=False)
    rank = avg_scores.index.get_loc('Chartwell') + 1 
    color = 'gold' if rank == 1 else 'silver' if rank == 2 else 'rosybrown' if rank == 3 else 'red'
    
    # Adding the rank text
    ax.text(4.3, 3.6, f"Rank: {rank}", ha='right', va='bottom', color=color, fontweight='1000', fontsize=20, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))
    plt.savefig(f'visualizations/{col.lower()}_comparison.png')
    plt.show()
    
# Pie chart for people looking to move out Chartwell with custom colors

plt.figure(figsize=(12, 6))
chartwell_df['Thinking_of_Moving'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, colors=['lightgreen', 'salmon', 'red'], labels=None)
plt.title('Chartwell Residents Thinking of Moving', fontweight='bold')
plt.ylabel('')

legend_labels = {'lightgreen': 'No', 'salmon': 'Maybe', 'red': 'Yes'}
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=label, markerfacecolor=color, markersize=10) for color, label in legend_labels.items()]
plt.legend(handles=legend_elements, loc='lower left')

counts = chartwell_df['Thinking_of_Moving'].value_counts()
if (counts.get('Yes', 0) + counts.get('Maybe', 0)) / sum(counts) > 0.2:
   
    # Add a warning message
    warning_message = "WARNING\n" \
                      "The moving out percentage is .\n" \
                      "greater than 20%.\n" \
                      "Actions needed to address \n" \
                      "the residents' needs\n" \
                      "and see where the home is losing \n" \
                      "to the other companies."

    plt.annotate(warning_message, xy=(1.2, 0.7), xycoords='axes fraction',
                 ha='center', va='center', bbox=dict(boxstyle='round', facecolor='red', alpha=0.5))

plt.savefig('visualizations/chartwell_moving_pie_chart_custom_colors.png')
plt.show()


