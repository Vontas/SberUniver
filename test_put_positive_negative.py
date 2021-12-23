#Для тестирования Put создаю новую сущность при помощи Post
import requests
def test_put_positive():
        
    urlPost = "https://petstore.swagger.io/v2/user"
    requestPost = {}
    requestPost['id'] = 2343
    requestPost['username'] = "orangevus692"
    requestPost['firstName'] = 'Dmitriy'
    requestPost['lastName'] = 'Smirnov'
    requestPost['email'] = 'dima@demon.net'
    requestPost['pssword'] = 'qwerty'
    requestPost['phone'] = '+7123456789'
    requestPost['userStatus'] = 0
    print ("RequestPost : ",requestPost)
    responsePost = requests.post(urlPost, auth=('orangevus','qwerty'), json=requestPost)
    print("response  POST : ", responsePost.json())
#Проверяем что сущность создана
    urlGet = "https://petstore.swagger.io/v2/user/" + requestPost["username"]
    responseGet = requests.get(urlGet)
    print("responseGET = ", responseGet.json())
#Делаем Put запрос.
    urlPut = "https://petstore.swagger.io/v2/user/" + responseGet.json()['username']
    requestPut = {}
    requestPut['id'] = 2343
    requestPut['username'] = "orangevus692"
    requestPut['firstName'] = 'Alex'
    requestPut['lastName'] = 'Bel'
    requestPut['email'] = 'Alex@Bel.net'
    requestPut['pssword'] = 'qwerty2'
    requestPut['phone'] = '+7987654321'
    requestPut['userStatus'] = 1
    print("requestPUT :", requestPut)                            
    responsePut = requests.put(urlPut, auth=('orangevus','qwerty'), json=requestPut)
    print("response  PUT :", responsePut.json())
    assert responsePut.json()["code"] == 200
    assert responsePut.json()["type"] == 'unknown'
    assert responsePut.json()["message"] == str(requestPut["id"])
    #Проверяем изменения при помощи Get
    print("responsePUTGET = ", responseGet.json())
    assert responseGet.json()["id"] == requestPut["id"]
    assert responseGet.json()["username"] == requestPut["username"]
    assert responseGet.json()["firstName"] == requestPut["firstName"]
    assert responseGet.json()["lastName"] == requestPut["lastName"]
    assert responseGet.json()["email"] == requestPut["email"]
    assert responseGet.json()["phone"] == requestPut["phone"]


#Для тестирования Put Negative создаю новую сущность при помощи Post

def test_put_neg():
        
    urlPost = "https://petstore.swagger.io/v2/user"
    requestPost = {}
    requestPost['id'] = 23434
    requestPost['username'] = "orangevus693"
    requestPost['firstName'] = 'Dmitriy'
    requestPost['lastName'] = 'Smirnov'
    requestPost['email'] = 'dima@demon.net'
    requestPost['pssword'] = 'qwerty'
    requestPost['phone'] = '+7123456789'
    requestPost['userStatus'] = 0
    print ("RequestPost : ",requestPost)
    responsePost = requests.post(urlPost, auth=('orangevus','qwerty'), json=requestPost)
    print("response  POST : ", responsePost.json())
#Проверяем что сущность создана
    urlGet = "https://petstore.swagger.io/v2/user/" + requestPost["username"]
    responseGet = requests.get(urlGet)
    print("responseGET = ", responseGet.json())
#Для выполнения Put запроса пользователь должен быть авторизован
#В данном тесте пользователь неавторизован
#Делаем Put запрос.
    urlPut = "https://petstore.swagger.io/v2/user/" + responseGet.json()['username']
    requestPut = {}
    requestPut['id'] = 23434
    requestPut['username'] = "orangevus693"
    requestPut['firstName'] = 'Alex'
    requestPut['lastName'] = 'Bel'
    requestPut['email'] = 'Alex@Bel.net'
    requestPut['pssword'] = 'qwerty2'
    requestPut['phone'] = '+7987654321'
    requestPut['userStatus'] = 1
    print("requestPUT :", requestPut)                            
    responsePut = requests.put(urlPut, json=requestPut)
    print("response  PUT :", responsePut.json())
    assert responsePut.status_code == 400
    #Проверяем изменения при помощи Get
def test_Put_Get_Neg():
    urlGet = "https://petstore.swagger.io/v2/user/orangevus693" 
    responseGet = requests.get(urlGet)
    print("responsePUTGET = ", responseGet.json())
    assert responseGet.json()["code"] == 1
    assert responseGet.json()["type"] == 'error'
    assert responseGet.json()["message"] == "User not found"
#Проверим создание сущности  через запрос Put
def test_Put_Username_Neg():
#Создаем сущность Post запросом
    urlPost = "https://petstore.swagger.io/v2/user"
    requestPost = {}
    requestPost['id'] = 45654
    requestPost['username'] = "orangevus8"
    requestPost['firstName'] = 'Dmitriy'
    requestPost['lastName'] = 'Smirnov'
    requestPost['email'] = 'dima@demon.net'
    requestPost['pssword'] = 'qwerty'
    requestPost['phone'] = '+7123456789'
    requestPost['userStatus'] = 0
    print ("RequestPost : ",requestPost)
    responsePost = requests.post(urlPost, auth=('orangevus','qwerty'), json=requestPost)
    print("response  POST : ", responsePost.json())
#Проверяем что сущность создана
    urlGet = "https://petstore.swagger.io/v2/user/" + requestPost["username"]
    responseGet = requests.get(urlGet)
    print("responseGET = ", responseGet.json())
#Делаем Put запрос
    urlPut = "https://petstore.swagger.io/v2/user/" + responseGet.json()['username']
    requestPut = {}
    requestPut['id'] = 45654
#Меняем username на orangevus9
    requestPut['username'] = "orangevus9"
    requestPut['firstName'] = 'Alex'
    requestPut['lastName'] = 'Bel'
    requestPut['email'] = 'Alex@Bel.net'
    requestPut['pssword'] = 'qwerty2'
    requestPut['phone'] = '+7987654321'
    requestPut['userStatus'] = 1
    print("requestPUT :", requestPut)                            
    responsePut = requests.put(urlPut, auth=('orangevus','qwerty'), json=requestPut)
    print("response  PUT :", responsePut.json())
    assert responsePut.status_code != 200
#Проверяем Put при помощи Get
#Put создал нового пользователя, при этом пользователь orangevus8 удалился.
def test_Get_Put_Neg():
    urlGet = "https://petstore.swagger.io/v2/user/orangevus9"
    responseGet = requests.get(urlGet)
    print("responseGET = ", responseGet.json())
    assert responseGet.json()["code"] == 1
    assert responseGet.json()["type"] == 'error'
    assert responseGet.json()["message"] == "User not found"




    


    