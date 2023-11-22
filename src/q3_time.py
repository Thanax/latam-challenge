from typing import List, Tuple
import pandas as pd

def q3_time(file_path: str) -> List[Tuple[str, int]]:

    # Read json file
    df = pd.read_json(file_path, lines=True)

    # Filter the DataFrame to include only the rows that contain a mention of a user
    filtered_df = df[df['content'].str.contains('@')]

    # Extract the usernames from the mentions
    mentions = filtered_df['content'].str.extractall(r'@(\w+)').reset_index(drop=True)[0]

    # Count the number of occurrences of each user
    top_users = mentions.value_counts().nlargest(10)

    # Print the top 10 most "popular" users
    print(top_users)

    data = [(content, count) for content, count in top_users.items()]

    return data