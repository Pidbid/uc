# -*- coding: utf-8 -*-
'''
@File    :   cu.py
@Time    :   2022/09/16 15:38:12
@Author  :   Wicos 
@Version :   1.0
@Site    :   https://wicos.me
@Email   :   wicos@wicos.cn
'''

import os
import json
import subprocess
import getopt
import sys


class cloudUp:
    def __init__(self) -> None:
        self.path = os.path.realpath(__file__).replace("\\", "/")
        self.__config_init__()

    def __config_init__(self):
        self.cli = '%Hbuilder%\cli'
        self.provider =self.__provider_init__()
        self.project = self.path.split("/")[-2]

    def __provider_init__(self):
        file_list = os.listdir()
        for i in file_list:
            if "uniCloud-aliyun" in i:
                return "aliyun"
            elif "uniCloud-tcb" in i:
                return "tcb"
        return None

    def __get_resource__(self, resource):
        if resource in ["cf", "cloudfunction"]:
            self.resource = "cloudfunction"
        if resource in ["cm", "common"]:
            self.resource = "common"
        if resource in ["db"]:
            self.resource = "db"
        if resource in ["vf"]:
            self.resource = "vf"
        if resource in ["ac", "action"]:
            self.resource = "action"
        if resource in ["sp", "space"]:
            self.resource = "space"

    # def
    def __run__(self, action):
        if action == "list":
            command = "{} cloud functions --list {} --prj {} --provider {} --cloud".format(
                self.cli, self.resource, self.project, self.provider)
            result = subprocess.Popen(
                command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if action == "upload":
            command = "{} cloud functions --upload {} --prj {} --provider {} --name {} --force".format(
                self.cli, self.resource, self.project, self.provider, self.name)
            result = subprocess.Popen(
                command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if action == "download":
            command = "{} cloud functions --download {} --prj {} --provider {} --name {} --force".format(
                self.cli, self.resource, self.project, self.provider, self.name)
            result = subprocess.Popen(
                command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        try:
            outs, errs = result.communicate(timeout=20)
            print(str(outs, 'gbk'))
        except subprocess.TimeoutExpired:
            result.kill()
            outs, errs = result.communicate()

    def start(self):
        opts, args = getopt.getopt(sys.argv[1:], "uld", [
                                   "upload", "list", "download"])
        action = ""
        for o, a in opts:
            # action
            if o in ["-u", "--upload"]:
                action = "upload"
            if o in ["-d", "--download"]:
                action = "download"
            if o in ["-l", "--list"]:
                action = "list"
        if action == "list":
            if len(args) != 1:
                print("-l 模式下只能输入一个资源模式 如 -l cf 或 -l cloudfunction")
                return 0
            else:
                self.__get_resource__(args[0])
                self.__run__(action)
        if action == "upload":
            if len(args) != 2:
                print("-u 模式下必须输入两个值 如 -u cf fun1 表示上传fun1云函数至云空间  默认强制覆盖")
                return 0
            else:
                self.__get_resource__(args[0])
                self.name = args[1]
                self.__run__(action)
        if action == "download":
            if len(args) != 2:
                print("-d 模式下必须输入两个值 如 -d cf fun1 表示下载fun1云函数至本地  默认强制覆盖")
                return 0
            else:
                self.__get_resource__(args[0])
                self.name = args[1]
                self.__run__(action)


if __name__ == "__main__":
    cu = cloudUp()
    cu.start()
