# simple-chat-app (Django Task Management App)

### 📌 日本語 (Japanese)

## 概要

このプロジェクトは Django を使用したシンプルなタスク管理アプリ（Todoアプリ）です。ユーザーはログイン後、自分専用のタスクを作成・編集・削除・完了管理することができます。

## 主な機能

ユーザー認証（ログイン / ログアウト）

タスクの追加 / 編集 / 削除

タスクの詳細表示

期限日の設定と期限順での並び替え

タスクの完了 / 未完了切り替え

## 必要環境

Python 3.10+

Django 5.x

SQLite3 (デフォルト)

## セットアップ方法

### 仮想環境の作成と有効化
```bash
python3 -m venv venv
source venv/bin/activate   # Windowsは venv\Scripts\activate

# 依存パッケージのインストール
pip install -r requirements.txt

# マイグレーション
python manage.py migrate

# 開発サーバー起動
python manage.py runserver

管理ユーザー作成

python manage.py createsuperuser
```

## デプロイ

本番環境では gunicorn + nginx を使用してデプロイ可能です。systemdでのサービス管理にも対応しています。

### 📌 English

## Overview

This project is a simple task management app (Todo app) built with Django. After logging in, each user can manage their own tasks by creating, editing, deleting, and marking them as completed.

## Features

User authentication (Login / Logout)

Create / Edit / Delete tasks

Task detail view

Set due dates and sort tasks by upcoming deadlines

Toggle task status (Completed / Incomplete)

## Requirements

Python 3.10+

Django 5.x

SQLite3 (default)

Setup

## Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run development server
python manage.py runserver

Create superuser

python manage.py createsuperuser
```

## Deployment

In production, the app can be deployed using gunicorn + nginx, with optional systemd service management.
