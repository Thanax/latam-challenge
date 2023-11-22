from typing import List, Tuple
from datetime import datetime
import pandas as pd

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Read json in chunks
    chunks = pd.read_json(file_path, lines=True, chunksize=1000)

    # Initialize an empty list to store the data
    data = []

    # Iterate over the chunks
    for chunk in chunks:
        # Convert the date column to datetime
        chunk['date'] = pd.to_datetime(chunk['date'])
        
        # Extract username from user column
        chunk['username'] = chunk['user'].apply(lambda x: x['username'])
        
        # Group the data by date and username, and count the number of tweets for each user on each date
        grouped_chunk = chunk.groupby(['date', 'username']).size().reset_index(name='count')

        # Select the top 10 dates with the most tweets and the username of the user with the most tweets on each date
        top_users = grouped_chunk.loc[grouped_chunk.groupby('date')['count'].idxmax()]
        top_dates = top_users['date'].value_counts().nlargest(10).index
        top_users = top_users[top_users['date'].isin(top_dates)]

        # Append the resulting data to the list
        data += [(row['date'].date(), row['username']) for _, row in top_users.iterrows()]

        # Select only the top 10 results
        data = data[:10]

    return data