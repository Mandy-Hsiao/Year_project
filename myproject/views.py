from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json


def chatbot(request):
    return render(request, "chatbot.html")


@csrf_exempt
def chat_api(request):
    if request.method != "POST":
        return JsonResponse({"error": "只支援 POST 請求。"}, status=405)

    try:
        payload = json.loads(request.body.decode("utf-8"))
        message = payload.get("message", "").strip()
    except (ValueError, UnicodeDecodeError):
        return JsonResponse({"error": "無效的 JSON。"}, status=400)

    if not message:
        return JsonResponse({"reply": "請輸入一句話，我可以跟你聊天。"})

    lower_message = message.lower()
    if "你好" in lower_message or "您好" in lower_message:
        reply = "你好！有什麼我可以幫忙的嗎？"
    elif "天氣" in lower_message:
        reply = "今天的天氣很不錯，適合聊天和喝杯咖啡。"
    elif "再見" in lower_message or "bye" in lower_message:
        reply = "再見！希望很快再跟你聊天。"
    elif "幫助" in lower_message or "?" in lower_message:
        reply = "我可以聽你說話、回覆簡單問題，試試問我今天、天氣或說你好。"
    else:
        reply = f"你說的是：{message}，我還在學習更多對話技巧。"

    return JsonResponse({"reply": reply})
