import datetime
import time

def countdown(target_date):
    while True:
        current_time = datetime.datetime.now()
        remaining_time = target_date - current_time

        if remaining_time.total_seconds() <= 0:
            print("Happy New Year!")
            break

        days, hours, minutes, seconds = remaining_time.days, remaining_time.seconds // 3600, (remaining_time.seconds // 60) % 60, remaining_time.seconds % 60

        print(f"Time until New Year: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
        time.sleep(1)

if __name__ == "__main__":
    # 设置目标日期，这里以新年为例
    target_date = datetime.datetime(datetime.datetime.now().year + 1, 1, 1, 0, 0, 0)
    
    # 调用倒计时函数
    countdown(target_date)
