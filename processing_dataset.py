import os
import pandas as pd

# Step 1: Load datasets
amazonBookData = pd.read_csv('merged_dataset.csv')
learningResourcesData = pd.read_csv('Learning_Resources_Database.csv')

# Step 2: Standardize Column Names and Structure
# Rename columns in amazonBookData to align with learningResourcesData
amazonBookData = amazonBookData.rename(columns={
    'Book_Name': 'Title',
    'Book_Author': 'Author'
})
# Add missing columns to amazonBookData
for col in ['URL', 'Description', 'Subject']:
    amazonBookData[col] = amazonBookData[col].fillna('') if col in amazonBookData else ''

# Rename columns in learningResourcesData to align with amazonBookData
learningResourcesData = learningResourcesData.rename(columns={
    'Resource Name': 'Title',
    'Resource URL': 'URL',
    'Subject Areas': 'Subject'
})
# Add missing columns to learningResourcesData
learningResourcesData['Author'] = learningResourcesData['Author'].fillna('Unknown') if 'Author' in learningResourcesData else 'Unknown'

# Step 3: Text Cleaning for Descriptions
def clean_text(text):
    if not isinstance(text, str):
        return ""
    # Convert to lowercase and remove special characters
    return text.lower().replace('\n', ' ').replace('\r', '').strip()

amazonBookData['Description'] = amazonBookData['Description'].apply(clean_text)
learningResourcesData['Description'] = learningResourcesData['Description'].apply(clean_text)

# Step 4: Ensure Both Datasets Have the Same Column Order
amazonBookData = amazonBookData[['Title', 'Author', 'URL', 'Description', 'Subject']]
learningResourcesData = learningResourcesData[['Title', 'Author', 'URL', 'Description', 'Subject']]

# Step 5: Concatenate the Two Datasets
combinedData = pd.concat([amazonBookData, learningResourcesData], ignore_index=True)

# Step 6: Save the Combined Dataset to a CSV File
output_file = 'combined_learning_materials.csv'
combinedData.to_csv(output_file, index=False)
print(f"Combined dataset saved to {output_file}")
