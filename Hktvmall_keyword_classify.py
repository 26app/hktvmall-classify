def long_grain(text):
    if '茉莉香米' in text or '頂級香米' in text or '茉莉銀絲香米'in text or '絲苗米' in text:
        return '101'
    else:
        return '199'
def short_grain(text):
    if '珍珠米' in text or '短身米' in text or '珍珠白米' in text:
        return '101'
    else:
        return '199'
def spaghetti(text):
    if '扁意粉' in text or '扁意大利粉' in text or '意大利' in text or '意大利意粉' in text or '扁身意粉' in text or '意粉' in text:
        return '101'
    else:
        return '199'
def macaroni(text):
    if '螺絲粉' in text or '直通粉' in text or '通心粉' in text or '通粉' in text or '蜆殼粉' in text or '扭扭粉' in text:
        return '101'
    else:
        return '199'
def noodle(text):
    if '蝦子麵' in text or '關廟麵' in text or '刀削麵' in text or '瑤柱麵' in text or '養生麵條' in text or '彈牙麵' in text or '有機麵線' in text or '有機紅藜麥麵' in text or '擔仔麵' in text or '全蛋麵' in text or '菠菜麵' in text or '蒟蒻麵' in text:
        return '101'
    else:
        return"199"
'''
def instant_noodles(text):
    #if '印尼撈麵' in text or '麻油麵' in text or '麻油味麵' in text or '麻油' in text or '豬骨湯麵' in text or '豬骨' in text or '拌麵' in text or '牛骨湯麵' in text or '芝士拉麵' in text or '麻醬拌麵' in text:
    if '印尼撈麵' in text:
        return '101'
    elif '麻油麵'in text or '麻油味麵' in text or '麻油' in text:
        return '102'
    elif '豬骨湯麵' in text or '豬骨' in text:
        return '103'
    elif '椒麻拌麵' in text:
        return '104'
    elif '牛骨湯麵' in text:
        return '105'
    elif '芝士拉麵' in text:
        return '106'
    elif '麻醬拌麵' in text:
        return '107'
    elif '麵' in text:
        return '199'
    else:
        return""

def oats_and_cereals(text):
    if '燕麥片' in text or '燕麥方脆'in text or '營養麥' in text or '麥片' in text or '燕麥糠' in text:
        return '101'
    elif '麥米片' in text or '玉米片' in text or '粟米片' in text:
        return '102'
    elif '美祿可可' in text or '蜂蜜星星' in text or '可可脆片' in text:
        return '103'
    else:
        return '199'
def flour_and_pancake_mix(text):
    if '高筋麵粉' in text or '高筋' in text:
        return '101'
    elif '低筋麵粉' in text or '低筋' in text:
        return '102'
    elif '小麥麵粉' in text or '小麥' in text or '法國全麥麵粉' in text or '法國麵粉' in text or '全麥' in text:
        return '103'
    elif '中筋' in text or '中筋麵粉' in text:
        return '104'
    else:
        return '199'
def frozen_seafood(text):
    if '左口魚' in text:
        return '101'
    elif '鯛魚柳' in text:
        return '102'
    elif '吞拿魚' in text:
        return '103'
    elif '希靈魚' in text:
        return '104'
    elif '鯛魚' in text:
        return '105'
    elif '鯖魚' in text:
        return '106'
    elif '三文魚' in text:
        return '107'
    elif '油甘魚' in text:
        return '108'
    else:
        return '199'
'''


