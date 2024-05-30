import pickle
from pymongo import MongoClient
from tqdm import tqdm  # Import tqdm for progress bar
import numpy as np  # Import numpy for array operations

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')  # Connection URI for MongoDB
db = client['BDA_Project']  
collection = db['songs_data'] 

# Open the pickle file in read-binary mode
with open('features.pkl', 'rb') as f:
    # Load the DataFrame from the pickle file
    df = pickle.load(f)
    
    # Iterate over each row in the DataFrame with tqdm
    for index, row in tqdm(df.iterrows(), total=len(df), desc='Uploading data', unit=' rows'):
        try:
            # Convert NumPy arrays to Python lists
            features_list = row['Feature'].tolist()
            
            # Convert each row into a dictionary
            data = {
                'labels': row['Label'],
                'features': features_list
            }
            
            # Insert the data into MongoDB
            collection.insert_one(data)
            
        except Exception as e:
            print(f"Error inserting row {index}: {e}")
        
        finally:
            # Delete the loaded row to free up memory
            del data

# Close MongoDB connection
client.close()

