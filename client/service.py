import requests
def my_exchandler(type, value, traceback):
  print(value)

import sys
sys.excepthook = my_exchandler



def test_conn(url):
    res = requests.get(url)
    return res.status_code


def get_list(url,token):

    if not token:
        return "Войдите или зарегистрируйтесь.\n chatty signup --help" \
               "\nchatty login --help"

    endpoint = '/api/v3/rooms/'
    headers = {'Authorization': 'Token %s' % token}
    res = requests.get(url+endpoint, headers=headers)
    return res.json()

def sign_up(url,user,email,password):

    endpoint = '/api/v3/reg/'
    json = {"username": "%s" % user,"email": "%s" % email,"password": "%s" % password}
    res = requests.post(url+endpoint,json = json).json()

    if res.get('error', False) != False:
        raise Exception(res['error'])
    else:
        return res['token']

def select_chat(url,chat_name,token):
    endpoint = '/api/v3/rooms/%s/' % chat_name
    headers = {'Authorization': 'Token %s' % token}
    try:
        res = requests.get(url+endpoint, headers=headers).json()
        def rotate_chr(c):
            msg = c["sender"] + ': ' + c["message"] + '\n- - - - - -\n'
            return msg
        string = '***' + chat_name + '*** \n'
        string += "".join(map(rotate_chr, res))
        return string
    except:
        return "Во время выполнения произошла ошибка, проверьте правильность введенных данных"

def create_room(url,chat_name,token):
    endpoint = '/api/v3/create-room/'
    headers = {'Authorization': 'Token %s' % token}
    try:
        json = {"room_name": "%s" % chat_name}

        requests.post(url+endpoint,headers=headers,json = json)
        return select_chat(url,chat_name,token)
    except:
        return "Во время выполнения произошла ошибка, проверьте правильность введенных данных"

def send_message(url,message,chat,token,):
    endpoint = '/api/v3/rooms/%s/create/' % chat
    headers = {'Authorization': 'Token %s' % token}
    try:
        json = {"room_name":"%s" % chat, "message":"%s" % message, "sender":"%s" % token}

        res = requests.post(url + endpoint, headers=headers, json=json).json()

        def rotate_chr(c):
            msg = c["sender"] + ': ' + c["message"] + '\n- - - - - -\n'
            return msg

        string = '***' + chat + '*** \n'
        string += "".join(map(rotate_chr, res))
        return string
    except:
        return "Во время выполнения произошла ошибка, проверьте правильность введенных данных\n" \
               "возможно вы еще не вступили не в один чат"


def login(url,user,password):
    endpoint = '/api-token-auth/'
    data = {'username':'%s' % user, 'password':'%s' % password}
    try:
        res = requests.post(url + endpoint, data=data).json()['token']
        return res
    except:
        return "Во время выполнения произошла ошибка, проверьте правильность введенных данных"


def leave_chat(url,chat_name,token):
    pass
#sign_up('http://127.0.0.1:8000','qwe333qweq','w22@3.com',123)
#select_chat('http://127.0.0.1:8000','smokers-club','49669aac2a987ad1dc472dbaf16d2c7c0095f870')
#create_room('http://127.0.0.1:8000','fans!','49669aac2a987ad1dc472dbaf16d2c7c0095f870')
#send_message('http://127.0.0.1:8000','я естьsss q231','smokers-club3','49669aac2a987ad1dc472dbaf16d2c7c0095f870')
#login('http://127.0.0.1:8000','pawell','1234')
