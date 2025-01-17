import re
import string
import emoji

def clean_text(text):
    """
    Cleans Amharic text by removing special characters, emojis, and extra spaces.
    It also normalizes punctuation and prepares the text for NLP tasks.
    """
    # Check if the text is a string; if not, return an empty string or appropriate placeholder
    if not isinstance(text, str):
        return ""
    
    # 1. Remove emojis using the emoji package
    text = emoji.replace_emoji(text, replace="")  # Removes emojis and replaces them with empty space
    
    # 2. Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # 3. Remove email addresses
    text = re.sub(r'\S+@\S+', '', text)
    
    # 4. Remove non-Amharic letters and non-punctuation characters (numbers, symbols)
    # Amharic characters Unicode range: \u1200-\u137F
    text = re.sub(r'[^\u1200-\u137F\s፡።፣፤፥፦፧፨]', '', text)
    
    # 5. Remove excess whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    # 6. Normalize Amharic punctuation (converting similar punctuation marks to standardized forms)
    text = text.replace('፣', ',')  # Convert Amharic semicolon to comma
    text = text.replace('።', '.')  # Convert Amharic full stop to period
    text = text.replace('፡', ' ')  # Convert Amharic space separator to normal space
    
    # 7. Optionally remove numbers if they're irrelevant
    text = re.sub(r'\d+', '', text)
    
    return text


def preprocess_data(df):
    """Preprocess the dataframe by cleaning the message text."""
    df['Cleaned_Message'] = df['Message'].apply(clean_text)
    return df
