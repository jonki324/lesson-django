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
