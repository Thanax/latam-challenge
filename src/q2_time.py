from typing import List, Tuple
import pandas as pd

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    
    # Read json file
    df = pd.read_json(file_path, lines=True)

    # Extract all the emojis from the content column
    emojis = df['content'].str.extractall(r'(:\w+:)').reset_index(drop=True)

    # Count the number of occurrences of each emoji
    top_emojis = emojis[0].value_counts().nlargest(10)

    data = [(emoji, count) for emoji, count in top_emojis.items()]

    return data