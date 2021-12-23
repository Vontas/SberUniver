from typing import NewType
import requests

#НЕГАТИВНАЯ ПРОВЕРКА POST. Отправляем запрос неавторизованным пользователем.
def test_post_Negative():
        
    urlPost = "https://petstore.swagger.io/v2/user"
    requestPost = {}
    requestPost['id'] = 3456
    requestPost['username'] = "orangevus323"
    requestPost['firstName'] = 'Dmitriy'
    requestPost['lastName'] = 'Smirnov'
    requestPost['email'] = 'dima@demon.net'
    requestPost['pssword'] = 'qwerty'
    requestPost['phone'] = '+7123456789'
    requestPost['userStatus'] = 0
    print ("RequestPost : ",requestPost)
    
  
   
    #Отправляем запрос неавторизированым пользователем
    #В Свагере сказано что запрос может сделать только авторизованный пользователь,
    #но не указано что за ошибка будет если пользователь неавторизован
    #поэтому просто ожидаю тут ошибку....   
    responsePost = requests.post(urlPost, json=requestPost)
    print("response  POST : ", responsePost.json())
    assert responsePost.json()["type"] == "error"    
    #Проверяем результат запросом Get  
def test_get_post_Negative():
    urlPostGet = "https://petstore.swagger.io/v2/user/orangevus323"
    responsePostGet = requests.get(urlPostGet)
    print("responsePostGET = ", responsePostGet.json())
    assert responsePostGet.json()["message"] == "User not found"
    assert responsePostGet.json()["type"] == "error"
    assert responsePostGet.json()["code"] == 1

 #Проверяем можно ли неавторизованным пользователем перезаписать уже созданную сущность
def test_post_Negative():
    #Создаем новую сущность Авторизованным пользователем
    urlPostNew = "https://petstore.swagger.io/v2/user"
    requestPostNew = {}
    requestPostNew['id'] = 32311
    requestPostNew['username'] = "orangevus32311"
    requestPostNew['firstName'] = 'Dmitriy'
    requestPostNew['lastName'] = 'Smirnov'
    requestPostNew['email'] = 'dima@demon.net'
    requestPostNew['pssword'] = 'qwerty'
    requestPostNew['phone'] = '+7123456789'
    requestPostNew['userStatus'] = 0
    print ("RequestPostNew : ",requestPostNew)
  
   
    #Отправляем запрос Авторизированным пользователем   
    responsePostNew = requests.post(urlPostNew, auth=('orangevus','qwerty'),json=requestPostNew)
    print("response  POSTNew : ", responsePostNew.json()) 
    #Проверяем что сущность создана
    urlPostGetNew = "https://petstore.swagger.io/v2/user/orangevus32311"
    responsePostGetNew = requests.get(urlPostGetNew)
    print("responsePostGETNEW = ", responsePostGetNew.json())
    

    #Пробуем перезаписать сущность неавторизованным пользователем    
    urlPostNeg = "https://petstore.swagger.io/v2/user"
    requestPostNeg = {}
    requestPostNeg['id'] = 32311
    requestPostNeg['username'] = "orangevus32311"
    requestPostNeg['firstName'] = 'Alex'
    requestPostNeg['lastName'] = 'Smirnov'
    requestPostNeg['email'] = 'dima@demon.net'
    requestPostNeg['pssword'] = 'qwerty'
    requestPostNeg['phone'] = '+7123456789'
    requestPostNeg['userStatus'] = 0
    print ("RequestPostNeg : ",requestPostNeg)
    responsePostNeg = requests.post(urlPostNeg, json=requestPostNeg)
    print("response  POSTNEG : ", responsePostNeg.json())
    #Ожидаем сообщение об ошибке
    assert responsePostNeg.json()["type"] == "error"   
    #Проверяем изменения при помощи Get
def test_PostNegGet():
    urlPostNegGet = "https://petstore.swagger.io/v2/user/orangevus32311"
    responsePostNegGet = requests.get(urlPostNegGet)
    print("responsePostNegGet = ", responsePostNegGet.json())
    assert responsePostNegGet.json()['firstName'] == "Dmitriy"
    print('FIRST NAME :', responsePostNegGet.json()['firstName'] )

