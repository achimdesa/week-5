# # import re
# # import pandas as pd
# # import string
# # from sklearn.model_selection import train_test_split

# # # Import any Amharic-specific libraries or custom tokenizers if available
# # try:
# #     import spacy
# #     # Load a pre-trained Amharic model if available
# #     nlp = spacy.load("xx_ent_wiki_sm")
# # except Exception as e:
# #     print(f"Error loading model: {e}")
# #     nlp = None  # Handle custom tokenizer here if Spacy is not available



# # # Regular expression to match emojis
# # EMOJI_PATTERN = re.compile("["
# #                            u"\U0001F600-\U0001F64F"  # emoticons
# #                            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
# #                            u"\U0001F680-\U0001F6FF"  # transport & map symbols
# #                            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
# #                            "]+", flags=re.UNICODE)

# # def remove_special_characters_and_emojis(text):
# #     """
# #     Removes special characters, emojis, and irrelevant symbols from text.
# #     """
# #     # Remove emojis
# #     text = EMOJI_PATTERN.sub(r'', text)
    
# #     # Remove other unnecessary characters (e.g., punctuation and special symbols)
# #     text = re.sub(r'[^\w\s\u1200-\u137F፡።፣፤፥፦፧፨፠-፿]', '', text)  # Keep only letters, numbers, and Amharic characters
    
# #     # Remove extra spaces
# #     text = re.sub(r'\s+', ' ', text).strip()
    
# #     return text

# # def tokenize_mixed_text(text):
# #     """
# #     Tokenize mixed text containing both Amharic and non-Amharic characters.
# #     Treat punctuation, emojis, and symbols as separate tokens, but keep Amharic text intact.
# #     """
# #     # Define patterns for Amharic characters, non-Amharic words, and symbols
# #     amharic_word_pattern = r'[\u1200-\u137F]+(?:፣|\.)?'  # Match Amharic words with punctuation
# #     non_amharic_pattern = r'[a-zA-Z0-9%]+'
    
# #     # Combine the patterns to form a full regex for tokenizing
# #     token_pattern = re.compile(r'({}|{})'.format(amharic_word_pattern, non_amharic_pattern))
    
# #     # Apply the regex pattern to find all tokens
# #     tokens = token_pattern.findall(text)
    
# #     return tokens
# # def preprocess_amharic_text(text):
# #     """
# #     Cleans, normalizes, and tokenizes Amharic and English text.
# #     Handles special characters, English words, and Amharic tokens.
# #     """
# #     if pd.isna(text):
# #         return ""  # Handle NaN values
    
# #     # Remove special characters, emojis, and symbols
# #     text = remove_special_characters_and_emojis(text)
    
# #     # Tokenize the text using the improved tokenization function
# #     tokens = tokenize_mixed_text(text)
    
# #     # Join tokens with a space to ensure proper format
# #     return ' '.join(tokens)


# # def process_telegram_data(input_file, output_file):
# #     """
# #     Reads raw scraped Telegram data, preprocesses it, and saves the cleaned version.
# #     """
# #     # Load the scraped data
# #     df = pd.read_csv(input_file)

# #     # Drop rows where the message is empty or NaN
# #     df.dropna(subset=['Message'], inplace=True)

# #     # Clean and tokenize each message
# #     df['cleaned_message'] = df['Message'].apply(preprocess_amharic_text)

# #     # Save the cleaned and tokenized data for labeling
# #     df.to_csv(output_file, index=False)

# #     print(f"Processed data saved to {output_file}")

# # if __name__ == "__main__":
# #     # Path to raw data
# #     input_path = '../data/telegram_data.csv'

# #     # Path to save cleaned data
# #     output_path = '../data/cleaned_telegram_data.csv'

# #     process_telegram_data(input_path, output_path)


# import re
# import pandas as pd
# import string
# from sklearn.model_selection import train_test_split

# # Import any Amharic-specific libraries or custom tokenizers if available
# try:
#     import spacy
#     # Load a pre-trained Amharic model if available
#     nlp = spacy.load("xx_ent_wiki_sm")
# except Exception as e:
#     print(f"Error loading model: {e}")
#     nlp = None  # Handle custom tokenizer here if Spacy is not available

# # Regular expression to match emojis
# EMOJI_PATTERN = re.compile("[" 
#                            u"\U0001F600-\U0001F64F"  # emoticons
#                            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
#                            u"\U0001F680-\U0001F6FF"  # transport & map symbols
#                            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
#                            "]+", flags=re.UNICODE)

# def remove_special_characters_and_emojis(text):
#     """
#     Removes special characters, emojis, and irrelevant symbols from text.
#     """
#     # Remove emojis
#     text = EMOJI_PATTERN.sub(r'', text)
    
#     # Remove other unnecessary characters (e.g., punctuation and special symbols)
#     text = re.sub(r'[^\w\s\u1200-\u137F፡።፣፤፥፦፧፨፠-፿]', '', text)  # Keep only letters, numbers, and Amharic characters
    
#     # Remove extra spaces
#     text = re.sub(r'\s+', ' ', text).strip()
    
#     return text

# def tokenize_mixed_text(text):
#     """
#     Tokenize mixed text containing both Amharic and non-Amharic characters.
#     Treat punctuation, emojis, and symbols as separate tokens, but keep Amharic text intact.
#     """
#     # Define patterns for Amharic characters, non-Amharic words, and symbols
#     amharic_word_pattern = r'[\u1200-\u137F]+(?:፣|\.)?'  # Match Amharic words with punctuation
#     non_amharic_pattern = r'[a-zA-Z0-9%]+'  # Match English and numeric patterns
    
#     # Combine the patterns to form a full regex for tokenizing
#     token_pattern = re.compile(r'({}|{})'.format(amharic_word_pattern, non_amharic_pattern))
    
#     # Apply the regex pattern to find all tokens
#     tokens = token_pattern.findall(text)
    
#     return tokens

# def preprocess_amharic_text(text):
#     """
#     Cleans, normalizes, and tokenizes Amharic and English text.
#     Handles special characters, English words, and Amharic tokens.
#     """
#     if pd.isna(text):
#         return ""  # Handle NaN values
    
#     # Remove special characters, emojis, and symbols
#     text = remove_special_characters_and_emojis(text)
    
#     # Tokenize the text using the improved tokenization function
#     tokens = tokenize_mixed_text(text)
    
#     # Join tokens with a space to ensure proper format
#     return ' '.join(tokens)

# def process_telegram_data(input_file, output_file):
#     """
#     Reads raw scraped Telegram data, preprocesses it, and saves the cleaned version.
#     """
#     # Load the scraped data
#     df = pd.read_csv(input_file)

#     # Drop rows where the message is empty or NaN
#     df.dropna(subset=['Message'], inplace=True)

#     # Clean and tokenize each message
#     df['cleaned_message'] = df['Message'].apply(preprocess_amharic_text)

#     # Save the cleaned and tokenized data for labeling
#     df.to_csv(output_file, index=False)

#     print(f"Processed data saved to {output_file}")

# if __name__ == "__main__":
#     # Path to raw data
#     input_path = '../data/telegram_data.csv'

#     # Path to save cleaned data
#     output_path = '../data/cleaned_telegram_data.csv'

#     process_telegram_data(input_path, output_path)


import re
import pandas as pd
import string
from sklearn.model_selection import train_test_split

# Import any Amharic-specific libraries or custom tokenizers if available
try:
    import spacy
    # Load a pre-trained Amharic model if available
    nlp = spacy.load("xx_ent_wiki_sm")
except Exception as e:
    print(f"Error loading model: {e}")
    nlp = None  # Handle custom tokenizer here if Spacy is not available

# Regular expression to match emojis
EMOJI_PATTERN = re.compile("[" 
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)

def remove_special_characters_and_emojis(text):
    """
    Removes special characters, emojis, and irrelevant symbols from text.
    """
    # Remove emojis
    text = EMOJI_PATTERN.sub(r'', text)
    
    # Remove other unnecessary characters (e.g., punctuation and special symbols)
    text = re.sub(r'[^\w\s\u1200-\u137F፡።፣፤፥፦፧፨፠-፿]', '', text)  # Keep only letters, numbers, and Amharic characters
    
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def tokenize_mixed_text(text):
    """
    Tokenize mixed text containing both Amharic and non-Amharic characters.
    Treat punctuation, emojis, and symbols as separate tokens, but keep Amharic text intact.
    """
    # Define patterns for Amharic characters, non-Amharic words, and punctuation
    amharic_word_pattern = r'[\u1200-\u137F]+(?:፣|\.)?'  # Match Amharic words with punctuation
    english_word_pattern = r'[a-zA-Z]+'  # Match English words
    number_pattern = r'[0-9]+'  # Match numbers
    punctuation_pattern = r'[.,:!?]'  # Match punctuation marks

    # Combine the patterns to form a full regex for tokenizing
    token_pattern = re.compile(f'({amharic_word_pattern}|{english_word_pattern}|{number_pattern}|{punctuation_pattern})')

    # Apply the regex pattern to find all tokens
    tokens = token_pattern.findall(text)
    
    return tokens

def preprocess_amharic_text(text):
    """
    Cleans, normalizes, and tokenizes Amharic and English text.
    Handles special characters, English words, and Amharic tokens.
    """
    if pd.isna(text):
        return ""  # Handle NaN values
    
    # Remove special characters, emojis, and symbols
    text = remove_special_characters_and_emojis(text)
    
    # Tokenize the text using the improved tokenization function
    tokens = tokenize_mixed_text(text)
    
    # Join tokens with a space to ensure proper format
    return ' '.join(tokens)

def process_telegram_data(input_file, output_file):
    """
    Reads raw scraped Telegram data, preprocesses it, and saves the cleaned version.
    """
    # Load the scraped data
    df = pd.read_csv(input_file, encoding='Windows-1252')

    # Drop rows where the message is empty or NaN
    df.dropna(subset=['Message'], inplace=True)

    # Clean and tokenize each message
    df['cleaned_message'] = df['Message'].apply(preprocess_amharic_text)

    # Save the cleaned and tokenized data for labeling
    df.to_csv(output_file, index=False)

    print(f"Processed data saved to {output_file}")

if __name__ == "__main__":
    # Path to raw data
    input_path = '../data/telegram_data.csv'

    # Path to save cleaned data
    output_path = '../data/cleaned_telegram_data_new.csv'

    process_telegram_data(input_path, output_path)
