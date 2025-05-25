import os
import subprocess
import sys

# course name from argument or default
course = sys.argv[1] if len(sys.argv) > 1 else "gozaisyo2022"
os.environ["MAP_COURSE"] = course

subprocess.run([
    "streamlit", "run", "app/map_viewer.py",
    "--server.port=8501",
    "--server.address=0.0.0.0"
])
