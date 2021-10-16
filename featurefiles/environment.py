import requests
from utilities.apiresources import *
from utilities.configurations import *


def after_scenario(context, scenario):
    if "PetStore" in scenario.tags:

        url = getconfig()['API']['endpoint'] + '/pet/'
        url2 = url+"{}".format(context.petId)

        response_deletepet = requests.delete(url2,
                                           json={"petId": context.petId},
                                           headers={"Content-Type": "application/json"},
                                           )

        assert response_deletepet.status_code == 200

