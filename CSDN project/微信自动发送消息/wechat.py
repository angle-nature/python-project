import pyautogui
import pyperclip
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


def main():
    pyautogui.PAUSE = 0

    icon_position = pyautogui.Point(x=1635, y=1061)  # 任务栏图标位置
    entry_position = pyautogui.Point(x=1693, y=336)  # 输入框位置

    pyautogui.moveTo(icon_position, duration=1)  # duration为执行时长，可选
    pyautogui.click(icon_position)
    pyautogui.moveTo(entry_position, duration=0.7)
    pyautogui.click(entry_position)
    pyautogui.click(entry_position)
    pyperclip.copy('正在进行发pyautogui试验，看到请忽略，更不要骂傻逼')  # 复制
    pyautogui.hotkey('ctrl', 'v')  # 按下组合键的方法，ctrl+v粘贴
    pyautogui.press('enter')  # 按下按键
    pyautogui.typewrite([*list('zhengzai '), *list('jinxing '), 'shift', *list('pyautogui'), 'shift', *list('shiyan '), 'enter'], 0.1) # 第二个参数为按下每一个字母的间隔，可选


scheduler = BlockingScheduler()  # 实例化一个调度器
scheduler.add_job(main, 'date', run_date=datetime(2021, 9, 15, 11, 27, 00))  # 添加任务
scheduler.start()

