# SHL Assessment Recommendation API

This is the backend API for the SHL Assessment Recommendation System. It accepts a job description or a natural language query and returns 1–10 relevant SHL assessment recommendations using content-based filtering.

## 🚀 Features

- Accepts POST requests with a query string.
- Returns assessment details like name, URL, duration, remote/adaptive support, and test type.
- Content-based recommendation using cosine similarity.
- Hosted on Render.

## 🔗 API Endpoint

https://shl-backend-nw.on  render.com/recommend/ 
Post Request and inside body
{
    "query":"data science and python"

}
Response:    {
        "Assessment Name": "Data Science Assessment",
        "URL": "https://www.shl.com/en/assessments/technical-coding/",
        "Remote Testing Support": "Yes",
        "Adaptive/IRT Support": "Yes",
        "Duration (minutes)": "60",
        "Test Type": "Technical",
        "Score": 0.672
    },
    {
        "Assessment Name": "Technical Test – Python",
        "URL": "https://www.shl.com/en/assessments/technical-coding/",
        "Remote Testing Support": "Yes",
        "Adaptive/IRT Support": "Yes",
        "Duration (minutes)": "45",
        "Test Type": "Technical",
        "Score": 0.358
    }
]

🧠 Tools & Libraries Used
Python 3.11

Django 4+

Django REST Framework

Scikit-learn

Pandas

NLTK

Render (for deployment)
📊 Evaluation Metrics
The model was tested on sample queries and achieved:

Mean Recall@3: 0.90

MAP@3: 0.90

Evaluation script is available in metrics_evaluation/evaluate.py.

