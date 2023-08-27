import unittest
from discordExt.utils.json import JSON
from discordExt.utils.store import *
import os
import toml

from discordExt.utils.test import tryDelete

class utils_store_drivers(unittest.TestCase):
    def setUp(self) -> None:
        self.bigger_data_sample = {"employees":[  
            {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},  
            {"name":"Bob", "email":"bob32@gmail.com"},  
            {"name":"Jai", "email":"jai87@gmail.com"},
            ],
            "meta" : {"test" : "data"},
            "test_int" : 1,
            "test_float" : 1.0,
            "test_bool" : True,
            "test_list" : [1,2,3],
        }  
    
    def test_store_json_driver(self):
        self.test_path = "tests/test.json"
        
        # dump self.bigger_data_sample to json file
        JSON.save_file(self.test_path,self.bigger_data_sample)
        
        # test json driver
        driver = JsonDriver(path=self.test_path)
        
        # test read
        self.assertEqual(driver.get("employees"), self.bigger_data_sample["employees"])
        self.assertEqual(driver.get("meta"), self.bigger_data_sample["meta"])
        self.assertEqual(driver.get("test_int"), self.bigger_data_sample["test_int"])
        self.assertEqual(driver.get("test_float"), self.bigger_data_sample["test_float"])
        self.assertEqual(driver.get("test_bool"), self.bigger_data_sample["test_bool"])
        self.assertEqual(driver.get("test_list"), self.bigger_data_sample["test_list"])
        
        # test write
        driver["employees"][0]["name"] = "test"
        self.assertEqual(driver.get("employees")[0]["name"], "test")
        with open(self.test_path, "r") as f:
            self.assertEqual(JSON.loads_json(f.read())["employees"][0]["name"], "test")
            
        # test write 2
        driver["employees"][0]["name"] = "Shyam"
        self.assertEqual(driver.get("employees")[0]["name"], "Shyam")
        with open(self.test_path, "r") as f:
            self.assertEqual(JSON.loads_json(f.read())["employees"][0]["name"], "Shyam")
            
        # test delete
        del driver["employees"][0]["name"]
        self.assertEqual(driver.get("employees")[0], {"email":"shyamjaiswal@gmail.com"})

    def test_store_toml_driver(self):
        self.test_path = "tests/test.toml"
        
        # dump self.bigger_data_sample to toml file
        with open(self.test_path, "w") as f:
            toml.dump(self.bigger_data_sample, f)
        
        # test toml driver
        driver = TomlDriver(path=self.test_path)
        
        # test read
        self.assertEqual(driver.get("employees"), self.bigger_data_sample["employees"])
        self.assertEqual(driver.get("meta"), self.bigger_data_sample["meta"])
        self.assertEqual(driver.get("test_int"), self.bigger_data_sample["test_int"])
        self.assertEqual(driver.get("test_float"), self.bigger_data_sample["test_float"])
        self.assertEqual(driver.get("test_bool"), self.bigger_data_sample["test_bool"])
        self.assertEqual(driver.get("test_list"), self.bigger_data_sample["test_list"])
        
        # test write
        driver["employees"][0]["name"] = "test"
        self.assertEqual(driver.get("employees")[0]["name"], "test")
        with open(self.test_path, "r") as f:
            self.assertEqual(toml.load(f)["employees"][0]["name"], "test")
            
        # test write 2
        driver["employees"][0]["name"] = "Shyam"
        self.assertEqual(driver.get("employees")[0]["name"], "Shyam")
        with open(self.test_path, "r") as f:
            self.assertEqual(toml.load(f)["employees"][0]["name"], "Shyam")
            
        # test delete
        del driver["employees"][0]["name"]
        self.assertEqual(driver.get("employees")[0], {"email":"shyamjaiswal@gmail.com"})
    
        
    def test_store_py_driver(self):
        self.test_path = "tests/xtest.py"
        
        # dump self.bigger_data_sample to py file
        with open(self.test_path, "w") as f:
            for k, v in self.bigger_data_sample.items():
                f.write(f"{k} = {v}\n")
            
        # test py driver
        driver = PyDriver(path=self.test_path)
        
        # test read
        self.assertEqual(driver.get("employees"), self.bigger_data_sample["employees"])
        self.assertEqual(driver.get("meta"), self.bigger_data_sample["meta"])
        self.assertEqual(driver.get("test_int"), self.bigger_data_sample["test_int"])
        self.assertEqual(driver.get("test_float"), self.bigger_data_sample["test_float"])
        self.assertEqual(driver.get("test_bool"), self.bigger_data_sample["test_bool"])
        self.assertEqual(driver.get("test_list"), self.bigger_data_sample["test_list"])
        
        
    def tearDown(self) -> None:
        if hasattr(self, "test_path"):
            os.remove(self.test_path)
            
class utils_store_driverGroup(unittest.TestCase):
    def setUp(self) -> None:
        # create a big enough json sample
        self.bigger_data_sample = [
            {
                "id": 1,
                "first_name": "Jeanette",
                "last_name": "Penddreth",
                "email": "jpenddreth0@census.gov",
                "gender": "Female",
                "ip_address": "26.58.193.2"
            }, {
                "id": 2,
                "first_name": "Giavani",
                "last_name": "Frediani",
                "email": "gfrediani1@senate.gov",
                "gender": "Male",
                "ip_address": "229.179.4.212"
            }, {
                "id": 3,
                "first_name": "Noell",
                "last_name": "Bea",
                "email": "nbea2@imageshack.us",
                "gender": "Female",
                "ip_address": "180.66.162.255"
            }, {
                "id": 4,
                "first_name": "Willard",
                "last_name": "Valek",
                "email": "wvalek3@vk.com",
                "gender": "Male",
                "ip_address": "67.76.188.26"
            }
        ]
        
        JSON.save_file("tests/jsondriver_1.json", self.bigger_data_sample[0])
        JSON.save_file("tests/jsondriver_2.json", self.bigger_data_sample[1])
        toml.dump(self.bigger_data_sample[2], open("tests/tomldriver_1.toml", "w"))
        toml.dump(self.bigger_data_sample[3], open("tests/tomldriver_2.toml", "w"))
        
        self.jsondriver_1 = JsonDriver(path="tests/jsondriver_1.json")
        self.jsondriver_2 = JsonDriver(path="tests/jsondriver_2.json")
        self.tomldriver_1 = TomlDriver(path="tests/tomldriver_1.toml")
        self.tomldriver_2 = TomlDriver(path="tests/tomldriver_2.toml")
        
    
    def test_drivergroup_std(self):
        self.drivergroup = DriverGroup(
            self.jsondriver_1, self.jsondriver_2, self.tomldriver_1, self.tomldriver_2
        )
        
        self.assertEqual(self.drivergroup.get("id"), 1)
        self.assertEqual(self.drivergroup.get("first_name"), "Jeanette")
        self.assertEqual(self.drivergroup.get("last_name"), "Penddreth")
        self.assertEqual(self.drivergroup.get("email"), "jpenddreth0@census.gov")
        
        self.drivergroup.reorder(1,0,2,3)
        
        self.assertEqual(self.drivergroup.get("id"), 2)
        self.assertEqual(self.drivergroup.get("first_name"), "Giavani")
        self.assertEqual(self.drivergroup.get("last_name"), "Frediani")
        self.assertEqual(self.drivergroup.get("email"), "gfrediani1@senate.gov")
        
        self.drivergroup.reorder(2,1,0,3)
        
        self.assertEqual(self.drivergroup.get("id"), 3)
        self.assertEqual(self.drivergroup.get("first_name"), "Noell")
        self.assertEqual(self.drivergroup.get("last_name"), "Bea")
        self.assertEqual(self.drivergroup.get("email"), "nbea2@imageshack.us")
        
        self.drivergroup.reorder(3,2,1,0)
        
        self.assertEqual(self.drivergroup.get("id"), 4)
        self.assertEqual(self.drivergroup.get("first_name"), "Willard")
        self.assertEqual(self.drivergroup.get("last_name"), "Valek")
        self.assertEqual(self.drivergroup.get("email"), "wvalek3@vk.com")
    
    def test_drivergroup_collection(self):
        self.drivergroup = DriverGroup(
            self.jsondriver_1, self.jsondriver_2, self.tomldriver_1, self.tomldriver_2,
        )
        
        self.drivergroup.MODE = "COLLECTION"
        
        ids = self.drivergroup.get("id")
        self.assertEqual(ids, [1,2,3,4])
        
        first_names = self.drivergroup.get("first_name")
        self.assertEqual(first_names, ["Jeanette", "Giavani", "Noell", "Willard"])
        
        last_names = self.drivergroup.get("last_name")
        self.assertEqual(last_names, ["Penddreth", "Frediani", "Bea", "Valek"])
        
    def tearDown(self) -> None:
        # remove files
        tryDelete("tests/jsondriver_1.json")
        tryDelete("tests/jsondriver_2.json")
        tryDelete("tests/tomldriver_1.toml")
        tryDelete("tests/tomldriver_2.toml")