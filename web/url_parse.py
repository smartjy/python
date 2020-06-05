from urllib.parse import urlparse

result = urlparse("https://docs.python.org/ko/3/library/index.html")

print(result)

# url 파싱 결과를 ParseResult 인스턴스를 반환
# ParseResult 클래스 속성의 의미
# scheme: URL에 사용된 프로토콜을 의미
# netloc: 네트워크 위치, user:password@host:port 형식으로 표현되며, HTTP 프로토콜인 경우 host:port 형식
# path: 파일이나 애플리케이션 경로 의미
# params: 애플리케이션에 전달될 매개변수
# query: 질의 문자열 또는 매개변수로 &로 구분된 이름=값 형식 표시
# fragment: 문서내의 앵커 등 조각을 지정 예 <a href="#앵">