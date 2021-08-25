# Topic-Modeling-on-Jeopardy-Trivia

Applied NLP techniques (NMF, TFI-IDF, topic-modeling) to discover latent meta-categories from 200k+ questions in the Jeopardy! archives.

## The Goal

**The goal of this analysis is to apply NLP techniques to categorize Jeopardy! questions into meta-categories. These will help form a study app that home viewers and aspirign contestants can use to study -- or just have fun! **

## Background

Jeopardy is a trivia gameshow where contestants are presented with [general knowledge](https://en.wikipedia.org/wiki/General_knowledge) clues in the form of answers, and must phrase their responses in the form of questions. Clues are concealed under varying dollar amounts on the game board, ostensibly reflecting varying levels difficulty, and come from different categories. Popular categories include Literature, Science, Word Origins, and Before & After, a tricky category that asks users to combine clues and answers. 

![img](/Users/elizabethnaameh/Desktop/Topic-Modeling-on-Jeopardy-Trivia/images/jeopardy_board.png)



## Key Terms

- **Clue**: What I will be calling a question-answer combination. A single clue instance can be considered as a text document
- **J-Category**: The "Jeopardy!" defined category. In the image above, 'BEFORE & AFTER', 'SAY "WH"', etc are the J-Categories of one round
- **Meta-category**: An overarching topic that can describe each clue's context, also referred to as a **hidden theme**. For example, the J-Category "BEFORE & AFTER" seen above might belong to potential meta-categories "Literature" and "History". In data-science, we can also think of a meta-category as a **latent topic**.

## The Data

The [original dataset](https://drive.google.com/file/d/0BwT5wj_P7BKXUl9tOUJWYzVvUjA/view?resourcekey=0-uFrn8bQkUfSCvJlmtKGCdQ) is a .csv file and has 216,929 rows and 7 columns. Each row contains the information pertaining to a single clue per episode from 1984 until 2021. 

## Algorithms

- *Text Pre-processing*: I used lemmatization, part-of-speech tagging and custom stopword removal to filter words. I then used regex expressions to remove punctuation, and dropped clues that included images or video. 
- *Vectorize Text:* used a tf-idf (Term Frequency * Inverse Document Frequency) to vectorize the text from each clue. In other words, I turned the raw text from the "Jeopardy!" questions and answers into a matrix whose entries are the numerical tf-idf features of each word in the text.
- *Dimensionality Reduction:* I then used Non-Negative Matrix Factorization (NMF) to create clusters of words, where each cluster can be thought of as a *meta-category* or latent topic, which is one of the goals of this analysis.

## Tools

* Numpy & Pandas for data processing 
* Matplotlib, WordCloud for visualization
* Scikit-learn for machine learning
* NLTK for natural language processing

## Results

 Initial data exploration revealed the most popular categories:

![img](/Users/elizabethnaameh/Desktop/Topic-Modeling-on-Jeopardy-Trivia/images/Jcategories_barplot.png)

In total, there are 27,295 actual Jeopardy categories from 1984 until 2012. From these, my analysis constructed 13 decently cohesive meta-catogies in the dataset such as PEOPLE, FILM & TV, WORDS, and HISTORY. 

Below is a wordcloud based on terms appearing in the CITY meta-category, along with two representative clues:

![img](/Users/elizabethnaameh/Desktop/Topic-Modeling-on-Jeopardy-Trivia/images/wordcloud_city.png)

* "4 treaties to mitigate the horrors of war were signed in this city in August, 1949." ('What is Geneva')
* "The last of the 13 colonies to be founded, its ‘Mother City’, Savannah, was settled in 1733." (What is Georgia)

As another example, take the 'BOOKS' meta-category:

![img](/Users/elizabethnaameh/Desktop/Topic-Modeling-on-Jeopardy-Trivia/images/wordcloud_books.png)

The top Produce item is Bananas by far, and organic produce is very popular, with 15 of the top 20 products being organic.

* Weakened by scarlet fever, Beth March was sentenced to death by this author.
* In a 14-line poem Wordsworth wrote "Scorn not" this form of poetry.

You can interact with the live Jeopardy! Quiz Game app here. 
