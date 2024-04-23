import requests
from datetime import datetime

def get_meals(dt):
    p = {
        'Type' : 'json',
        'ATPT_OFCDC_SC_CODE' : 'J10',
        'SD_SCHUL_CODE' : '7530167',
        'MLSV_YMD' : dt
    }

    url = 'https://open.neis.go.kr/hub/mealServiceDietInfo'
    result = requests.get(url, params = p)

    try:
        if result.status_code == 200:
            meals = result.json()
            meal = meals['mealServiceDietInfo'][1]['row'][0]['DDISH_NM']
        else:
            meal = ''
        return meal
    except:
        return ''

date = datetime.today()
date = str(date)[0:10].split('-')
date = date[0] + date[1] + date[2]

meal = get_meals(dt= date)

if meal == '':
    print("자료가 없습니다")
else:
    m = str(meal).replace('<br/>', '\n')
    print(m)
