import pytest
import requests
import pytest
import requests
                                                          #СОЗДАЮ POST ЗАПРОС
def test_post_positive():
    url = "https://petstore.swagger.io/v2/pet"
    request = {}
    request['name'] = "KOTOSBER"                         #Имя животного задаем прямо тут
    request['category'] = {}
    request['category']['name'] = "SBEROKOT"
    request['category']['id'] = 500
    request['photoUrls'] = ['photoCat']
    request['status'] = "available"
    print("==================================================REQUEST POST===========================================================================================")
    print("REQUEST : ", request)                          #Смотрим что записали в массив request
    response = requests.post(url, json=request)           #По переменной url , делает json запрос и сохраняет его в response (id name и тп)
    print("==================================================RESPONSE POST=====================================================================================")
    print("response  POST : ", response.json())           #Выводим ответ
    #id2 = str(response.json()['id'])                     #Вначале думал занести id в отдельную переменную для будущего Put.
    assert response.json()['id'] is not None              #Проверяем что id не пустой
    assert response.json()['name'] == request['name']     #Проверяем что имя запроса и ответа совпадают
    assert response.json()['category']['name'] == request['category']['name']
    assert response.json()['category']['id'] == request['category']['id']
    assert response.json()['photoUrls'] == request['photoUrls']
    assert response.json()['status'] == request['status']


    print('======================================================GET===================================================================================')
    urlGet = "https://petstore.swagger.io/v2/pet/" + str(response.json()['id'])
    responseGet = requests.get(urlGet)
    #Мартышкин труд. Так как базы не зеркалируются, то для того что бы получить нужный результат, мне пришлось прибегнуть к циклам.
    #В реальном тесте, это скорей всего будет лишним, тк  то что базы друг друга не копируют - ЭТО БАГ, но в конктексте обучения,
    #данный баг приходится воспринимать как Фичу, поэтому я буду стучаться в базу до тех пор пока она не выдаст НУЖНЫЙ мне результат...
    while responseGet.status_code == 404:   #Если вдруг в базе данного id нет, то сообщим что у нас ошибка 404 и будем стучать дальше.
        responseGet = requests.get(urlGet)
        print("Ошибка 404")

    while responseGet.json()['name'] != "KOTOSBER":       
        print('Данные не обновились, пробуем еще раз')        #Это необходимо тк база не зеркалируется, что бы избежать неверного ответа.
        responseGet = requests.get(urlGet)                    #Если name сразу будет Kotosber то цикл просто не будет выполняться, 
        while responseGet.status_code == 404:                 #Есть вероятность что мы снова получим 404, поэтому Цикл внутри Цикла внутри Цикла..
            responseGet = requests.get(urlGet)
            print('снова 404')
    print("responseGET = ", responseGet.json())               #Мы сразу перейдем к print, если все звёзды сойдутся...
    




                                                
                                                
                                                 # МЕНЯЮ ЧЕРЕЗ PUT ЗАПРОС
    
    urlPut = "https://petstore.swagger.io/v2/pet"
    request = {}
      
    #print("ВВЕДИТЕ НАЗВАНИЕ ЖИВОТНОГО")
    #name = input()                                     #В этом варианте название животного можно задать  прямо в процеессе выполнения кода
    #request['name'] = name

    request['id'] = str(response.json()['id'])
    request['name'] = "SBERDOG"                         #Имя животного задаем прямо тут
    request['category'] = {}
    request['category']['name'] = "TopDOG"
    request['category']['id'] = 101
    request['photoUrls'] = ['photoDog']
    request['status'] = "SOLD"
   #request['tags'] = {}
    #request['tags'] = ["id"], ["name"]
    #request['tags']["id"] = 5                          pytest test_put.py -v -s
    #request['tags']['name'] = 'DJORDANO'
    #request['tags'] = "5"                           # ВОТ ТУТ НЕПОНЯТНО, как менять значения внутри tags?
    #request['tags']['name'] = "Dog"
    #request ['tags'] = [['id', 5], ['name', "lol"]]     и не матрица......


    print("===================================================REQUEST PUT=================================================================================")
    print("request :", request)                            # Смотрим свой массив
    responsePut = requests.put(urlPut, json=request)       #По переменной url , делает json запрос и сохраняет его в response (id name и тп)
    print("===================================================RESPONSE PUT================================================================================")
    print("response  PUT :", responsePut.json())       #Выводим ответ
    assert responsePut.json()['id'] is not None
    assert responsePut.json()['name'] == request['name']
    assert responsePut.json()['category']['name'] == request['category']['name']
    assert responsePut.json()['category']['id'] == request['category']['id']
    assert responsePut.json()['photoUrls'] == request['photoUrls']
    assert responsePut.json()['status'] == request['status']
    
    print('======================================================GET===================================================================================')
    urlGet = "https://petstore.swagger.io/v2/pet/" + str(response.json()['id'])
    responseGet = requests.get(urlGet)

    while responseGet.status_code != 200:
        responseGet = requests.get(urlGet)
        print("Ошибка 404")
    
    while responseGet.json()['name'] != "SBERDOG":            #Запускаем Цикл, который будет выполняться пока name не станет Sberdog. 
        print('Данные не обновились, пробуем еще раз')        #Это необходимо тк база не зеркалируется, что бы избежать неверного ответа.
        responseGet = requests.get(urlGet)                     #Если name сразу будет Sberdog то цикл просто не будет выполняться, 
        while responseGet.status_code != 200:                 #Мы сразу перейдем к print
            responseGet = requests.get(urlGet)
            print('снова 404')                     
    print("responseGET = ", responseGet.json())               
    #if (responseGet.status_code == 200):
        #assert responseDel.status_code == 404
        #print("Pet Not Found")
    #else:
        #print("noob")


    print("===================================================REQUEST DELETE=================================================================================")
    urlDel = "https://petstore.swagger.io/v2/pet/" + str(response.json()['id'])  #Тк id в данном случает int, то привели к типу str - строковый
    responseDel = requests.delete(urlDel, json=request)
    while responseDel.status_code == 404:
        print('Данный id не существует, повторяем запрос')
        responseDel = requests.delete(urlDel, json=request)
   # if responseDel.status_code == 404:              #На тот случай если данный id уже удален делаем проверку. Без данной проверки может возникнуть ошибка, тк БД не зеркалируется.
    #    print ('Данный ID не существует', responseDel.status_code)
    #else:
    print('Приступаем к удаленнию')
    print("RESPONSE DELETE:", responseDel.json())
    assert responseDel.status_code == 200           #Проверяем статус код 200
    assert responseDel.json()['message'] == str(responsePut.json()['id']) #Проверяем что message из Delete это ID из Put.
    print("Status code: ", responseDel.status_code) #Отдельно вывел на экран Status code 200
    print("Message: ", responseDel.json()['message'])  # Отдельно вывожу Message




    print('======================================================GET===================================================================================')
    urlGet = "https://petstore.swagger.io/v2/pet/" + str(response.json()['id'])
    responseGet = requests.get(urlGet)

    while responseGet.status_code != 404:
        responseGet = requests.get(urlGet)
        print("Status Code = 200 , данные не обновились. Повторяем запрос")
    print('Ура Победа', responseGet.json())
    assert responseGet.status_code == 404
    assert responseGet.json()['type'] == 'error'
    assert responseGet.json()['message'] == 'Pet not found'
    assert responseGet.json()['code'] == 1
    
    print('======================================================PUT NEGATIVE===================================================================================')
    
    urlPutNeg = "https://petstore.swagger.io/v2/pet"
    request = {}
    request['id'] = 98526314           #Отправляем запрос Put в несуществующий id
    request['name'] = ""                                #Имя животного оставляем пустым
    request['category'] = {}
    request['category']['name'] = "TopDOG"
    request['category']['id'] = 101
    request['photoUrls'] = ['photoDog']
    request['status'] = "TROLL"                         #Указываем несуществующий status
    print("request :", request)
    responsePutNeg = requests.put(urlPutNeg, json=request)
    print("response  PUT :", responsePutNeg.json())       #Выводим ответ
    assert responsePutNeg.json()['id'] is not None
    assert responsePutNeg.json()['name'] == request['name']
    assert responsePutNeg.json()['category']['name'] == request['category']['name']
    assert responsePutNeg.json()['category']['id'] == request['category']['id']
    assert responsePutNeg.json()['photoUrls'] == request['photoUrls']
    assert responsePutNeg.json()['status'] == request['status']


    print('======================================================GET===================================================================================')
    urlGetNeg = "https://petstore.swagger.io/v2/pet/98526314"
    responseGetNeg = requests.get(urlGetNeg)

    while responseGetNeg.status_code == 404:
        responseGetNeg = requests.get(urlGetNeg)
        print("Ошибка 404")
    
    while responseGetNeg.json()['status'] != "TROLL":            #Запускаем Цикл, который будет выполняться пока name не станет Sberdog. 
        print('Данные не обновились, пробуем еще раз')        #Это необходимо тк база не зеркалируется, что бы избежать неверного ответа.
        responseGetNeg = requests.get(urlGetNeg)                     #Если name сразу будет Sberdog то цикл просто не будет выполняться, 
        while responseGetNeg.status_code == 404:                 #Мы сразу перейдем к print
            responseGetNeg = requests.get(urlGetNeg)
            print('снова 404')                     
    print("responseGET = ", responseGetNeg.json()) 
    assert responseGetNeg.json()['id'] is not None
    assert responseGetNeg.json()['name'] == request['name']
    assert responseGetNeg.json()['category']['name'] == request['category']['name']
    assert responseGetNeg.json()['category']['id'] == request['category']['id']
    assert responseGetNeg.json()['photoUrls'] == request['photoUrls']
    assert responseGetNeg.json()['status'] == request['status']      


   