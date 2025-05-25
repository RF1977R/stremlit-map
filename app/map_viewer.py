import streamlit as st
import gpxpy
import os
import json
from pathlib import Path
from PIL import Image
import base64
from io import BytesIO
import folium
from streamlit_folium import st_folium

def get_course():
    query = st.experimental_get_query_params()
    if "course" in query:
        return query["course"][0]
    return os.environ.get("MAP_COURSE", "gozaisyo2022")

course = get_course()
data_path = Path("data") / course

# meta info
meta_path = data_path / "meta.json"
if meta_path.exists():
    meta = json.load(open(meta_path))
    st.title(meta.get("title", course))
    st.markdown(meta.get("description", ""))
else:
    st.title(course)

# GPX load
track_path = data_path / "track.gpx"
if not track_path.exists():
    st.error("GPXファイルが見つかりません")
    st.stop()

with open(track_path, "r") as f:
    gpx = gpxpy.parse(f)

coords = [(p.latitude, p.longitude)
          for t in gpx.tracks
          for s in t.segments
          for p in s.points]

m = folium.Map(location=coords[len(coords)//2], zoom_start=13)
folium.PolyLine(coords, color='blue').add_to(m)

photo_dir = data_path / "photos"
for photo_file in sorted(photo_dir.glob("*.jpg")):
    try:
        img = Image.open(photo_file)
        img.thumbnail((300, 300))
        buf = BytesIO()
        img.save(buf, format="JPEG")
        img64 = base64.b64encode(buf.getvalue()).decode()
        img_html = f'<img src="data:image/jpeg;base64,{img64}" width="300">'
        folium.Marker(coords[len(coords)//2], popup=img_html,
                      icon=folium.Icon(color='orange', icon='camera', prefix='fa')).add_to(m)
    except Exception as e:
        st.warning(f"画像処理エラー: {photo_file.name} - {e}")

st_folium(m, width=700, height=500)
