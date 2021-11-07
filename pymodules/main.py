'''
Author: 兄弟们Go
Date: 2021-11-07 17:01:31
LastEditTime: 2021-11-07 19:19:47
LastEditors: 兄弟们Go
Description: 
FilePath: \pymodules\pymodules\main.py

'''
import importlib
class require(object):
    def __init__(self,name):
        self.__RequireManageData__ ={
            'obj':None,
            '_obj':None,
            'spec':None,
            'name':name,
            'at':None,
            'imported':False
        }
    def __call__(self,*args,**kwargs):
        self.__check_imported()
        return self.__RequireManageData__["obj"](*args,**kwargs)
    def at(self,name):
        self.__RequireManageData__["at"] = name
        return self
    def __getattr__(self, name):
        if(name != "__RequireManageData__"):
            self.__check_imported()
            return getattr(self.__RequireManageData__["obj"],name,None)
        return super().__getattr__(name)
    def __can_require(self,name):
        self.__RequireManageData__["spec"] = importlib.util.find_spec(name)
        if self.__RequireManageData__["spec"] is None:
            return False
        else:
            return True
    def __import(self,name):
        if self.__can_require(name)==False:
            raise ModuleNotFoundError(f'No module named {name!r}',name)
        module = importlib.util.module_from_spec(self.__RequireManageData__["spec"])
        self.__RequireManageData__["spec"].loader.exec_module(module)
        self.__RequireManageData__["imported"] = True
        if self.__RequireManageData__["at"] is None:
            self.__RequireManageData__["obj"] = module
        else:
            self.__RequireManageData__["_obj"] = module
            self.__RequireManageData__["obj"] = getattr(self.__RequireManageData__["_obj"],self.__RequireManageData__["name"],None)
    def _resolve_name(self):
        if self.__RequireManageData__["at"] is not None:
            return self.__RequireManageData__["at"]
        return self.__RequireManageData__["name"]
    def __check_imported(self):
        if self.__RequireManageData__["imported"]==False:
            package=self._resolve_name()
            self.__import(package)
    # importlib.import_module()
    def __str__(self):
        """
        字符串表示
        """
        self.__check_imported()
        if(self.__RequireManageData__["imported"]):
            return '<{0}.{1} object at {2} wrapped in {3}>'.format(
            self.__module__,type(self.__RequireManageData__["obj"]).__name__,
            hex(id(self.__RequireManageData__["obj"])),hex(id(self)))
        return '<{0}.{1} object at {2}>'.format(
            self.__module__,type(self).__name__,hex(id(self)))
    def __repr__(self):
        return self.__str__()

if __name__ == '__main__':
    a = require("tkinter")
    print(a)