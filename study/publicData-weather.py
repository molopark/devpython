import urllib.request as ul
import xmltodict
import json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
# 아톰에디터 한글사용을 위한 구문

url = "http://apis.data.go.kr/1360000/TourStnInfoService?serviceKey=rhQDlfFMowrdHmcifkhfvlyhS3reeXiggW2NfXrrR5xDceaGCtAlaA3uSwix87ZABqYn4pLGHD6diZHJH7kiTA%3D%3D&CURRENT_DATE=2018082700&HOUR=12&COURSE_ID=1&numOfRows=1"
# 데이터를 받을 url

request = ul.Request(url)
# url의 데이터를 요청함

response = ul.urlopen(request)
# 요청받은 데이터를 열어줌

rescode = response.getcode()
# 제대로 데이터가 수신됐는지 확인하는 코드 성공시 200
if (rescode == 200):
    responseData = response.read()
    # 요청받은 데이터를 읽음
    rD = xmltodict.parse(responseData)
    # XML형식의 데이터를 dict형식으로 변환시켜줌

    rDJ = json.dumps(rD)
    # dict 형식의 데이터를 json형식으로 변환

    rDD = json.loads(rDJ)
    # json형식의 데이터를 dict 형식으로 변환

    print(rDD)
    # 정상적으로 데이터가 출력되는지 확인

    w_data = rDD["response"]["body"]["items"]["item"]
    # 해당 dict형식의 파일의 item을 사용하기 편하도록 w_data에 저장

    print('관광지명 : ' + w_data["spotName"])
    print('시간 : ' + w_data["tm"])
    print('기온 : ' + w_data["th3"])
    if (w_data["sky"] == '1'):
        print('하늘상태 : 맑음')
    elif (w_data["sky"] == '2'):
        print('하늘상태 : 구름조금')
    elif (w_data["sky"] == '3'):
        print('하늘상태 : 구름많음')
    elif (w_data["sky"] == '4'):
        print('하늘상태 : 흐림')
    elif (w_data["sky"] == '5'):
        print('하늘상태 : 비')
    elif (w_data["sky"] == '6' or w_data["sky"] == '7'):
        print('하늘상태 : 눈비')
    elif (w_data["sky"] == '8'):
        print('하늘상태 : 눈')
    else:
        print('하늘상태 : ???')

    print('강수확률 : ' + w_data["pop"])
