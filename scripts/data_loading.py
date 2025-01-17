

import pandas as pd
from transformers import AutoTokenizer

def load_and_preprocess_data(file_path):
    """
    Load the data in CoNLL format and prepare it for training.
    """
    try:
        # Read the file with a proper delimiter
        data = pd.read_csv(file_path, delimiter='\t', names=['tokens', 'labels'], header=None, nrows=100)

        # DEBUG: Print the raw data read from the file
        print("Raw data from file:")
        print(data)

    except Exception as e:
        print(f"Error reading file: {e}")
        return [], []

    sentences, labels = [], []
    temp_sentence, temp_labels = [], []

    for index, row in data.iterrows():
        token = row['tokens'].strip().strip("'")  # Remove leading/trailing whitespace and single quotes
        label = row['labels'].strip() if not pd.isna(row['labels']) else 'O'  # Default to 'O' if label is NaN
        
        # DEBUG: Print each token and label
        print(f"Row {index}: Token = '{token}', Label = '{label}'")

        if token == '':  # Skip empty tokens
            continue

        if label == '':  # Skip empty labels
            continue

        temp_sentence.append(token)
        temp_labels.append(label)

    # Check if the last sentence needs to be added
    if temp_sentence:
        sentences.append(temp_sentence)
        labels.append(temp_labels)

    # DEBUG: Print the sentences and labels before returning
    print("Processed Sentences:", sentences)
    print("Processed Labels:", labels)

    return sentences, labels


# def load_and_preprocess_data(file_path):
#     """
#     Load the data in CoNLL format and prepare it for training.
#     """
#     try:
#         # Read the file with a proper delimiter
#         data = pd.read_csv(file_path, delimiter='\t', names=['tokens', 'labels'], header=None)

#         # DEBUG: Print the raw data read from the file
#         print("Raw data from file:")
#         print(data)

#     except Exception as e:
#         print(f"Error reading file: {e}")
#         return [], []

#     sentences, labels = [], []
#     temp_sentence, temp_labels = [], []

#     for _, row in data.iterrows():
#         token = row['tokens'].strip().strip("'")  # Remove leading/trailing whitespace and single quotes
#         label = row['labels'].strip() if not pd.isna(row['labels']) else 'O'  # Default to 'O' if label is NaN
        
#         if token == '':  # Skip empty tokens
#             continue

#         if label == '':  # Skip empty labels
#             continue

#         if label == 'O':  # If 'O', add it normally, else start new sentence
#             temp_sentence.append(token)
#             temp_labels.append(label)
#         else:
#             temp_sentence.append(token)
#             temp_labels.append(label)

#     # Check if the last sentence needs to be added
#     if temp_sentence:
#         sentences.append(temp_sentence)
#         labels.append(temp_labels)

#     # DEBUG: Print the sentences and labels before returning
#     print("Processed Sentences:", sentences)
#     print("Processed Labels:", labels)

#     return sentences, labels

# def load_and_preprocess_data(file_path):
#     """
#     Load the data in CoNLL format and prepare it for training.
#     """
#     try:
#         # Check if the file exists and read it
#         data = pd.read_csv(file_path, delimiter='\t', names=['tokens', 'labels'], header=None)
        
#         # DEBUG: Print the raw data read from the file
#         print("Raw data from file:")
#         print(data)

#     except Exception as e:
#         print(f"Error reading file: {e}")
#         return [], []

#     sentences, labels = [], []
#     temp_sentence, temp_labels = [], []

#     for _, row in data.iterrows():
#         if pd.isna(row['tokens']):
#             # End of sentence
#             if temp_sentence:  # Only append if there's content
#                 sentences.append(temp_sentence)
#                 labels.append(temp_labels)
#                 temp_sentence, temp_labels = [], []
#         else:
#             temp_sentence.append(row['tokens'])
#             temp_labels.append(row['labels'])

#     # DEBUG: Print the sentences and labels before returning
#     print("Processed Sentences:", sentences)
#     print("Processed Labels:", labels)

#     return sentences, labels

# def load_and_preprocess_data(file_path):
#     """
#     Load the data in CoNLL format and prepare it for training.
#     """
#     data = pd.read_csv(file_path, delimiter='\t', names=['tokens', 'labels'])
#     sentences, labels = [], []
#     temp_sentence, temp_labels = [], []

#     for _, row in data.iterrows():
#         if pd.isna(row['tokens']):
#             # End of sentence
#             if temp_sentence:  # Append only if there's a sentence
#                 sentences.append(temp_sentence)
#                 labels.append(temp_labels)
#             temp_sentence, temp_labels = [], []
#         else:
#             temp_sentence.append(row['tokens'])
#             temp_labels.append(row['labels'])

#     return sentences, labels


def tokenize_and_align_labels(sentences, labels, model_name='xlm-roberta-base'):
    """
    Tokenize sentences and align the labels with sub-tokens.
    Returns a dictionary with tokenized inputs and corresponding labels.
    """
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenized_inputs = tokenizer(sentences, truncation=True, padding=True, is_split_into_words=True)
    
    label_all_tokens = True
    new_labels = []
    
    for i, sentence_labels in enumerate(labels):
        word_ids = tokenized_inputs.word_ids(batch_index=i)  # Get word ids for this sentence
        aligned_labels = []
        previous_word_idx = None
        
        for word_idx in word_ids:
            if word_idx is None:
                aligned_labels.append(-100)  # Special token, ignore
            elif word_idx != previous_word_idx:  # New token, assign the label
                aligned_labels.append(sentence_labels[word_idx])
            else:  # Sub-token of a word, assign the same label if `label_all_tokens` is True
                aligned_labels.append(sentence_labels[word_idx] if label_all_tokens else -100)
                
            previous_word_idx = word_idx
        
        # Ensure the length of aligned_labels matches the length of word_ids
        if len(aligned_labels) != len(word_ids):
            print(f"Warning: Label length mismatch in sentence {i}:")
            print(f"Word ids length: {len(word_ids)}, Labels length: {len(aligned_labels)}")
        
        new_labels.append(aligned_labels)
    
    tokenized_inputs["labels"] = new_labels  # Add aligned labels to the tokenized inputs
    
    # DEBUG: Check token and label lengths
    print("Tokenized inputs length:", len(tokenized_inputs['input_ids']))
    print("Aligned labels length:", len(tokenized_inputs['labels']))
    
    # Limit the printed output to avoid excessive output
    for i in range(min(3, len(tokenized_inputs['input_ids']))):  # Print first 3 token-label pairs
        print(f"Sentence {i}:")
        print("Tokens:", tokenized_inputs['input_ids'][i])
        print("Labels:", tokenized_inputs['labels'][i])
        print("Length comparison:", len(tokenized_inputs['input_ids'][i]), len(tokenized_inputs['labels'][i]))
    
    return tokenized_inputs