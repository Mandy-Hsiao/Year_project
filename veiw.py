import sys
from django.conf import settings
from django.http import HttpResponse
from django.urls import path
from django.core.management import execute_from_command_line


html = """
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <title>Django 第一個頁面</title>
    <style>
        body {
            margin: 0;
            font-family: "Microsoft JhengHei", sans-serif;
            background: #f7f4ef;
            color: #1a2744;
        }

        .navbar {
            background: #1a2744;
            color: white;
            padding: 18px 40px;
            font-size: 20px;
            font-weight: bold;
        }

        .hero {
            padding: 80px 40px;
            text-align: center;
        }

        .card {
            max-width: 720px;
            margin: 0 auto;
            background: white;
            border-radius: 18px;
            padding: 40px;
            box-shadow: 0 10px 30px rgba(26, 39, 68, 0.12);
        }

        h1 {
            font-size: 36px;
            margin-bottom: 16px;
        }

        p {
            font-size: 18px;
            line-height: 1.8;
            color: #4a5068;
        }

        .btn {
            display: inline-block;
            margin-top: 24px;
            padding: 12px 28px;
            background: #1a2744;
            color: white;
            border-radius: 8px;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <div class="navbar">My Django Website</div>

    <div class="hero">
        <div class="card">
            <h1>成功看到 Django 頁面！</h1>
            <p>
                這是一個用 Python Django 寫出來的第一個網頁。
                目前這個版本先不用資料庫，也不用 templates，
                目標是先確認 Django 可以正常顯示頁面。
            </p>
            <a class="btn" href="/">回到首頁</a>
        </div>
    </div>
</body>
</html>
"""


def index(request):
    return HttpResponse(html)


urlpatterns = [
    path("", index),
]


if __name__ == "__main__":
    settings.configure(
        DEBUG=True,
        SECRET_KEY="django-single-page-secret-key",
        ROOT_URLCONF=__name__,
        ALLOWED_HOSTS=["*"],
        MIDDLEWARE=[],
    )

    execute_from_command_line(sys.argv)