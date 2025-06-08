from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# 默认寿命（岁）
LIFE_EXPECTANCY = 78.2

def calculate_life_time(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')
    today = datetime.today()
    age_in_days = (today - birthdate).days
    total_days = LIFE_EXPECTANCY * 365.25
    day_fraction = age_in_days / total_days
    total_minutes = 24 * 60 * day_fraction
    hour = int(total_minutes // 60)
    minute = int(total_minutes % 60)
    period = "AM" if hour < 12 else "PM"
    hour_display = hour if 1 <= hour <= 12 else (hour - 12 if hour > 12 else 12)

    # 文案提示
    if hour < 6:
        message = "黎明时分，人生的起点，尽情探索吧。"
    elif hour < 12:
        message = "上午时光，正是蓄力奔跑的阶段。"
    elif hour < 18:
        message = "下午时分，请坚定地迈向人生目标。"
    else:
        message = "黄昏将至，珍惜时光，不留遗憾。"

    return f"{hour_display:02}:{minute:02} {period}", message

@app.route('/', methods=['GET', 'POST'])
def index():
    time_result = None
    message = None
    birthdate = None
    if request.method == 'POST':
        birthdate = request.form['birthdate']
        time_result, message = calculate_life_time(birthdate)
    return render_template('index.html', time_result=time_result, message=message, birthdate=birthdate)

if __name__ == '__main__':
    app.run(debug=True)
