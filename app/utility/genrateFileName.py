import os
from datetime import datetime

def generateFileName(file_name):
    name, ext = os.path.splitext(file_name)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")  # e.g., "20250511143720"
    return f"{name}_{timestamp}.{ext}"
