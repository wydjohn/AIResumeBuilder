import os
from dotenv import load_dotenv
import random
from pymongo import MongoClient

load_dotenv()

DATABASE_CONNECTION_STRING = os.getenv('DATABASE_URL')
database = MongoClient(DATABASE_CONNECTION_STRING)['your_db_name']

class UserManager:
    def __init__(self):
        self.users_collection = database['users']

    def create_user(self, user_details):
        self.users_collection.insert_one(user_details)
        print(f"User created successfully.")

    def update_user_by_id(self, user_id, updated_details):
        self.users_collection.update_one({'_id': user_id}, {'$set': updated_details})
        print(f"User updated successfully.")

    def delete_user_by_id(self, user_id):
        self.users_collection.delete_one({'_id': user_id})
        print(f"User deleted successfully.")

class ResumeManager:
    def __init__(self):
        self.resumes_collection = database['resumes']

    def upload_user_resume(self, user_id, resume_details):
        self.resumes_collection.insert_one({'user_id': user_id, 'resume': resume_details})
        print(f"Resume uploaded successfully.")

    def update_resume_by_id(self, resume_id, updated_resume_details):
        self.resumes_collection.update_one({'_id': resume_id}, {'$set': updated_resume_details})
        print(f"Resume updated successfully.")

    def delete_resume_by_id(self, resume_id):
        self.resumes_collection.delete_one({'_id': resume_id})
        print(f"Resume deleted successfully.")

class AIResumeSuggestionEngine:
    def __init__(self):
        pass

    def suggest_potential_jobs(self, resume_data):
        job_suggestions_pool = ["Software Developer", "Data Analyst", "System Administrator"]
        suggested_jobs = random.choices(job_suggestions_pool, k=3)
        return suggested_jobs

    def provide_resume_feedback(self, resume_data):
        feedback_suggestions = ["Add more technical skills.", "Include relevant project descriptions."]
        return feedback_suggestions

if __name__ == "__main__":
    userManager = UserManager()
    resumeManager = ResumeManager()
    aiSuggestionEngine = AIResumeSuggestionEngine()

    newUserDetails = {"name": "John Doe", "email": "johndoe@example.com"}
    userManager.create_user(newUserDetails)

    resumeDetails = {"content": "Experienced software developer...", "format": "pdf"}
    resumeManager.upload_user_resume("john_doe_id", resumeDetails)

    print(aiSuggestionEngine.suggest_potential_jobs(resumeDetails))
    print(aiSuggestionEngine.provide_resume_feedback(resumeDetails))