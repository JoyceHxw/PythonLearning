import os
import shutil
import json
import webbrowser

# 创建文件夹
if os.path.exists('bilibili_decode'):
    pass
else:
    os.mkdir('bilibili_decode')
# 创建html文件
info_html=os.path.join(os.getcwd(),'bilibili_decode','info.html')
h=open(info_html,'w',encoding='utf-8')
content=''
# 修改名称，导入视频文件
path1='D:/Python/590843709'
path2=os.path.join(os.getcwd(),'bilibili_decode')
part_name=''
for dirpath, dirnames, filenames in os.walk(path1):
    for filename in filenames:
        if '.info' in filename:
            # 获取文件信息
            info=open(os.path.join(dirpath,filename),'r',encoding='utf-8')
            info_dict=json.loads(info.read())
            part_no=info_dict['PartNo']
            part_name=info_dict['PartName']
            totaltime=info_dict['TotalTime']
            createtime=info_dict['CreateDate']
            content+="分集编号："+part_no+"："+"分集名称："+part_name+"："+"分集时长："+totaltime+"："+"分集创建时间："+createtime+"："+"<br>"
            # info.close()
        if '.mp4' in filename:
            # 修改文件名称
            new_name=part_name+'.mp4'
            os.rename(os.path.join(dirpath,filename),os.path.join(dirpath,new_name))
            # 导入视频文件
            shutil.move(os.path.join(dirpath,new_name),path2)
# 写html文件
structure="""
    <html>
    <head>
    </head>
    <body>
    <p>%s<p>
    </body>
    </html>
    """%content
h.write(structure)
webbrowser.open(info_html,new=1)
h.close()

# 文件解密
for dirpath, dirnames, filenames in os.walk(path2):
    for filename in filenames:
        f1=open(os.path.join(dirpath,filename),'rb')
        if f1.read(3)==b'\xff\xff\xff':
            f1.seek(3)
            content=f1.read()
            f1.close()
            f2=open(os.path.join(dirpath,filename),'wb')
            f2.write(content)
            f2.close()