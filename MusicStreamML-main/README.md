# MusicStreamML
# My Music Recommendation Project README

## Overview

Welcome to my personalized music recommendation project! This project is a labor of love where I delve into the realms of music data, machine learning, and web development to create a personalized music streaming experience for users. Here's a breakdown of what I've been up to:

---

## Phase #1: Data Extraction and Feature Extraction with Librosa

I started by diving into the Free Music Archive (FMA) dataset and extracting valuable audio features using the Librosa module. My focus was on extracting Mel-Frequency Cepstral Coefficients (MFCC), which are crucial for representing audio in a machine-readable format. Once extracted, I saved all the data in a convenient pickle (pkl) file for easy access and manipulation.

## Phase #2: MongoDB Integration

Next, I seamlessly integrated the pickle file into MongoDB, ensuring scalability and accessibility of the dataset. MongoDB provides a robust platform for storing and managing large volumes of data, making it the perfect choice for my project.

## Phase #3: Data Transformation with PySpark

With the data securely stored in MongoDB, I utilized PySpark to read the audio features and transform them into a structured format suitable for machine learning inputs. This involved cleaning the data, handling missing values, and encoding categorical variables to prepare it for the next phase.

## Phase #4: Exploring Machine Learning Algorithms

Here comes the fun part! I experimented with various machine learning algorithms, including Approximate Nearest Neighbors (ANN), Locality-Sensitive Hashing (LSH), K-Means Clustering, K-Nearest Neighbors (KNN), and ANN. Each algorithm brought its own unique approach to music recommendation, and I meticulously evaluated their performance to determine the best fit for my project.

## Phase #5: Flask Integration for Web Deployment

Now, it was time to bring my recommendation model to life! I integrated the selected algorithm into a Flask web application, creating an interactive music streaming platform. Users can enjoy their favorite tunes while receiving personalized recommendations based on their listening history. It's a seamless experience that enhances user engagement and satisfaction.

## Conclusion

This project has been an exciting journey, blending data science, machine learning, and web development to create a personalized music recommendation system. I'm thrilled with the results and eager to share my creation with the world. If you have any questions or want to learn more about my project, feel free to reach out!

---

*Note: If you have any questions or need further clarification on any aspect of my project, please don't hesitate to ask!*
