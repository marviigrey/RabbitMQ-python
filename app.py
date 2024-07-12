import os
from flask import Flask, request
import logging
from datetime import datetime
from tasks import send_email

app = Flask(__name__)

# Set log file path to the current directory
log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'messaging_system.log')

# Configure logging
logging.basicConfig(filename=log_file_path, level=logging.INFO)

@app.route('/')
def index():
    if 'sendmail' in request.args:
        recipient = request.args.get('sendmail')
        message = request.args.get('message', 'Default message text')  # Add default message if message param not provided
        send_email.delay(recipient, message)
        return f'Email will be sent to {recipient}', 200
    elif 'talktome' in request.args:
        logging.info(f'Log time: {datetime.now()}')
        return 'Time logged.', 200
    return 'Invalid parameters.', 400

if __name__ == '__main__':
    app.run()

