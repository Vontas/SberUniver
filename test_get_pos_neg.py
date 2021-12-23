#Позитивная проверка, Get запрос с заранее созданым Пользователем username = orangevus password = qwerty
import requests
import datetime
def test_get():
    urlGet = "https://petstore.swagger.io/v2/user/login?username=orangevus&password=qwerty"
    responseGet = requests.get(urlGet)
    print("responseGET = ", responseGet.json())
    #Создаю дополнительную переменую что бы записать в нее значение X-Expires-After , если оно есть...
    expires = responseGet.headers['X-Expires-After']
    assert responseGet.status_code == 200
    assert responseGet.json()["code"] == 200
    assert responseGet.json()["type"] == 'unknown'
    assert responseGet.headers["X-Rate-Limit"] == "5000"
    assert responseGet.headers['X-Expires-After'] == expires
  
   #Пытался сделать Assert для сравнения даты и времени создания ключа, но как привести к нуюному формату пока не понял.  
   # today = datetime.datetime.today()
   # print( today.strftime(" %Y-%m-%d-%H.%M.%S") )   
#Негативная проверка Get , неверный пароль
def test_get_wrong_pass():
    urlGetpass = "https://petstore.swagger.io/v2/user/login?username=orangevus&password=ywqrt"
    responseGetpass = requests.get(urlGetpass)
    print("responseGET = ", responseGetpass.json())
    assert responseGetpass.status_code == 400
#Негативная проверка Get, без логина и пароля

def test_get_wrong_logpas():
    urlGetLog = "https://petstore.swagger.io/v2/user/login?username=&password="
    responseGetLog = requests.get(urlGetLog)
    print("responseGET = ", responseGetLog.json())
    assert responseGetLog.status_code == 400
    
    