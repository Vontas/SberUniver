import requests
#Для выполнения Post необходимо что бы пользователь был Авторизован
#Для этого вначале делаю запрос get что бы проверить авторизацию
#под логином "orangevus" и паролем "qwerty"
def test_get():
    urlGet = "https://petstore.swagger.io/v2/user/login?username=orangevus&password=qwerty"
    responseGet = requests.get(urlGet)
    print("responseGET = ", responseGet.json())
    assert responseGet.status_code == 200
    assert responseGet.json()["code"] == 200
    assert responseGet.json()["type"] == 'unknown'


def test_post():
        
    urlPost = "https://petstore.swagger.io/v2/user"
    requestPost = {}
    requestPost['id'] = 99984324
    requestPost['username'] = "orangevus255"
    requestPost['firstName'] = 'Dmitriy'
    requestPost['lastName'] = 'Smirnov'
    requestPost['email'] = 'dima@demon.net'
    requestPost['pssword'] = 'qwerty'
    requestPost['phone'] = '+7123456789'
    requestPost['userStatus'] = 0
    print ("RequestPost : ",requestPost)
  
   
    #Отправляем запрос Авторизированым пользователем   
    responsePost = requests.post(urlPost, auth=('orangevus','qwerty'),json=requestPost)
    print("response  POST : ", responsePost.json()) 
    assert responsePost.json()["code"] == 200
    assert responsePost.json()["type"] == 'unknown'
    assert responsePost.json()["message"] == str(requestPost["id"])

    # ДЕЛАЕМ ПРОВЕРКУ POST ЗАПРОСА ПРИ ПОМОЩИ GET

    urlPostGet = "https://petstore.swagger.io/v2/user/"  + requestPost['username']
    responsePostGet = requests.get(urlPostGet)
    #Создаем переменную для подсчета количетсва запросов
    kol = 0
   #Если вдруг в базе данного id нет, то сообщим что у нас ошибка 404 и повторяем запрос.
   #Чтобы избежать бесконечного цикла, поставил ограничение на 10 попыток.  
   #Если за 10 попыток все будут неудачными, значит Post не отработал как надо и будем считать тест проваленным.
   #В реальном проекте вероятно данные циклы будут лишними, тк то что база не зеркалируется (дублируется) это БАГ,
   # но в рамках обучения, чтобы не запускать десятки раз один и тот же код, я сделал данное допущение...
    while responsePostGet.status_code == 404 and kol != 10:  
        responsePostGet = requests.get(urlPostGet)
        print("Ошибка 404  ", "Повторяем запрос", "kol = ", kol)
        kol = kol+1
    if kol == 10:
        print("Количество попыток :", kol)
        print("responsePostGET =", responsePostGet.json())
        assert responsePostGet.json()["id"] == requestPost["id"]
        assert responsePostGet.json()["username"] == requestPost["username"]
        assert responsePostGet.json()["firstName"] == requestPost["firstName"]
        assert responsePostGet.json()["lastName"] == requestPost["lastName"]
        assert responsePostGet.json()["email"] == requestPost["email"]
        assert responsePostGet.json()["phone"] == requestPost["phone"] 
    else:
        #Обнуляю переменную
        kol = 0   
              
        
        while (responsePostGet.json()['firstName'] != "Dmitriy") and (kol !=10):
            print('Данные не обновились, пробуем еще раз')        
            responsePostGet = requests.get(urlPostGet)                     
            kol = kol+1
            while responsePostGet.status_code == 404:
                #Есть вероятность что мы снова получим 404
                responsePostGet = requests.get(urlPostGet)
                print('снова 404')
        print("responsePostGET = ", responsePostGet.json())
        assert responsePostGet.json()["id"] == requestPost["id"]
        assert responsePostGet.json()["username"] == requestPost["username"]
        assert responsePostGet.json()["firstName"] == requestPost["firstName"]
        assert responsePostGet.json()["lastName"] == requestPost["lastName"]
        assert responsePostGet.json()["email"] == requestPost["email"]
        assert responsePostGet.json()["phone"] == requestPost["phone"] 



    