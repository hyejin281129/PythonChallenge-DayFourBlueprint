import os
import requests

# 다시 시작할 건지 질문하기
def question():
  quest = input("Do you want to start over? y/n ")
  if quest == "y":
    # 초기화
    os.system('clear')
    boilerplate(site)
  elif quest == "n":
    print("ok bye!")
  else:
    print("That's not a valid answer")
    question()

# online 유무 확인
def check_online_site(site):
  HTTP = 'http://'
  for check in site:
    # 예외 처리
    try:
      r = requests.get(HTTP+check)
      if r.status_code == 200:
        print(f"{HTTP}{check} is up!")
      else:
        print(f"{HTTP}{check} is up!")
    except requests.RequestException:  
      print(f"{HTTP}{check} is is down!")
      # raise
    except:
      print(f"{HTTP}{check} is is down!")
  # 다시 시작할건지 질문 실행
  question()


def boilerplate(site=[]):
  # 시작 문구
  print("Welcome to IsItDown.py!")
  print("Please write a URL or URLs you want to check. (separated by comma)")
  # 입력
  links = str(input())
  # 구분
  # http:// 입력시 처리 방법 고민 중
  link = links.replace(',',' ').replace('http://','')
  site = link.split()
  # 링크가 맞는지 확인하기
  search=".com"
  for check in site:
    if search not in check:
      print(f"{check} is not a valid URL")
      site.remove(check)
  # 로딩
  print("--------- loading ---------")
  check_online_site(site)


site = []
boilerplate()