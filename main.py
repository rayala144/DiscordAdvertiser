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
        
        post(f"https://discord.com/api/v9/channels/{channel}/messages", data=data, headers=headers)
        return
        
    async def main(self):
        channels = [channel for channel in open(self.channelsDirectory).read().splitlines()]
        print(channels)
        auths = [auth for auth in open(self.authsDirectory).read().splitlines()]
        
        funcs = [self.sendMessage(channel, choice(auths)) for channel in channels]
        
        await asyncio.gather(*funcs)
        print("Finished sending messages. Waiting.")
        await asyncio.sleep(self.delay)
        print("Finished waiting, restarting.")
        
        
            
    
    
a = advertiser(authsDirectory="auths.txt", messageDirectory="message.txt", channelsDirectory="channels.txt")


asyncio.run(a.main())