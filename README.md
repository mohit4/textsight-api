![TextSight - Opinion Mining API](images/textsight.png)

# textsight-api
An opinion mining API developed using Django rest framework to process text using NLP

## Idea

The idea is to have an application that allow its users to perform Natural Language Processing on the text and store data on server side.

### What is Natural Language Processing ?

Natural Language Processing, usually shortened as NLP, is a branch of artificial intelligence that deals with the interaction between computers and humans using the natural language. The ultimate objective of NLP is to read, decipher, understand, and make sense of the human languages in a manner that is valuable. For more information : ![Check out this article](https://becominghuman.ai/a-simple-introduction-to-natural-language-processing-ea66a1747b32)

### What is the valuable information that can be achieved from the text ?

There are many vital information that can be extracted from a text after processing it.
For the purpose of this application we will be interested in the below information only.

* **Polarity** : Determines wheather a text is negative or positive. A text can also have a polarity score to determine how much negative or positive it is. This score is usually a value between 0 and 1.

* **Subjectivity** : Determines wheather a text is subjective or objective. A text can also have a subjectivity score to detemine how much subjective or objective it is. This score is usually a value between 0 and 1.

* **Tags** : Tags are keywords that can relate a text with a specific noun, an entity, which can be used to summarize or classify the text in a specific category.

## Technologies Used

1. **Python** : Primary programming language for this application. Version 3.8 will be used for the development.
2. **Django** : Django framework will be used to create the back-end of the application.
3. **Rest Framework** : Rest Framework is used along with Django to develop the Rest API Architecture.
4. **TextBlob** : Text Blob package from python will be used to perform Natural Language Processing.

## API References

Base URL : https://localhost:8000/textsight-api/

### API Heirarchy

    /textanalyze
        /add

### Details

| Reference | Method | Purpose |
| --- | --- | --- |
| /textanalyze/add | POST | Will accept text parameter, process and stores it on server, also returns the basic text analysis results |

## High Level Design for Development

## Project setup