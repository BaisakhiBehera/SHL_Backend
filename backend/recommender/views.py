import os
import pandas as pd
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

@api_view(['POST'])
def recommend_assessments(request):
    try:
        # 1. Load the CSV
        csv_path = os.path.join(settings.BASE_DIR, 'data', 'assessments.csv')
        df = pd.read_csv(csv_path)

        # 2. Get input query
        user_query = request.data.get('query', '')
        if not user_query:
            return Response({"error": "Query not provided."}, status=status.HTTP_400_BAD_REQUEST)

        # 3. Combine relevant text fields for better matching
        df['combined_text'] = df['Assessment Name'].astype(str) + ' ' + df['Test Type'].astype(str)

        # 4. TF-IDF vectorization
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(df['combined_text'])
        query_vec = vectorizer.transform([user_query])

        # 5. Cosine similarity
        similarity = cosine_similarity(query_vec, tfidf_matrix).flatten()

        # 6. Filter results using a threshold
        threshold = 0.1
        top_indices = [i for i in similarity.argsort()[::-1] if similarity[i] >= threshold][:10]

        if not top_indices:
            return Response({"message": "No relevant assessments found."}, status=status.HTTP_200_OK)

        # 7. Prepare results
        results = df.iloc[top_indices][[
            'Assessment Name', 'URL', 'Remote Testing Support',
            'Adaptive/IRT Support', 'Duration (minutes)', 'Test Type'
        ]].copy()

        # (Optional) Include similarity score for transparency/debugging
        results['Score'] = [round(similarity[i], 3) for i in top_indices]

        return Response(results.to_dict(orient='records'))

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
