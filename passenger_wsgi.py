import sys, os

# Set up the path to your app
sys.path.append(os.getcwd())

# Import your Flask instance
# Note: 'app' is the name of your variable in app.py
from app import app as application