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
        self.insert_user_details(user_details)
        self.confirm_action("User created successfully.")

    def insert_user_details(self, user_details):
        self.users_collection.insert_one(user_details)

    def update_user_by_id(self, user_id, updated_details):
        self.perform_user_update(user_id, updated_details)
        self.confirm_action("User updated successfully.")

    def perform_user_update(self, user_id, updated_details):
        self.users_collection.update_one({'_id': user_id}, {'$set': updated_details})

    def delete_user_by_id(self, user_id):
        self.perform_user_deletion(user_id)
        self.confirm_action("User deleted successfully.")

    def perform_user_deletion(self, user_id):
        self.users_collection.delete_one({'_id': user_id})

    def confirm_action(self, message):
        print(message)

class ResumeManager:
    def __init__(self):
        self.resumes_collection = database['resumes']

    def upload_user_resume(self, user_id, resume_details):
        self.insert_resume_details(user_id, resume_details)
        self.confirm_action("Resume uploaded successfully.")

    def insert_resume_details(self, user_id, resume_details):
        self.resumes_collection.insert_one({'user_id': user_id, 'resume': resume_details})

    def update_resume_by_id(self, resume_id, updated_resume_details):
        self.perform_resume_update(resume_id, updated_resume_details)
        self.confirm_action("Resume updated successfully.")

    def perform_resume_update(self, resume_id, updated_resume_details):
        self.resumes_collection.update_one({'_id': resume_id}, {'$set': updated_resume_details})

    def delete_resume_by_id(self, resume_id):
        self.perform_resume_deletion(resume_id)
        self.confirm_action("Resume deleted successfully.")

    def perform_resume_deletion(self, resume_id):
        self.resumes_collection.delete_one({'_id': resume_id})

    def confirm_action(self, message):
        print(message)

class AIResumeSuggestionEngine:
    def __init__(self):
        pass

    def suggest_potential_jobs(self, resume_data):
        job_suggestions_pool = ["Software Developer", "Data Analyst", "System Administrator"]
        suggested_jobs = self.random_job_selection(job_suggestions_pool, 3)
        return suggested_jobs

    def random_job_selection(self, job_pool, number_of_jobs):
        return random.choices(job_pool, k=number_of_jobs)

    def provide_resume_feedback(self, resume_data):
        feedback_suggestions = self.generate_feedback_suggestions()
        return feedback_suggestions

    def generate_feedback_suggestions(self):
        return ["Add more technical skills.", "Include relevant project descriptions."]

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