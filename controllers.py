import os
from dotenv import load_dotenv
import random
load_dotenv()
from pymongo import MongoClient
db = MongoClient(os.getenv('DATABASE_URL'))['your_db_name']
class UserManager:
    def __init__(self):
        self.users_collection = db['users']
    def create_user(self, user_data):
        self.users_collection.insert_one(user_data)
        print("User created successfully.")
    def update_user(self, user_id, updates):
        self.users_collection.update_one({'_id': user_id}, {'$set': updates})
        print("User updated successfully.")
    def delete_user(self, user_id):
        self.users_collection.delete_one({'_id': user_id})
        print("User deleted successfully.")
class ResumeManager:
    def __init__(self):
        self.resumes_collection = db['resumes']
    def upload_resume(self, user_id, resume):
        self.resumes_collection.insert_one({'user_id': user_id, 'resume': resume})
        print("Resume uploaded successfully.")
    def update_resume(self, resume_id, updates):
        self.resumes_collection.update_one({'_id': resume_id}, {'$set': updates})
        print("Resume updated successfully.")
    def delete_resume(self, resume_id):
        self.resumes_collection.delete_one({'_id': resume_id})
        print("Resume deleted successfully.")
class AISuggestionEngine:
    def __init__(self):
        pass
    def suggest_jobs(self, resume):
        job_suggestions = ["Software Developer", "Data Analyst", "System Administrator"]
        return random.choices(job_suggestions, k=3)
    def review_resume(self, resume):
        resume_feedback = ["Add more technical skills.", "Include relevant project descriptions."]
        return resume_feedback