from datetime import datetime
import unittest

import discord
from discordExt.com.embed import EmbedModel

class com_embed_attrs(unittest.TestCase):

    def setUp(self) -> None:
        self.e = EmbedModel(
            title="test {test1}",
            description="test {test2}",
            url="https://{test3}",
            timestamp=datetime.now(),
            color=0x000000,
            footer={"text" : "test {test5}"},
            fields=[
                {"name":"test {test9}", "value" : "test {test10}"},
                {"name":"test {test11}", "value" : "test {test12}"}
            ]
        )

    def test_embed_vars_1(self):
        """
        structure
        title : str
        description : str
        url : str 
        color : int
        timestamp : str
        footer : FooterModel 
        image : str 
        thumbnail : str
        author : AuthorModel 
        fields : typing.List[EmbedFieldModel] 
        
        """
        
        values, unique, children = self.e._one_time_parse_format_vars
        self.assertEqual(children, ["footer","fields"])
        self.assertEqual(values["title"], ["test1"])
        self.assertEqual(values["description"], ["test2"])
        self.assertEqual(values["url"], ["test3"])        
        self.assertEqual(unique, {"test1","test2","test3",})
        
    def test_format_1(self):
        
        h = self.e.format(
            test1="test1",
            test2="test2",
            test3="test3",
            test4="test4",
            test5="test5",
            test7="test7",
            test9="test9",
            test10="test10",
            test11="test11",
            test12="test12"
        )
        
        self.assertEqual(h.title, "test test1")
        self.assertEqual(h.description, "test test2")
        self.assertEqual(h.url, "https://test3")
        self.assertEqual(h.footer.text, "test test5")
        self.assertEqual(h.fields[0].name, "test test9")
        self.assertEqual(h.fields[0].value, "test test10")
        self.assertEqual(h.fields[1].name, "test test11")
        self.assertEqual(h.fields[1].value, "test test12")
        
        embed = h.toEmbed()
        self.assertIsInstance(embed, discord.Embed)
        self.assertEqual(embed.title, "test test1")
        self.assertEqual(embed.description, "test test2")
        self.assertEqual(embed.url,  "https://test3")
        self.assertEqual(embed.footer.text, "test test5")
        self.assertEqual(embed.fields[0].name, "test test9")
        self.assertEqual(embed.fields[0].value, "test test10")
        self.assertEqual(embed.fields[1].name, "test test11")
        self.assertEqual(embed.fields[1].value, "test test12")
        
        x, model = self.e.parse(embed)
        self.assertEqual(
            len(x), 8
        )
        