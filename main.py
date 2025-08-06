import os
import time
os.system('cls')
data_list = []
# 定义一些函数
# # 这里定义的是gtml转到html的函数
def gtml_html ():
    os.system('cls')
    file = str(input("文件路径:"))
    # 后缀判断
    if file[-5:] == ".gtml":
        # 异常处理
        try: 
            print("\033[93m[Tips]\033[0m 海内存知己，天涯若比邻(?)稍安勿躁，欣赏一下日志罢")
            with open(file, 'r',encoding='utf-8') as html_file: 
                lines = html_file.readlines() 
            print("\033[93m[Tips]\033[0m 文件读取成功！")
            for line in lines: 
                if line.startswith("字"):
                        data = line.split(" ")
                        data_list.append('<p>' + data[1] + '</p>')
                        print("\033[93m[Tips]\033[0m 已转换1个" + data[0])

                elif line.startswith("题1"):
                        data = line.split(" ")
                        data_list.append('<h1>' + data[1] + '</h1>')
                        print("\033[93m[Tips]\033[0m 已转换1个" + data[0])

                elif line.startswith(""):
                        data_list.append('')
                        print("\033[93m[Tips]\033[0m 空行已被忽略" )

                else :
                    data_list.append(line)
                    print("\033[93m[Tips]\033[0m 直接写入：" + line )
                
            print("\033[93m[Tips]\033[0m 开始写入文件...")
            with open('生成.html', 'w',encoding='utf-8') as file: 
                file.writelines(data_list)


            print("\033[93m[Tips]\033[0m 恭喜你！转换成功！在程序根目录下找到生成.html文件即可！（太乱的话可以使用格式化代码解决！）")
            print("\033[93m[Tips]\033[0m 每次转换成功都请记得删除或从程序根目录中移出生成.html文件，否则下次生成会出现冲突！")
            if str(input("键入空格以继续")) == " ":
                os.system('cls')
                return
        
        except FileNotFoundError: 
            print('\033[91m[warning]\033[0m文件不存在！') 
            if str(input("键入空格以继续")) == " ":
                os.system('cls')
                return

        except PermissionError: 
            print('\033[91[mwarning]\033[0m无权限访问文件！') 
            if str(input("键入空格以继续")) == " ":
                os.system('cls')
                return



        


    else:
        print("\033[91m[warning]\033[0m 你输入的后缀是错误的！")
        if str(input("键入空格以继续")) == " ":
            os.system('cls')
            return

# 更新检测
os.system('cls')
print("\033[93m[Tips]\033[0m 当前版本号 0.0.1-beta")
print("\033[93m[Tips]\033[0m 该版本没有更新检测:( 如需查找更新请前往项目地址 \033[94mhttps://github.com/Explore114/GavaTML/releases\033[0m ！靴靴")

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
    Options = int(input())
    if Options == 1:
        gtml_html ()

    else:
        print("请输入正确的选项")