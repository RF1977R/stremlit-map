import subprocess
import sys
import os

mount_name = sys.argv[1]
streamlit_bin = "/root/myenv/bin/streamlit"
if "--streamlit-bin" in sys.argv:
    idx = sys.argv.index("--streamlit-bin")
    streamlit_bin = sys.argv[idx + 1]

app_path = os.path.join("app", "map_viewer.py")

subprocess.run([
    streamlit_bin,
    "run",
    app_path,
    "--server.port=8501",
    "--server.address=0.0.0.0"
], env={**os.environ, "MAP_ID": mount_name})
