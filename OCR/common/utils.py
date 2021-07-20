
import requests
import json

def sendTextMessage(message,contactno):
    url = "https://www.fast2sms.com/dev/bulkV2"

    payload = "sender_id=TXTIND&message="+message+"&route=v3&numbers="+contactno
    headers = {
        'authorization': "sXWz05ZdROMhxVAE5WG2sK74N9mIfVdT4j0dqAWWWUhrM65UUtFpg84w50t0",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    dict_data = json.loads(response.text)

    return dict_data['return']

