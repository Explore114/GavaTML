import os
import re
from loguru import logger
os.system('cls')
data_list = []
# 定义转换字典
gtml_html_dict = {
    '<gtml>': '<html>',
    '</gtml>': '</html>',
    '<配置>': '<head>',
    '</配置>': '</head>',
    '<内容>': '<body>',
    '</内容>': '</body>',
    '<字': '<p',
    '</字': '</p',
    '<标题1': '<h1',
    '</标题1': '/<h1',
    '<标题2': '<h2',
    '</标题2': '</h2',
    '<标题3': '<h3',
    '</标题3': '</h3',
    '<标题4': '<h4',
    '</标题4': '</h4',
    '<标题5': '<h5',
    '</标题5': '</h5',
    '<标题6': '<h6',
    '</标题6': '</h6',
    '<链接': '<a',
    '</链接': '</a',
    '<表格>': '<table>',
    '</表格': '</table>',
    '<行':'<tr',
    '</行>': '</tr',
    '<列标题>': '<th',
    '</列标题>': '</th',
    


}
gtml_html_dict_key = list(gtml_html_dict.keys())


# 定义一些函数
# # 这里定义的是gtml转到html的函数
def gtml_html ():
    os.system('cls')
    file = str(input("文件路径:"))
    # 后缀判断
    if file[-5:] == ".gtml":
        # 异常处理
        try: 
            logger.info("海内存知己，天涯若比邻(?)稍安勿躁，欣赏一下日志罢")
            with open(file, 'r',encoding='utf-8') as html_file: 
                lines = html_file.readlines() 
            logger.success("文件读取成功！")
            data_list.append('<!DOCTYPE html>' + '\n')
            data_list.append('<meta charset="utf-8">' + '\n')
            for line in lines:
                if line == '\n':
                    data_list.append('\n')
                    logger.info("空行将仍然写入")
                else:
                    # 判断该行是否有字典中的键
                    pattern = '|'.join(gtml_html_dict_key)
                    match = re.findall(pattern, line)
                    if not match:
                        logger.warning("代码：" + line + '\n' + "没有被转换器识别为gtml代码，将原样写入！")
                        data_list.append(line)
                    else:
                        for key in match:
                            convert_data = re.sub(key, gtml_html_dict[key], line, count=0)
                            logger.success("代码：" + line + '\n' + "已被转换为：" + convert_data)
                            line = convert_data
                        data_list.append(convert_data)




                
                
            logger.info("开始写入文件，请勿退出程序！")
            with open('生成.html', 'w',encoding='utf-8') as file: 
                file.writelines(data_list)

            logger.success("恭喜你！转换成功！在程序根目录下找到生成.html文件即可！（太乱的话可以使用格式化代码解决！）")
            logger.info("每次转换成功都请记得删除或从程序根目录中移出生成.html文件，否则下次生成会覆盖此文件！")
            if str(input("任意键以继续")):
                os.system('cls')
                return
        
        except FileNotFoundError: 
            logger.warning("文件不存在")  
            if str(input("任意键以继续")):
                os.system('cls')
                return

        except PermissionError: 
            logger.warning("无权限访问") 
            if str(input("任意键以继续")):
                os.system('cls')
                return



        


    else:
        logger.warning("路径后缀错误！")
        if str(input("任意键以继续")):
            os.system('cls')
            return

# 更新检测
os.system('cls')
logger.info("当前版本号 0.0.3-beta")
logger.info("该版本没有更新检测:( 如需查找更新请前往项目地址 https://github.com/Explore114/GavaTML/releases ！靴靴")


# 主页面


while True:
    print(""" \
  _______      ___   ____    ____  ___   .___________.___  ___.  __      
 /  _____|    /   \  \   \  /   / /   \  |           |   \/   | |  |     
|  |  __     /  ^  \  \   \/   / /  ^  \ `---|  |----|  \  /  | |  |     
|  | |_ |   /  /_\  \  \      / /  /_\  \    |  |    |  |\/|  | |  |     
|  |__| |  /  _____  \  \    / /  _____  \   |  |    |  |  |  | |  `----.
 \______| /__/     \__\  \__/ /__/     \__\  |__|    |__|  |__| |_______|
                                                                                                                                                                               
""")
    print("主菜单")
    print("1.gtml转html")
    print("2.还没做好！提交PR可以加快开发进度哟~")
    if input() == "1":
        gtml_html ()
    else:
        logger.warning("请输入正确选项！")