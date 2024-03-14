import requests
def checkServiceForWord(url, keyword):


   try:
    x = requests.get(url)
    print(x.text)
    serverStatus=1
    if keyword in x.text:
      print("found keyword")
      return True
   except:
     print("error")
     return False
url = 'https://jsonplaceholder.typicode.com/todos/1'
result = checkServiceForWord(url, 'userId')
print(result)