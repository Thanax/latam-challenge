from typing import List, Tuple
import pandas as pd

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    # Read json in chunks
    chunks = pd.read_json(file_path, lines=True, chunksize=1000)

    # Initialize an empty list to store the data
    data = []

    # Iterate over the chunks
    for chunk in chunks:
        # Extract all the emojis from the content column
        emojis = chunk['content'].str.extractall(r'(:\w+:)').reset_index(drop=True)

        # Count the number of occurrences of each emoji
        top_emojis = emojis[0].value_counts().nlargest(10)

        # Select only the top 10 emojis
        top_emojis = top_emojis.iloc[:10]

        data +=  [(emoji, count) for emoji, count in top_emojis.items()]

    return data