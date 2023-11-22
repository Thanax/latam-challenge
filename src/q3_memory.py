from typing import List, Tuple
import pandas as pd

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    # Read json file in chunks
    chunks = pd.read_json(file_path, lines=True, chunksize=1000)

    # Initialize an empty Series to store the usernames
    usernames = pd.Series(dtype='string')

    # Iterate over the chunks
    for chunk in chunks:
        # Extract the usernames from the mentions column
        chunk_usernames = chunk['content'].str.extract(r'@(\w+)', expand=False).dropna()

        # Concatenate the usernames to the Series
        usernames = pd.concat([usernames, chunk_usernames])

    # Count the number of occurrences of each username
    top_users = usernames.value_counts().nlargest(10)

    # Return the top 10 most popular users as a list of tuples
    return [(username, count) for username, count in top_users.items()]