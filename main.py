from random import choice
import aiohttp
import asyncio


class advertiser:
    def __init__(self, authsDirectory: str, messageDirectory: str, channelsDirectory: str, delay: int = 300) -> str:
        self.authsDirectory = authsDirectory
        self.messageDirectory = messageDirectory
        self.channelsDirectory = channelsDirectory
        self.delay = delay
        self.message = open(messageDirectory).read()

    async def sendMessage(self, channel, auth):
        data = {
            "content": self.message
        }
        headers = {
            "Authorization": auth
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(f"https://discord.com/api/v9/channels/{channel}/messages", data=data, headers=headers) as response:
                return response.status

    async def main(self):
        channels = [channel for channel in open(
            self.channelsDirectory).read().splitlines()]
        account = choice([auth for auth in open(
            self.authsDirectory).read().splitlines()])

        funcs = [self.sendMessage(channel, account) for channel in channels]
        responses = await asyncio.gather(*funcs)
        print(f"Sent messages with responses: {responses}")
        await asyncio.sleep(self.delay)


a = advertiser(authsDirectory="auths.txt",
               messageDirectory="message.txt", channelsDirectory="channels.txt")

while True:
    asyncio.run(a.main())
