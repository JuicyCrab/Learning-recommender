# Learning Resource Recommender

A personalized learning path generator that removes the stress of finding where to start. Instead of overwhelming users with resources, this system curates a tight, sequenced path of high-quality materials tailored to what the user already knows and where they want to go.

The Problem
Starting to learn something new is hard — not because resources don't exist, but because there are too many. Decision fatigue kills momentum before learning even begins. This project flips that model: the user states a goal, the system builds the path.
How It Works
The system combines four ML components to generate personalized recommendations:

Knowledge Graph — models concepts and their prerequisite relationships for a given domain
Sentence Embeddings + FAISS — matches resources to concepts semantically without expensive LLM API calls
Bayesian Knowledge Tracing — infers what the user likely knows based on their behavior, updating in real time
Collaborative Filtering — surfaces patterns from other learners once sufficient interaction data exists

Current Domain
Binary Classification with scikit-learn
Tech Stack

Python, FastAPI, NetworkX, sentence-transformers, FAISS, PyTorch, React
