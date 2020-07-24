# Django練習リポジトリ
## 仮想環境構築
```
$ pipenv --python 3.8
$ pipenv --venv  # 仮想環境のパス

# Pipfileから環境再現
$ pipenv install
```

## パッケージのインストール
```
$ pipenv install django
```

## Djangoプロジェクトの作成
```
$ django-admin startproject config .  # カレントディレクトリにプロジェクト作成
```

## Djangoアプリケーションの作成
```
$ django-admin startapp accounts
```

## URLの設定
### 作成したアプリケーションとURLのマッピングを設定する
- config/urls.pyをaccounts/urls.pyにコピー
- config/urls.pyにアプリケーションのurls.pyをincludeする
- accounts/urls.pyでURLを追加していく
```
# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls'))
]
```
```
# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
```

## ビューの設定
```
# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
]
```
```
# accounts/views.py
from django.shortcuts import render, HttpResponse
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello World')

index = IndexView.as_view()
```

## テンプレート設定
```
# base.html
{% load static %}<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="{% static 'css/bootstrap.css' %}">
    <link rel="stylesheet" href="{% static 'css/all.css' %}">
    {% block extra_css %}{% endblock %}
    <title>{% block page_title %}lesson-django{% endblock %}</title>
  </head>
  <body>
    <div id="app">
      {% block main %}{% endblock %}
    </div>
    <script src="{% static 'js/jquery-3.4.1.js' %}"></script>
    <script src="{% static 'js/bootstrap.bundle.js' %}"></script>
    <script src="{% static 'js/vue.js' %}"></script>
    <script src="{% static 'js/axios.js' %}"></script>
    {% block extra_script %}{% endblock %}
  </body>
</html>
```
```
# accounts/index.html
{% extends 'base.html' %}
{% block page_title %}lesson-django - index{% endblock %}
{% block main %}
Hello World {{ msg }}
<button type="button" class="btn btn-primary">Hi</button>
{% endblock %}
```