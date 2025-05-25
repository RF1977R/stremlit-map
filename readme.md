# Streamlit登山マップ

このアプリは複数の山行を動的に切り替えて表示できるStreamlitベースの登山記録ビューアです。

- `/app/map_viewer.py`: メインの表示アプリ
- `/data/<山行名>/`: GPXと写真を格納
- クエリパラメータ `?course=gozaisyo2022` で対象山行を切り替え

## 起動方法
```
python launcher.py [コース名]
# または：
streamlit run app/map_viewer.py