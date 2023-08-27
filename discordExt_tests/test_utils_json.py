import os
import discordExt.utils.json as JSON
import unittest

class utils_json_load(unittest.TestCase):

    def tearDown(self) -> None:
        if os.path.exists("tests/test.json"):
            os.remove("tests/test.json")
    
    def test_standard_json(self):
        import json
        JSON.load_json("json")
        self.assertEqual(JSON.JSON.json, json)
        
        JSON.loads_json('{"a":"b"}')
        JSON.dumps_json({"a" :1 })
        JSON.save_file("tests/test.json", {"a" :1})    
        self.assertEqual(JSON.load_file("tests/test.json"), {"a" :1})
        
    def test_orjson(self):
        try:
            import orjson
        except ImportError:
            raise
        
        JSON.load_json("orjson")
        self.assertEqual(JSON.JSON.orjson, orjson)
        
        JSON.loads_json('{"a":"b"}')
        JSON.dumps_json({"a" :1 })
        JSON.save_file("tests/test.json", {"a" :1})    
        self.assertEqual(JSON.load_file("tests/test.json"), {"a" :1})