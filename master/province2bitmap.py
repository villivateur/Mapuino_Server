data_map = {
    "新疆": (0, 0),
    "黑龙": (0, 2),
    "辽宁": (0, 4),
    "天津": (0, 6),
    "甘肃": (0, 8),
    "陕西": (0, 10),
    "河北": (0, 12),
    "河南": (0, 14),
    "四川": (0, 16),
    "湖北": (0, 18),
    "江苏": (0, 20),
    "贵州": (0, 22),
    "江西": (0, 24),
    "上海": (0, 26),
    "广东": (0, 28),
    "海南": (0, 30),
    "香港": (1, 0),
    "World": (1, 2),
    "内蒙": (0, 1),
    "吉林": (0, 3),
    "北京": (0, 5),
    "青海": (0, 7),
    "宁夏": (0, 9),
    "山西": (0, 11),
    "山东": (0, 13),
    "西藏": (0, 15),
    "重庆": (0, 17),
    "安徽": (0, 19),
    "云南": (0, 21),
    "湖南": (0, 23),
    "浙江": (0, 25),
    "广西": (0, 27),
    "福建": (0, 29),
    "澳门": (0, 31),
    "台湾": (1, 1),
}

def province2bitmap(province_name):
    try:
        return data_map[province_name]
    except KeyError:
        return data_map["World"]
