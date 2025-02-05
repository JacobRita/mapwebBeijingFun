# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 11:05:32 2025

@author: lenovo
"""

from flask import Flask, render_template
import folium

app = Flask(__name__)

# 北京市的经纬度
beijing_coords = [39.9042, 116.4074]

# 景点信息
attractions = [
    {"name": "故宫", "coords": [39.9163, 116.3972], "info": "故宫是中国明清两代的皇家宫殿。"},
    {"name": "天安门", "coords": [39.9042, 116.3975], "info": "天安门是中华人民共和国的象征。"},
    {"name": "颐和园", "coords": [39.9997, 116.2754], "info": "颐和园是中国清朝时期皇家园林。"},
    {"name": "长城", "coords": [40.4319, 116.5704], "info": "长城是中国古代的军事防御工程。"},
]

@app.route('/')
def index():
    # 创建地图对象
    m = folium.Map(location=beijing_coords, zoom_start=12)

    # 在地图上添加景点标记
    for attraction in attractions:
        folium.Marker(
            location=attraction["coords"],
            popup=folium.Popup(attraction["info"], max_width=300),
            tooltip=attraction["name"]
        ).add_to(m)

    # 将地图保存为HTML文件
    m.save('templates/map.html')


    return render_template('map.html')

if __name__ == '__main__':
    root_path = app.root_path
    print(root_path)
    app.run(debug=True)