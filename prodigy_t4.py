# -*- coding: utf-8 -*-
"""Prodigy_T4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zSpX6Tb6yIk3YygCFqMIKp8rhzfVRONG
"""

import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load your own dataset
file_path = 'sentimental.csv'
df = pd.read_csv('sentimental.csv')

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Check for missing values
print("\nMissing values in the dataset:")
print(df.isnull().sum())

# Data Cleaning and Preprocessing
# Handle missing values, if necessary

# Perform sentiment analysis
nltk.download('vader_lexicon')  # Download the VADER lexicon
sid = SentimentIntensityAnalyzer()
df['Sentiment'] = df['Text'].apply(lambda x: sid.polarity_scores(x)['compound'])

# Visualize sentiment distribution
plt.figure(figsize=(8, 6))
plt.hist(df['Sentiment'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.title('Sentiment Distribution in Social Media Data')
plt.show()

# Generate and display a word cloud of positive and negative words
positive_words = ' '.join(df[df['Sentiment'] > 0]['Text'])
negative_words = ' '.join(df[df['Sentiment'] < 0]['Text'])

wordcloud_positive = WordCloud(width=800, height=400, background_color='white').generate(positive_words)
wordcloud_negative = WordCloud(width=800, height=400, background_color='white').generate(negative_words)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(wordcloud_positive, interpolation='bilinear')
plt.title('Positive Words')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(wordcloud_negative, interpolation='bilinear')
plt.title('Negative Words')
plt.axis('off')

plt.show()