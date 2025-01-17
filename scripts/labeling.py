import pandas as pd
import re

def load_data(file_path):
    """
    Loads the cleaned Telegram data from a CSV file.
    """
    data = pd.read_csv(file_path)
    return data

def is_amharic(token):
    """
    Determines if a token is Amharic based on Unicode ranges.
    Amharic characters are mostly in the range U+1200 to U+137F.
    """
    return re.search(r'[\u1200-\u137F]', token) is not None

# def label_data(data):
#     """
#     Manually label the dataset. The function labels tokens in Amharic messages with specific
#     entity tags such as B-PRODUCT, I-PRICE, B-LOC, etc., and marks English or non-entity tokens as 'O'.
#     """
#     labeled_data = []

#     # Updated placeholder lists for identifying entities
#     product_keywords = ['ማሳጅ', 'ማድረጊያ', 'ሶፍትዌር', 'አስተማማኝ', 'መጽሀፍ', 'የቤት እቃ', 
#                         'ቤት እቃ', 'የልጆች ልብስ', 'ብሪንዝ', 'ሶፋ', 'መኪና', 'ሱሪ', 
#                         'ካሜራ', 'ስልክ', 'ላስቶር', 'ኮምፒውተር', 'የኤሌክትሮኒክስ እቃ', 
#                         'የሴቶች ልብስ', 'ኩባያ', 'ሽፋን', 'ጫማ', 'ምግብ', 'አዳሽ']  # Expanded product list
#     location_keywords = ['አዲስ አበባ', 'ቦሌ', 'መዳህኒዓለም', 'ጅማ', 'ሀረር', 'አስማራ', 
#                          'ጋምቤላ', 'ባህር ዳር']  # Expanded location list
#     price_keywords = ['ብር', 'ዋጋ', 'ተቀንሷል', 'እኩል እቃ', 'ቅናሽ']  # Expanded price list

#     for idx, row in data.iterrows():
#         message = row['cleaned_message']

#         if pd.isna(message) or not isinstance(message, str):
#             continue  # Skip invalid rows

#         tokens = message.split()  # Tokenize the message

#         for token in tokens:
#             if not is_amharic(token):
#                 labeled_data.append((token, 'O'))  # Non-Amharic tokens are 'O'
#                 continue

#             # Label Amharic tokens with entity labels
#             if any(keyword in token for keyword in product_keywords):
#                 labeled_data.append((token, 'B-PRODUCT'))
#             elif any(keyword in token for keyword in price_keywords):
#                 labeled_data.append((token, 'B-PRICE'))
#             elif any(keyword in token for keyword in location_keywords):
#                 labeled_data.append((token, 'B-LOC'))
#             elif token.isnumeric():  # Check for numbers (potentially prices)
#                 labeled_data.append((token, 'I-PRICE'))
#             else:
#                 labeled_data.append((token, 'O'))  # Default label for non-entities

#     return labeled_data

# def save_conll_format(labeled_data, output_file):
#     """
#     Saves labeled data to a file in CoNLL format.
#     """
#     with open(output_file, 'w', encoding='utf-8') as f:
#         for token, label in labeled_data:
#             if token and label:
#                 f.write(f"{token} {label}\n")  # Write token and label
#             else:
#                 f.write("\n")  # Separate each sentence/message with a blank line


# Labeling logic

def label_data(data):
    """
    Labels tokens in Amharic messages with specific entity tags like B-PRODUCT, B-PRICE, etc.
    """
    labeled_data = []

    # Sample keywords for entity recognition
    # Expanded product keywords
    product_keywords = [
        'ማሳጅ', 'ማድረጊያ', 'ሶፍትዌር', 'አስተማማኝ', 'መጽሀፍ', 'ብሪንዝ', 
        'ሶፋ', 'መኪና', 'ካሜራ', 'ስልክ', 'ኮምፒውተር', 'ማሽን', 'እቃ', 'የቤት እቃ', 
        'የኤሌክትሮኒክስ እቃ', 'የሴቶች ልብስ', 'ጫማ', 'ምግብ', 'ኩባያ', 
        'ካምፕላ', 'መቆሚያ', 'ሽፋን', 'ዕቃ', 'አቤባ', 'መጻፍ', 'የተረገም እቃ'
    ]

    # Expanded location keywords
    location_keywords = [
        'አዲስ አበባ', 'ቦሌ', 'መዳህኒዓለም', 'ጅማ', 'አስማራ', 'ባህር ዳር', 
        'ጋምቤላ', 'ሐዋርያ', 'አማራ', 'ኦሮሚያ', 'ሶማሌ', 'ግድም', 'ወልደ ኦርሚ', 
        'ጉይደር', 'ድንጋይ ለከባቢ', 'ገነዘብ', 'እንቁላል', 'ታዋቂ'
    ]

    # Expanded price keywords
    price_keywords = [
        'ብር', 'ዋጋ', 'ቅናሽ', 'ወቅታዊ ዋጋ', 'የወደፍ', 'ክፍያ', 'በየትኛው ዋጋ',
        'ተመርጦ ዋጋ', 'የወንበር እቃ ዋጋ', 'ዋጋ፦', 'መመርመሪያ', 'እኩል'
    ]


    for idx, row in data.iterrows():
        message = row['cleaned_message']

        if pd.isna(message) or not isinstance(message, str):
            continue  # Skip invalid rows

        tokens = message.split()  # Tokenize the message

        for token in tokens:
            # Skip empty tokens and tokens that are not meaningful words
            if len(token.strip()) == 0:
                continue

            # Label the token with entity tags
            if any(keyword in token for keyword in product_keywords):
                labeled_data.append((token, 'B-PRODUCT'))
            elif any(keyword in token for keyword in price_keywords):
                labeled_data.append((token, 'B-PRICE'))
            elif any(keyword in token for keyword in location_keywords):
                labeled_data.append((token, 'B-LOC'))
            else:
                labeled_data.append((token, 'O'))  # Default label for non-entities

    return labeled_data
# Save labeled data in CoNLL format

def save_conll_format(labeled_data, output_file):
    """
    Saves labeled data in CoNLL format.
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        for token, label in labeled_data:
            if token and label:
                f.write(f"{token} {label}\n")
            else:
                f.write("\n")  # Separate each sentence/message with a blank line