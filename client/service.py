import requests



def test_conn(url):
    res = requests.get(url)
    return res.status_code


def get_list(url,token):
    endpoint = '/api/v3/rooms/'
    headers = {'Authorization': 'Token %s' % token}
    res = requests.get(url+endpoint, headers=headers)
    if res.status_code != 200:
        return res.text
    res = res.json()
    def pretty_print(c):
        msg = '**'+ c["room_name"] + '\n- - - - - -\n'
        return msg


    string = "".join(map(pretty_print, res))
    return string

def sign_up(url,user,email,password):

    endpoint = '/api/v3/reg/'
    json = {"username": "%s" % user,"email": "%s" % email,"password": "%s" % password}
    res = requests.post(url+endpoint,json = json)
    if res.status_code != 200:
        return res.text
    res = res.json()
    if res.get('error', False) != False:
        raise Exception(res['error'])
    else:
        return res['token']

def select_chat(url,chat_name,token):
    endpoint = '/api/v3/rooms/%s/' % chat_name
    headers = {'Authorization': 'Token %s' % token}
    try:
        res = requests.get(url+endpoint, headers=headers)
        if res.status_code != 200:
            return "err: status code %s" % res.status_code
        res = res.json()
        def pretty_print(c):
            msg = c["sender"] + ': ' + c["message"] + '\n- - - - - -\n'
            return msg

        string = '***' + chat_name + '*** \n'

        string += "".join(map(pretty_print, res))

        return string
    except:
        return "Во время выполнения произошла ошибка, проверьте правильность введенных данных"

def create_room(url,chat_name,token):
    endpoint = '/api/v3/create-room/'
    headers = {'Authorization': 'Token %s' % token}
    try:
        json = {"room_name": "%s" % chat_name}
        res = requests.post(url+endpoint,headers=headers,json = json)
        if res.status_code != 200:
            return res.text
        return select_chat(url,chat_name,token)
    except:
        return "Во время выполнения произошла ошибка, проверьте правильность введенных данных"

def send_message(url,message,chat,token,):
    endpoint = '/api/v3/rooms/%s/create/' % chat
    headers = {'Authorization': 'Token %s' % token}
    try:
        json = {"room_name":"%s" % chat, "message":"%s" % message, "sender":"%s" % token}

        res = requests.post(url + endpoint, headers=headers, json=json)
        if res.status_code != 200:
            return res.text
        res = res.json()
        def pretty_print(c):
            msg = c["sender"] + ': ' + c["message"] + '\n- - - - - -\n'
            return msg

        string = '***' + chat + '*** \n'
        string += "".join(map(pretty_print, res))
        return string
    except:
        return "Во время выполнения произошла ошибка, проверьте правильность введенных данных\n" \
               "возможно вы еще не вступили не в один чат"


def login(url,user,password):
    endpoint = '/api-token-auth/'
    data = {'username':'%s' % user, 'password':'%s' % password}
    try:
        res = requests.post(url + endpoint, data=data)
        if res.status_code != 200:
            return res.text
        return res.json()['token']
    except:
        return "Во время выполнения произошла ошибка, проверьте правильность введенных данных"


select_chat('http://127.0.0.1:8000','aWa','9b34ff6ab7defd610f41bb0e4bd5d09f5015f5af')