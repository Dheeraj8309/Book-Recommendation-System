# Book-Recommendation-System
Book Recommendation System
This project is a web-based Book Recommendation System built using Python, Flask, and a k-Nearest Neighbors (k-NN) machine learning model. It suggests books to users based on the principles of item-based collaborative filtering.

<!-- Optional: Add a screenshot of your app -->

How It Works
The recommendation engine works by finding books that have been rated similarly by a large group of users. When a user selects a book they like, the system identifies the top 5 books that are most similar to it based on the rating patterns stored in the dataset.

The core logic is built in the Book.ipynb Jupyter Notebook and deployed as a web application using the Flask framework.

Features
Item-Based Collaborative Filtering: Recommends books based on the similarity between items (books), calculated from user rating data.

Interactive Web Interface: A simple and clean user interface built with Flask and HTML/CSS allows users to select a book and receive recommendations.

Pre-Trained Model: The k-NN model is pre-trained and saved using pickle, allowing for fast, real-time recommendations without retraining.

Filtered Dataset: The model is trained on a filtered subset of the Book-Crossing dataset to ensure recommendation quality, focusing on users from the USA and Canada with significant rating activity.

Technology Stack
Backend: Python, Flask

Machine Learning: Scikit-learn, Pandas, NumPy

Frontend: HTML, CSS

Notebook: Jupyter Notebook

How to Run This Project Locally
To run this project on your own machine, follow these steps:

Prerequisites
Python 3.x installed

Pip (Python package installer)

1. Clone the Repository
git clone [https://github.com/your-username/Book-Recommendation-System.git](https://github.com/your-username/Book-Recommendation-System.git)
cd Book-Recommendation-System/Flask

2. Install Dependencies
Install the required Python libraries using pip:

pip install flask pandas scikit-learn

3. Run the Flask Application
Navigate to the Flask directory and run the main application file:

python app1.py

4. View
