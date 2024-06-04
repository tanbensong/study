# study

个人学习笔记录入系统

## 安装 Django

创建虚拟环境：

```bash
python -m venv studyenv
```

激活虚拟环境：

```bash
# Windows
call studyenv\Scripts\activate.bat

# Linux/MacOS
source studyenv/bin/activate
```

安装 Django：

- python 3.12

```bash
pip install -r requirements.txt
```

创建项目：

```bash
django-admin startproject study
```

创建应用：

```bash
cd study
python manage.py startapp studyapp
```

运行项目：

```bash
python manage.py runserver
```

## study-web

### Project setup

```bash
npm install
```

#### Compiles and hot-reloads for development

```bash
npm run serve
```

#### Compiles and minifies for production

```bash
npm run build
```

### Lints and fixes files

```bash
npm run lint
```

### Customize configuration

See [Configuration Reference](https://cli.vuejs.org/config/).

