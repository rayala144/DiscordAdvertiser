from time import sleep
from random import choice
from requests import post
import asyncio

class advertiser:
    def __init__(self, authsDirectory: str, messageDirectory: str, channelsDirectory: str, delay: int=300) -> str:
        self.authsDirectory = authsDirectory
        self.messageDirectory = messageDirectory
        self.channelsDirectory = channelsDirectory
        self.delay = delay
        self.message = open(messageDirectory).read()
        
    
    async def sendMessage(self, channel, auth):
        data = {
            "content" : self.message
        }
        headers = {
            "Authorization" : auth
        }
        
        response = post(f"https://discord.com/api/v9/channels/{channel}/messages", data=data, headers=headers)
        return response.status_code
        
    async def main(self):
        channels = [channel for channel in open(self.channelsDirectory).read().splitlines()]
        auths = [auth for auth in open(self.authsDirectory).read().splitlines()]
        
        funcs = [self.sendMessage(channel, choice(auths)) for channel in channels]
        responses = await asyncio.gather(*funcs)
        print(f"Sent messages with responses: {responses}")
        await asyncio.sleep(self.delay)
        
        
    
a = advertiser(authsDirectory="auths.txt", messageDirectory="message.txt", channelsDirectory="channels.txt")

while True:
    asyncio.run(a.main())