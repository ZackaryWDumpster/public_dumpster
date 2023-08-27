import asyncio
import unittest

import discord
from discordExt.com.bot import xBot
from discordExt.utils.store import MemoryDriver
from discordExt.com.objectOnDemand import DiscordObjectDriver, DiscordObjectSpecifier
from discordExt.utils.test import quickDebug

class com_bot(unittest.IsolatedAsyncioTestCase):
    async def test_bot_run_and_cache_load(self):
        quickDebug()
        #load .env and get token
        import os
        from dotenv import load_dotenv
        load_dotenv()
        
        bot: xBot = xBot.default()

        user = DiscordObjectSpecifier(
            "USER",
            os.getenv("testUser")
        )
        
        guild = DiscordObjectSpecifier(
            "GUILD",
            os.getenv("testGuild")
        )
        
        subchannel = DiscordObjectSpecifier(
            "CHANNEL",
            os.getenv("testChannel"),
            os.getenv("testGuild")
        )
        
        driver = MemoryDriver()
        driver["user"] = user
        driver["guild"] = guild
        driver["subchannel"] = subchannel
        
        
        
        bot.x_odc_add_cache(DiscordObjectDriver(driver=driver))
        #bot.start("", reconnect=False)
        asyncio.create_task(bot.start(os.getenv("token"), reconnect=False))
        await asyncio.sleep(5)
        print("control is back")
        
        self.assertIsInstance(bot.cache["user"], discord.User)
        print(bot.cache["user"])
        self.assertIsInstance(bot.cache["guild"], discord.Guild)
        print(bot.cache["guild"])
        self.assertIsInstance(bot.cache["subchannel"], discord.TextChannel)
        print(bot.cache["subchannel"])
        
        await bot.close()
         
        
