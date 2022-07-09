# WEWO 笔记

WEWO 是一款基于 django 和 vue 的 web 笔记应用，是 flomo 的重新实现，功能设计上有不少修改。WEWO 支持：

- 基础 markdown 语法
- 笔记内容搜索
- 标签系统，支持标签过滤
- 笔记链接系统，支持显示链接笔记
- 图床
- 笔记统计

demo: http://wuud.fun:8000

测试账号:  admin | 123456

## 环境要求

- python
- （默认）sqlite，无需额外安装  
- （可选）其他数据库，如 mysql 

## 部署

1. 安装 requirement.txt：
```
pip install -r requirement.txt
```

2. 默认使用 sqlite，若要使用其他数据库，请修改 server/settings.py 文件：（这里的账号密码是没用的🤣）
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'notes',
        # 'USER': 'root',
        # 'PASSWORD': 'qweasd123456.',
        # 'HOST': 'localhost',
        # 'PORT': '3306',
    }
}
```

3. 迁移数据库，自动创建数据表：
```
python manage.py migrate
```

4. 本地运行服务端。如果是 Linux 系统并使用 virtualenv，可以直接运行shell脚本 `run.sh`
```
python manage.py runserver 0.0.0.0:8000
```

5. 访问网页 `http://localhost:8000/` 或 `http://server.address:8000/`

6. 如果环境运行正常，可以在 `server/settings` 文件中，修改 `DEBUG = False`，关闭调试信息的显示。

## 支持

如有更多问题，请联系 baiqiletter@gmail.com
