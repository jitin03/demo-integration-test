from pactman.verifier.verify import ProviderStateMissing
import requests


def provider_state(name, **params):

    if name == 'UserA exist':
        print(name)
        # res = requests.get('https://reqres.in/api/users/2')
        # print(res.headers)

    else:
        raise ProviderStateMissing(name)


def test_pacts(pact_verifier):
    pact_verifier.verify("https://reqres.in/",provider_state)


