import os
API1_Path=os.path.abspath('.')+'\\API1.py'
Manage_Path=os.path.abspath('.')+'\\manage.py'
os.system('cmd/c start python '+API1_Path)
os.system('cmd/c start python '+Manage_Path+" runserver")
print("当两个服务均成功启动之后即可使用")
