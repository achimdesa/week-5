# week-5
# EthioMart NER Project

## Overview

### Business Need

EthioMart aims to become the primary hub for Telegram-based e-commerce activities in Ethiopia. With the increasing popularity of Telegram for business transactions, various independent e-commerce channels have emerged, each facilitating its own operations. However, this decentralization presents challenges for both vendors and customers who need to manage multiple channels for product discovery, order placement, and communication.

To solve this problem, EthioMart plans to create a single centralized platform that consolidates real-time data from multiple e-commerce Telegram channels into one unified channel. This will provide a seamless experience for customers to explore and interact with multiple vendors in one place.

### Project Focus

This project focuses on fine-tuning Large Language Models (LLMs) for an Amharic Named Entity Recognition (NER) system that extracts key business entities such as product names, prices, and locations from text, images, and documents shared across these Telegram channels. The extracted data will populate EthioMart's centralized database, making it a comprehensive e-commerce hub.

## Key Objectives

- Real-time data extraction from Telegram channels.
- Fine-tuning LLMs to extract entities like product names, prices, and locations.


## Task 1: Data Ingestion and Preprocessing
Data Collection:
The data was collected from Ethiopian-based e-commerce Telegram channels. For this, a custom scraper was built to capture text messages, product images, and other relevant data in real-time.
Steps:
1.	Telegram Scraper: A custom message ingestion system was implemented to fetch real-time messages, images, and documents posted in the selected Telegram channels.
2.	Data Preprocessing: The messages were processed, focusing on Amharic text. Preprocessing included:
o	Tokenization: Splitting the text into tokens (words).
o	Normalization: Handling variations in Amharic spelling and characters.
o	Cleaning: Removing unnecessary metadata such as timestamps, user IDs, and irrelevant text symbols.
Challenges & Solutions:
•	Amharic Tokenization: Dealing with morphological variations and the lack of spaces between words in Amharic posed a challenge. A custom tokenizer was created to address this.
•	Handling Ambiguities: Preprocessing involved addressing common ambiguities in Amharic text, such as mixed usage of punctuation.
 
## Task 2: Labeling a Subset of Dataset in CoNLL Format
The next task involved labeling a portion of the collected dataset in CoNLL format for NER training. This format is widely used for entity recognition tasks, where each token is labeled as either part of a specific entity (e.g., product, price, location) or as outside any entity (O).
Key Entities:
•	B-Product: Beginning of a product entity (e.g., “Smartphone”).
•	I-Product: Inside a product entity (e.g., “Cover” in "Smartphone Cover").
•	B-LOC: Beginning of a location entity (e.g., “Addis Abeba”).
•	I-LOC: Inside a location entity (e.g., “Abeba” in “Addis Abeba”).
•	B-PRICE: Beginning of a price entity (e.g., "1000 ብር").
•	I-PRICE: Inside a price entity (e.g., "ብር").


The goal was to label at least 50-100 messages with these entity types. This labeled data would serve as training data for our NER model.
 
## Task 3: Fine-Tuning the NER Model
Model Selection:
To build the NER system, several pre-trained models were considered. For fine-tuning, the following models were chosen due to their compatibility with multilingual tasks and efficiency in resource-constrained environments:
•	XLM-Roberta: A robust multilingual model for NER tasks.
•	DistilBERT: A lightweight version of BERT with reduced computational cost.
•	mBERT (Multilingual BERT): Suitable for Amharic text processing.
•	AfroXLM-R: A model fine-tuned specifically for African languages, including Amharic.
Fine-Tuning Process:
The labeled dataset in CoNLL format was loaded and tokenized using Hugging Face’s datasets library. The labels were aligned with the tokens produced by the tokenizer. Fine-tuning involved:
1.	Training on Labeled Data: The models were fine-tuned for the NER task using the labeled Amharic data.
2.	Hyperparameters: Key parameters included a learning rate of 2e-5, batch size of 16, and training for 3 epochs.
The Hugging Face Trainer API was used to fine-tune the models, followed by evaluation on a validation set

 
## Task 4: Model Comparison & Selection
Model Comparison:
After fine-tuning multiple models, I evaluated their performance based on standard NER metrics such as precision, recall, F1-score, and accuracy. The models were compared in terms of their ability to correctly identify the product, price, and location entities.
1.	XLM-Roberta: A multilingual model fine-tuned for NER tasks, known for its strong performance across multiple languages.
2.	DistilRoBERTa: A distilled, lightweight version of RoBERTa designed to be faster and more efficient without sacrificing too much accuracy.
3.	mBERT (Multilingual BERT): A version of BERT pre-trained on multiple languages, including Amharic, that is widely used for language modeling tasks.
Dataset Preparation:
I loaded and preprocessed the labeled dataset in CoNLL format, which consisted of product names, prices, and locations extracted from Amharic Telegram messages. Given the size of the dataset, a train-validation split was performed, ensuring that the models were trained and evaluated on separate subsets of the data.
The dataset was tokenized using each model's respective tokenizer, and the labels were aligned to the tokens, ensuring the NER model could correctly map each token to its corresponding entity.
Models and Training:
The models were trained using the Hugging Face Trainer API, which simplifies the fine-tuning process. Each model was fine-tuned for 3 epochs with a learning rate of 2e-5. The training also involved the use of a data collator to handle dynamic padding and ensure that batch sizes were consistent during training.
The following models were compared:
•	XLM-Roberta: Tokenized and fine-tuned for NER tasks.
•	DistilRoBERTa: A smaller and faster model but potentially less accurate.
•	mBERT: A multilingual version of BERT pre-trained on multiple languages, including Amharic.
Evaluation Metrics:
To compare the models' performance, I used the seqeval metric, which computes precision, recall, F1-score, and accuracy for sequence labeling tasks such as NER. These metrics were crucial in determining the best model for Amharic entity extraction.
•	Precision: How many of the identified entities were actually correct.
•	Recall: How many of the actual entities in the text were correctly identified.
•	F1-score: The harmonic mean of precision and recall, providing a balanced measure of both.
•	Accuracy: The overall percentage of correct predictions.
## Results:
The evaluation results for each model after fine-tuning are summarized below:
Model	Precision	Recall	F1-Score	Accuracy
XLM-Roberta	0.8564	0.8491	0.8527	87.3%
DistilRoBERTa	0.8052	0.7943	0.7997	81.0%
mBERT	0.8135	0.8072	0.8103	82.2%
## Key Insights:
1.	XLM-Roberta consistently outperformed the other models, achieving the highest F1-score and accuracy. Its ability to handle multilingual text with robust entity recognition capabilities made it ideal for Amharic NER.
2.	DistilRoBERTa, while faster and more lightweight, showed lower performance, likely due to its compressed architecture.
3.	mBERT performed reasonably well, but it was slightly less accurate compared to XLM-Roberta, making it less suitable for this particular task.
Conclusion:
Based on the evaluation metrics, XLM-Roberta was selected as the best-performing model for the task of extracting Amharic entities from Telegram messages. While DistilRoBERTa offered speed advantages, it was outmatched by XLM-Roberta in terms of precision, recall, and F1-score, making XLM-Roberta the ideal choice for production use.
 
## Task 5: Model Interpretability
Model interpretability is essential for building trust in the NER system, especially when dealing with business-critical entities like product prices and locations. We employed SHAP (SHapley Additive exPlanations) and LIME (Local Interpretable Model-Agnostic Explanations) to explain how the model arrived at its predictions.
SHAP Analysis:
•	SHAP values helped us understand which tokens in a sentence contributed most to identifying a specific entity.
•	For example, the model could explain why "1000 ብር" was identified as a price, showing the contributions of "1000" and "ብር" to the prediction.
LIME Analysis:
•	LIME was used to generate local explanations for individual predictions. This method helped visualize difficult cases where the model struggled with overlapping entities or ambiguous phrases.
Difficult Cases:
•	Ambiguities: In cases where product names and locations were intertwined (e.g., “Bole Store”), the model sometimes confused the entity types. By analyzing the SHAP values, we identified the need for additional location-specific training data.
 
## Conclusion
This project successfully built a fine-tuned Amharic NER system that can extract essential business entities from Telegram e-commerce messages. By leveraging state-of-the-art language models like AfroXLM-R, we were able to achieve high accuracy and entity extraction performance.
The final NER model not only provides real-time entity extraction for EthioMart’s centralized platform but also offers transparency through SHAP and LIME, enabling us to explain and trust the model’s decisions.
