import os
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
            data_list.append('<!DOCTYPE html>' + '\n')
            data_list.append('<meta charset="utf-8">' + '\n')
            for line in lines: 
                if line.startswith("<字>"):
                        data_0 = line.split("<")[1].split(">")[0]
                        data_1 = line.split(">")[1].split("</")[0]
                        data_list.append('<p>' + data_1 + '</p>' + '\n')
                        print("\033[93m[Tips]\033[0m 已转换1个" + data_0)

                elif line.startswith("<题1>"):
                        data_0 = line.split("<")[1].split(">")[0]
                        data_1 = line.split(">")[1].split("</")[0]
                        data_list.append('<h1>' + data_1 + '</h1>' + '\n')
                        print("\033[93m[Tips]\033[0m 已转换1个" + data_0)
                
                elif line.startswith("<题2>"):
                        data_0 = line.split("<")[1].split(">")[0]
                        data_1 = line.split(">")[1].split("</")[0]
                        data_list.append('<h2>' + data_1 + '</h2>' + '\n')
                        print("\033[93m[Tips]\033[0m 已转换1个" + data_0)
                
                elif line.startswith("<题3>"):
                        data_0 = line.split("<")[1].split(">")[0]
                        data_1 = line.split(">")[1].split("</")[0]
                        data_list.append('<h3>' + data_1 + '</h3>' + '\n')
                        print("\033[93m[Tips]\033[0m 已转换1个" + data_0)

                elif line.startswith("<题4>"):
                        data_0 = line.split("<")[1].split(">")[0]
                        data_1 = line.split(">")[1].split("</")[0]
                        data_list.append('<h4>' + data_1 + '</h4>' + '\n')
                        print("\033[93m[Tips]\033[0m 已转换1个" + data_0)
                
                elif line.startswith("<题5>"):
                        data_0 = line.split("<")[1].split(">")[0]
                        data_1 = line.split(">")[1].split("</")[0]
                        data_list.append('<h5>' + data_1 + '</h5>' + '\n')
                        print("\033[93m[Tips]\033[0m 已转换1个" + data_0)
                
                elif line.startswith("<题6>"):
                        data_0 = line.split("<")[1].split(">")[0]
                        data_1 = line.split(">")[1].split("</")[0]
                        data_list.append('<h6>' + data_1 + '</h6>' + '\n')
                        print("\033[93m[Tips]\033[0m 已转换1个" + data_0)

                elif line.startswith("<gtml>"):
                        data_0 = line.split("<")[1].split(">")[0]
                        data_list.append('<html>' + '\n')
                        print("\033[93m[Tips]\033[0m 已转换1个" + data_0)

                elif line.startswith("</gtml>"):
                        data_0 = line.split("<")[1].split(">")[0]
                        data_list.append('</html>' + '\n')
                        print("\033[93m[Tips]\033[0m 已转换1个" + data_0)
                
                elif line.startswith("<主体>"):
                        data_0 = line.split("<")[1].split(">")[0]
                        data_list.append('<body>' + '\n')
                        print("\033[93m[Tips]\033[0m 已转换1个" + data_0)

                elif line.startswith("</主体>"):
                        data_0 = line.split("<")[1].split(">")[0]
                        data_list.append('</body>' + '\n')
                        print("\033[93m[Tips]\033[0m 已转换1个" + data_0)

                elif line.startswith("<网页标题>"):
                        data_0 = line.split("<")[1].split(">")[0]
                        data_1 = line.split(">")[1].split("</")[0]
                        data_list.append('<title>' + data_1 + '</title>' + '\n')
                        print("\033[93m[Tips]\033[0m 已转换1个" + data_0)

                elif line == ("\n"):
                        data_list.append('\n')
                        print("\033[93m[Tips]\033[0m 空行" )

                else :
                    data_list.append(line + '\n')
                    print("\033[93m[Tips]\033[0m 直接写入：" + line +
                    "\033[93m[↑]\033[0m 如果这段代码不是HTML代码或注释，请检查被转换文件的GTML0.0.3beta语法是否规范" )
                
                
            print("\033[93m[Tips]\033[0m 开始写入文件...")
            with open('生成.html', 'w',encoding='utf-8') as file: 
                file.writelines(data_list)


            print("\033[93m[Tips]\033[0m 恭喜你！转换成功！在程序根目录下找到生成.html文件即可！（太乱的话可以使用格式化代码解决！）")
            print("\033[93m[Tips]\033[0m 每次转换成功都请记得删除或从程序根目录中移出生成.html文件，否则下次生成会覆盖此文件！")
            if str(input("任意键以继续")):
                os.system('cls')
                return
        
        except FileNotFoundError: 
            print('\033[91m[warning]\033[0m文件不存在！') 
            if str(input("任意键以继续")):
                os.system('cls')
                return

        except PermissionError: 
            print('\033[91[mwarning]\033[0m无权限访问文件！') 
            if str(input("任意键以继续")):
                os.system('cls')
                return



        


    else:
        print("\033[91m[warning]\033[0m 你输入的后缀是错误的！")
        if str(input("任意键以继续")):
            os.system('cls')
            return

# 更新检测
os.system('cls')
print("\033[93m[Tips]\033[0m 当前版本号 0.0.3-beta")
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
    if input() == "1":
        gtml_html ()
    else:
        print("请输入正确的选项")