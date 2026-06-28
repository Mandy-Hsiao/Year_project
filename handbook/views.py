from django.shortcuts import render


RATE_TABLE = {
    "國小解題教室": {"base": 10, "preparation": 115, "image": 35, "material": 0},
    "國中解題教室": {"base": 15, "preparation": 140, "image": 35, "material": 0},
    "高中解題教室": {"base": 20, "preparation": 165, "image": 35, "material": 0},
}


def home(request):
    return render(request, "home.html")


def salary_calculator(request):
    result = None
    if request.method == "POST":
        try:
            lesson_label = request.POST.get("lesson_label", "")
            duration_minutes = float(request.POST.get("duration_minutes", 0))
            question_count = float(request.POST.get("question_count", 0))

            rate = RATE_TABLE.get(lesson_label)
            if not rate:
                result = {"error": "請選擇有效的課程標籤。"}
            else:
                preparation_fee = rate["preparation"]
                image_fee = rate["image"]
                material_fee = rate["material"]
                base_fee = rate["base"]
                duration_fee = round((preparation_fee + image_fee + material_fee) * (duration_minutes / 30), 2)
                question_fee = round(question_count * base_fee, 2)
                total_salary = round(duration_fee + question_fee, 2)
                result = {
                    "lesson_label": lesson_label,
                    "duration_minutes": duration_minutes,
                    "question_count": question_count,
                    "preparation_fee": preparation_fee,
                    "image_fee": image_fee,
                    "material_fee": material_fee,
                    "duration_fee": duration_fee,
                    "question_fee": question_fee,
                    "total_salary": total_salary,
                }
        except ValueError:
            result = {"error": "請輸入有效的數字。"}

    return render(request, "salary_calculator.html", {"result": result})


def salary_chatbot(request):
    return render_chatbot(request, "salary", "報酬問題")


def absence_chatbot(request):
    return render_chatbot(request, "absence", "無法到課問題")


def entry_chatbot(request):
    return render_chatbot(request, "entry", "入職申請問題")


def render_chatbot(request, theme, title):
    session_key = f"chat_messages_{theme}"
    messages = request.session.get(session_key, [])

    if request.method == "POST":
        question = request.POST.get("question", "").strip()
        if question:
            messages.append({"role": "user", "content": question})
            messages.append({"role": "assistant", "content": get_answer(question, theme)})
            request.session[session_key] = messages
            request.session.modified = True

    return render(request, "chatbot.html", {"messages": messages, "title": title, "theme": theme})


def get_answer(question, theme):
    q = question.lower()

    if theme == "salary":
        if any(keyword in q for keyword in ["薪水", "salary", "待遇", "津貼", "報酬", "pay"]):
            return "報酬問題：教學報酬由準備費、形象費、教材加給與解題費組成。"
        return "這是報酬專區，您可以詢問薪水、待遇、津貼或報酬相關問題。"

    if theme == "absence":
        if any(keyword in q for keyword in ["請假", "缺課", "不能到課", "無法到課", "遲到", "leave", "absent"]):
            return "請先向學校行政單位或系主任說明情況，並依照流程提交請假或補課申請。"
        return "這是請假與缺課專區，您可以詢問無法到課、請假或補課相關問題。"

    if theme == "entry":
        if any(keyword in q for keyword in ["入職", "報到", "申請", " onboarding", "hire", "入用"]):
            return "入職時需準備相關證件、完成報到流程，並確認學校要求的文件與時間。"
        return "這是入職申請專區，您可以詢問報到、申請文件或入職流程相關問題。"

    return "請直接輸入與此主題相關的問題。"
