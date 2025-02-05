# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 16:12:13 2025

@author: lenovo
"""

from flask import Flask, render_template
import folium

app = Flask(__name__)

@app.route('/')
def index():
    # 创建地图对象，中心点设为北京
    m = folium.Map(location=[39.9042, 116.4074], zoom_start=12)

    # 添加标记点（景点）
    places = [
        {
            "name": "天安门",
            "location": [39.9037, 116.3975],
            "description": "天安门是北京的标志性建筑，位于北京市中心。"
        },
        {
            "name": "故宫",
            "location": [39.9163, 116.3972],
            "description": "故宫是中国明清两代的皇家宫殿，现为故宫博物院。"
        },
        {
            "name": "颐和园",
            "location": [39.9997, 116.2754],
            "description": "颐和园是中国清朝时期的皇家园林，以昆明湖和万寿山著称。"
        },
        {
            "name": "长城",
            "location": [40.4319, 116.5704],
            "description": "长城是中国古代的军事防御工程，是世界文化遗产。"
        }
    ]

    # 在地图上添加标记
    for place in places:
        folium.Marker(
            location=place["location"],
            popup=f"<b>{place['name']}</b><br>{place['description']}",
            tooltip=place["name"]
        ).add_to(m)

    # 保存地图为 HTML 文件
    m.save('templates/map.html')

    # 渲染地图页面
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True)