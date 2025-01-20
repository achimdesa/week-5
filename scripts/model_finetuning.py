# scripts/fine_tune_ner.py

import pandas as pd
import torch
from datasets import load_dataset  # Removed load_metric import
from transformers import AutoModelForTokenClassification, TrainingArguments, Trainer, AutoTokenizer

def load_data(file_path):
    """
    Loads the labeled CoNLL data from the specified file path.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    data = []
    current_sentence = []
    current_labels = []
    
    for line in lines:
        line = line.strip()
        if line:
            token, label = line.split()  # Assuming format "token label"
            current_sentence.append(token)
            current_labels.append(label)
        else:
            if current_sentence:
                data.append((current_sentence, current_labels))
                current_sentence = []
                current_labels = []
    
    # Handle the last sentence if not followed by a newline
    if current_sentence:
        data.append((current_sentence, current_labels))

    return data

def tokenize_and_align_labels(examples, tokenizer):
    """
    Tokenizes the input examples and aligns labels with the tokenized inputs.
    """
    tokenized_inputs = tokenizer(examples[0], is_split_into_words=True, padding='max_length', truncation=True, return_tensors="pt")

    labels = []
    for i, label in enumerate(examples[1]):
        word_ids = tokenized_inputs.word_ids(batch_index=0)  # Get word ids for the first item in the batch
        label_ids = [-100] * len(tokenized_inputs['input_ids'][0])  # Default label for padding
        
        # Check if the token length matches the label length
        if word_ids.count(None) + len(examples[1]) != len(word_ids):
            raise ValueError("Mismatch between token and label lengths.")
        
        for word_id in set(word_ids):  # Set to avoid duplicate words
            if word_id is None:
                continue
            label_ids[word_id] = label[i]  # Assign the label to the corresponding token
        
        labels.append(label_ids)

    tokenized_inputs['labels'] = labels
    return tokenized_inputs
