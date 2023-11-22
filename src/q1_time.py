from typing import List, Tuple
from datetime import datetime
import pandas as pd

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Read json file
    df = pd.read_json(file_path, lines=True)

    # Convert the date column to datetime
    df['date'] = pd.to_datetime(df['date'])

    # Extract username from user column
    df['username'] = df['user'].apply(lambda x: x['username'])

    # Filter the DataFrame to include only the rows that correspond to the top dates
    top_dates = df['date'].value_counts(sort=False).nlargest(10)
    filtered_df = df[df['date'].isin(top_dates.index)]

    # Group the data by date and user, and get the user with the most tweets for each date
    top_users = filtered_df.groupby(['date', 'username']).size().nlargest(10).reset_index(name='count')
    top_users = top_users.loc[top_users.groupby('date')['count'].idxmax()]

    # Return the resulting data as a list of tuples
    return [(row['date'].date(), row['username']) for _, row in top_users.iterrows()]