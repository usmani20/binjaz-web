import sys
import os
import traceback

# Hardwire the path to your new app directory
app_directory = os.path.dirname(__file__)
if app_directory not in sys.path:
    sys.path.insert(0, app_directory)

try:
    # Attempt to load your Flask app
    from app import app as application
except Exception:
    # If it crashes, catch the error and print it to the screen
    error_trace = traceback.format_exc()


    def application(environ, start_response):
        start_response('500 Internal Server Error', [('Content-Type', 'text/plain')])
        return [b"PYTHON CRASH REPORT:\n\n", error_trace.encode('utf-8')]