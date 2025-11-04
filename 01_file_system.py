# ek specific folder me jitni bhi files hn unka naam and last modification

import os
from datetime import datetime

# Specify the folder path
folder_path = r'C:\Users\Noor Links\OneDrive\Desktop\Picture\Editing'

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # Check if it's a file (not a folder)
    if os.path.isfile(file_path):
        # Get last modified time
        modified_time = os.path.getmtime(file_path)
        
        # Convert timestamp to readable format
        readable_time = datetime.fromtimestamp(modified_time).strftime('%Y-%m-%d %H:%M:%S')
        
        print(f"{filename} — Last Modified: {readable_time}")
the End 
