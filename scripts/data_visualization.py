import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

def generate_basic_stats(df):
    """Generate basic statistics for the dataframe."""
    return df.describe()

def plot_message_length_distribution(df):
    """Plot the distribution of message lengths."""
    df['Message Length'] = df['Cleaned_Message'].apply(lambda x: len(str(x)))
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Message Length'], bins=50, color='blue')
    plt.title('Distribution of Cleaned Message Lengths')
    plt.xlabel('Message Length')
    plt.ylabel('Frequency')
    plt.show()

def plot_message_over_time(df):
    """Plot the number of messages over time."""
    plt.figure(figsize=(10, 6))
    df['Message'].resample('M').count().plot(color='green')
    plt.title('Number of Messages Over Time')
    plt.xlabel('Date')
    plt.ylabel('Message Count')
    plt.show()

def generate_word_cloud(df, column):
    """Generate a word cloud from the specified column."""
    all_text = ' '.join(df[column].dropna().tolist())
    wordcloud = WordCloud(width=800, height=400, background_color='white', max_words=100).generate(all_text)
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'Word Cloud of {column}')
    plt.show()
