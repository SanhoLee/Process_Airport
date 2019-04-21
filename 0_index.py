#!/usr/local/bin/python3
print("Content-Type: text/html")
print()                             
import cgi
form = cgi.FieldStorage()           #query string, url에서 ? 표시 이후에 나오는 문자열에 대해서 질의에 대한 작업을 하기 위해 작성함.
print('<link type="text/css" rel="stylesheet" href="style_sheet1.css" >')

if 'id' in form:
    pageId = form["id"].value
    description = open('data_a/'+pageId,'r').read()
else:
    pageId = ''
    description = '''
          <h2>사작하기 전에!!</h2>
            <ul>
              <li>이제부터 여권이 곧 신분증 역할을 하게 됩니다. 잘 가지고 다니셔야됩니다.</li>
              <li>비행기에 탈때는 생수, 음료 등등 가지고 탈수 없어요. 그러니깐 체크인(티켓발권)하고 들어가기 전에 모두 마시거나 버려야 합니다.</li>
              <li>위탁수화물은 캐리어(짐)를 미리 붙일때 사용하는 용어
              <li>라이터, 보조배터리, 칼 등 위험한 물건은 위탁수화물에 들어있으면 안되요. 특히 보조배터리는 필요할 경우 붙이지 말고, 가지고 타세요.</li>
              <li>자, 그럼 순서대로 편안하게 보세요.</li>
            </ul>
        <img src="https://www.airport.co.kr/uploads/CONTENTS/2018/08/CONTENTS_2018081617124683393921370.jpg" >
    '''

print('''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://afeld.github.io/emoji-css/emoji.css" rel="stylesheet">
    </head>
    <body>
      <h1><a href="0_index.py"><i class="em em-house"></i>공항 사용설명서 (김해공항)<i class="em em-airplane"></i></a></h1>
      <div id="grid">
        <ol>
            <li><a href="0_index.py?id=1">국제선 출국장</a></li>
            <li><a href="0_index.py?id=2">환전/와이파이/체크인</a></li>
            <li><a href="0_index.py?id=3"><i class="em em-kr"></i>출국수속</a></li>
            <li><a href="0_index.py?id=4">탑승 게이트</a></li>
            <li><a href="0_index.py?id=5"><i class="em em-airplane"></i>여행자 정보작성</a></li>
            <li><a href="0_index.py?id=6"><i class="em em-jp"></i>입국심사</a></li>
            <li><a href="0_index.py?id=7"><i class="em em-jp"></i> 입국</a></li>
        </ol>
        <div id="desc">
        {desc}
        <p></p>
        </div>
      </div>
      
      <footer>
        made by fwanggus in Tokyo.&#128054
      </footer>
    </body>
</html>
'''.format(pageid=pageId, desc=description))