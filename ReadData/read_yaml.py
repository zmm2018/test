# 导入yaml的包 打开读取文件
import yaml
import os
# with open((os.getcwd() + os.sep +"data01.yaml"),"r",encoding="utf-8") as f:
def read_yaml():

    with open("../Data/data01.yaml", "r", encoding="utf-8") as f:

        return  yaml.load(f)

if __name__ == '__main__':

    print("")