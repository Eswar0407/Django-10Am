#import random

#random_number = random.randint(100000,999999)

#print(random_number)

#import requests

#url = "https://www.fast2sms.com/dev/bulkV2"

#payload = "sender_id=TXTIND&message=This is a test message from Eswar&route=v3&numbers=9542934624"
#headers = {
#    'authorization': "sXWz05ZdROMhxVAE5WG2sK74N9mIfVdT4j0dqAWWWUhrM65UUtFpg84w50t0",
#    'Content-Type': "application/x-www-form-urlencoded",
#    'Cache-Control': "no-cache",
#    }

#response = requests.request("POST", url, data=payload, headers=headers)

#print(response.text)

from common.utils import sendTextMessage
response = sendTextMessage("Hello this Is Eswar","95428213021")

print(response)