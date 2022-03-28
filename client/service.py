import requests
def my_exchandler(type, value, traceback):
  print(value)

import sys
sys.excepthook = my_exchandler



def test_conn(url):
    res = requests.get(url)
    return res.status_code

def login():
    '''ok'''

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
        for i in res:

        return res
    except:
        return "Во время выполнения произошла ошибка, проверьте правильность введенных данных"



#sign_up('http://127.0.0.1:8000','qwe333qweq','w22@3.com',123)
select_chat('http://127.0.0.1:8000','smokers-club','49669aac2a987ad1dc472dbaf16d2c7c0095f870')