import requests


def get_user_list(path):
    '''
    Get User list
    :param page_no:
    :return:
    '''
    response = requests.get(f'http://localhost:8155/api/users/{path}')

    if response.text=="":
        print(response.status_code)
        return None
    return response.json()


