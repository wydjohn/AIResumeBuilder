# Importing necessary libraries and modules from Django
from django.db import models
import os
from dotenv import load_dotenv

# Loading environment variables from .env file
load_dotenv()

class UserProfile(models.Model):
    """Model to represent a user profile with basic attributes including unique username and email."""
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    account_creation_date = models.DateTimeField(auto_now_add=True)

    # Method to return a string representation of the user
    def __str__(self):
        return self.username

class ResumePost(models.Model):
    """Model to represent a resume post with a title, content and relation to the author."""
    title = models.CharField(max_length=200)
    content = models.TextField()
    resume_author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="resume_posts")
    post_date = models.DateTimeField(auto_now_add=True)
    
    # Method to return a string representation of the post
    def __str__(self):
        return f'Resume for {self.resume_author.username}: {self.title}'

# Database configuration settings using environment variables
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DATABASE_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.getenv('DATABASE_NAME', 'ai_resumebuilder_db'),
        'USER': os.getenv('DATABASE_USER', 'dbadmin'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', 'securepassword'),
        'HOST': os.getenv('DATABASE_HOST', 'localhost'),
        'PORT': os.getenv('DATABASE_PORT', '5432'),
    }
}