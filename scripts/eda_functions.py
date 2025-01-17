# scripts/eda_functions.py

def get_basic_stats(text_series):
    """
    Returns basic statistics about the text data such as average message length, etc.
    """
    message_lengths = text_series.apply(len)
    
    stats = {
        'Total messages': len(text_series),
        'Average message length': message_lengths.mean(),
        'Longest message': message_lengths.max(),
        'Shortest message': message_lengths.min(),
    }
    
    return stats
