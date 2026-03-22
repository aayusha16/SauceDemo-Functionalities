import csv
import os

def get_login_data():
    """Reads login_data.csv and returns a list of (username, password) tuples."""
    data = []
    # Construct path dynamically so it works from anywhere
    file_path = os.path.join(os.path.dirname(__file__), "..", "data", "login_data.csv")
    
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Optional: strip spaces and handle empty cells
            username = row['username'].strip() if row['username'] else ""
            password = row['password'].strip() if row['password'] else ""
            data.append((username, password))
    return data