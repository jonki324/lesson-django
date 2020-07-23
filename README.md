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
## 作成したアプリケーションとURLのマッピングを設定する
- config/urls.pyをaccounts/urls.pyにコピー
- config/urls.pyにアプリケーションのurls.pyをincludeする
- accounts/urls.pyでURLを追加していく
```
# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts/urls'))
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