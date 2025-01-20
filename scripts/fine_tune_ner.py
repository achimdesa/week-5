from transformers import AutoTokenizer, AutoModelForTokenClassification, Trainer, TrainingArguments
import evaluate  # New import for metrics computation

def tokenize_and_align_labels(labeled_data, tokenizer_name="Davlan/xlm-roberta-base-amharic"):
    """Tokenize the dataset and align labels."""
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
    
    def tokenize_and_align_labels_batch(examples):
        tokenized_inputs = tokenizer(examples['tokens'], truncation=True, is_split_into_words=True)
        word_ids = tokenized_inputs.word_ids()
        previous_word_idx = None
        label_ids = []
        for word_idx in word_ids:
            if word_idx is None:
                label_ids.append(-100)
            elif word_idx != previous_word_idx:
                label_ids.append(examples['ner_tags'][word_idx])
            else:
                label_ids.append(examples['ner_tags'][word_idx] if examples['ner_tags'][word_idx] != -100 else -100)
            previous_word_idx = word_idx
        tokenized_inputs["labels"] = label_ids
        return tokenized_inputs
    
    tokenized_dataset = labeled_data.map(tokenize_and_align_labels_batch, batched=True)
    return tokenized_dataset

def compute_metrics(p):
    metric = evaluate.load("seqeval")  # Changed from datasets.load_metric to evaluate.load
    predictions, labels = p
    predictions = predictions.argmax(axis=-1)
    true_labels = [[label for label in label_example if label != -100] for label_example in labels]
    true_predictions = [
        [pred for pred, label in zip(prediction, label) if label != -100]
        for prediction, label in zip(predictions, labels)
    ]
    results = metric.compute(predictions=true_predictions, references=true_labels)
    return {
        "precision": results["overall_precision"],
        "recall": results["overall_recall"],
        "f1": results["overall_f1"],
        "accuracy": results["overall_accuracy"],
    }

def train_model(tokenized_data, model_name="Davlan/xlm-roberta-base-amharic", output_dir="./ner_model"):
    """Train the NER model using the tokenized data."""
    model = AutoModelForTokenClassification.from_pretrained(model_name, num_labels=5)  # Adjust num_labels as per your data
    
    training_args = TrainingArguments(
        output_dir=output_dir,
        evaluation_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16,
        num_train_epochs=3,
        weight_decay=0.01,
        logging_dir="./logs",
    )
    
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_data["train"],
        eval_dataset=tokenized_data["test"],
        compute_metrics=compute_metrics,
    )
    
    trainer.train()
    return model
