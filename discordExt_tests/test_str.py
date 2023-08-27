import unittest
from discordExt.funcs.str import *

class funcs_str(unittest.TestCase):
    def test_get_type(self):
        f = "<#4124124124>"
        a, b = get_type(f)
        self.assertEqual(a, STRING_TYPE.CHANNEL)
        self.assertEqual(b, "4124124124")

        f = "<@4124124124>"
        a, b = get_type(f)
        self.assertEqual(a, STRING_TYPE.USER)
        self.assertEqual(b, "4124124124")

        f = "<@!4124124124>"
        a, b = get_type(f)
        self.assertEqual(a, STRING_TYPE.USER)
        self.assertEqual(b, "4124124124")

        f = "<@&4124124124>"
        a, b = get_type(f)
        self.assertEqual(a, STRING_TYPE.ROLE)
        self.assertEqual(b, "4124124124")

        f = "<#4124124124>"
        a, b = get_type(f)
        self.assertEqual(a, STRING_TYPE.CHANNEL)
        self.assertEqual(b, "4124124124")

        f = "<:sadasd:4124124124:>"
        a, b = get_type(f)
        self.assertEqual(a, STRING_TYPE.EMOJI)
        self.assertEqual(b, "sadasd:4124124124")

        f = "Hello"
        a, b = get_type(f)
        self.assertEqual(a, STRING_TYPE.TEXT)
        self.assertEqual(b, "Hello")
        
    def test_get_text_styles(self):
        string = "**World**"
        a = get_styles(string)
        self.assertEqual(a.get("format"), [TEXT_FORMAT.BOLD])
        
        string = "__World__"
        a = get_styles(string)
        self.assertEqual(a.get("format"), [TEXT_FORMAT.UNDERLINE])
        
        string = "~~World~~"
        a = get_styles(string)
        self.assertEqual(a.get("format"), [TEXT_FORMAT.STRIKETHROUGH])
        
        string = "`World`"
        a = get_styles(string)
        self.assertEqual(a.get("format"), [TEXT_FORMAT.CODE])
        
        string = "```World```"
        a = get_styles(string)
        self.assertEqual(a.get("format"), [TEXT_FORMAT.CODEBLOCK])
        
        string = "```py\nWorld```"
        a = get_styles(string)
        self.assertEqual(a.get("format"), [TEXT_FORMAT.CODEBLOCK_WITH_DECO])
        self.assertEqual(a.get("deco"), "py")

from discordExt.com.str import *
  
class com_str(unittest.TestCase):
    def test_parsestring(self):
        x = parseString(
            "xxxx hello <#1244142412> check again <aasddsd> and <@!444124124>"
        )
        pass