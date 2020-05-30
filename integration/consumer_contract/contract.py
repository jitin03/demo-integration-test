import unittest
from pactman import Consumer, Provider
from integration.clients.client import get_user_list
import json
import os
from pathlib import Path
from pactman import Term, Like

PACT_MOCK_HOST = 'localhost'
PACT_MOCK_PORT = 1234

PACT_DIR = os.getcwd() + "/../provider_test/pact/"
print(os.getcwd())

pact = Consumer('Consumer').has_pact_with(Provider('Provider'), file_write_mode="overwrite", pact_dir=PACT_DIR)


class GetUserListContract(unittest.TestCase):

    def test_get_user(self):
        expected =None
        pact.given(
            "UserA doesn't exists"
        ).upon_receiving(
            'a request for User'
        ).with_request(
            'GET', '/api/users/23'
        ).will_respond_with(404)

        with pact:
            result = get_user_list("23")


        self.assertEqual(result, expected)

    def test_get_user_info(self):
        expected = Like({
            "data": {
                "id": 2,
                "email": Term('\S+@\S+',"janet.weaver@reqres.in"),
                "first_name": "Janet",
                "last_name": "Weaver",
                "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/josephstein/128.jpg"
            },
            "ad": {
                "company": "StatusCode Weekly",
                "url": "http://statuscode.org/",
                "text": "A weekly newsletter focusing on software development, infrastructure, the server, performance, and the stack end of things."
            }
        })

        pact.given(
            'UserA exist'
        ).upon_receiving(
            'a request for User'
        ).with_request(
            'GET', '/api/users/2'
        ).will_respond_with(200, body=expected)

        with pact:
            result = get_user_list("2")
            print(result)

