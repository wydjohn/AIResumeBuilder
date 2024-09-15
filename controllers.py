import os
from dotenv import load_dotenv
import random
from pymongo import MongoClient

# Load environment variables
load_dotenv()

# Database connection setup
DATABASE_URL = os.getenv('DATABASE_URL')
db = MongoClient(DATABASE_URL)['your_db_name']

class UserManager:
    def __init__(self):
        self.users_collection = db['users']

    def create_user(self, user_data):
        self.users_collection.insert_one(user_data)
        print(f"User created successfully.")

    def update_user(self, user_id, updates):
        self.users_collection.update_one({'_id': user_id}, {'$set': updates})
        print(f"User updated successfully.")

    def delete_user(self, user_id):
        self.users_collection.delete_one({'_id': user_id})
        print(f"User deleted successfully.")

class ResumeManager:
    def __init__(self):
        self.resumes_collection = db['resumes']

    def upload_resume(self, user_id, resume):
        self.resumes_collection.insert_one({'user_id': user_id, 'resume': resume})
        print(f"Resume uploaded successfully.")

    def update_resume(self, resume_id, updates):
        self.resumes_collection.update_one({'_id': resume_id}, {'$set': updates})
        print(f"Resume updated successfully.")

    def delete_resume(self, resume_id):
        self.resumes_collection.delete_one({'_id': resume_id})
        print(f"Resume deleted successfully.")

class AISuggestionEngine:
    def __init__(self):
        pass

    def suggest_jobs(self, resume):
        job_suggestions = ["Software Developer", "Data Analyst", "System Administrator"]
        return random.choices(job_suggestions, k=3)

    def review_resume(self, resume):
        resume_feedback = ["Add more technical skills.", "Include relevant project descriptions."]
        return resume_feedback

# Example of how these classes could be used
if __name__ == "__main__":
    user_manager = UserManager()
    resume_manager = ResumeManager()
    ai_suggestion_engine = AISuggestionEngine()

    # Example user and resume data
    user_data = {"name": "John Doe", "email": "johndoe@example.com"}
    user_manager.create_user(user_data)

    resume = {"content": "Experienced software developer...", "format": "pdf"}
    resume_manager.upload_resume("john_doe_id", resume)

    print(ai_suggestion_engine.suggest_jobs(resume))
    print(ai_suggestion_engine.review_resume(resume))