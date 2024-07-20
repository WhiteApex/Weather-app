import os 
from datetime import datetime as dt , timedelta as td


LOGS_PATH = 'log.txt'
 
if not os.path.exists(LOGS_PATH): 
    open(LOGS_PATH, mode='x', encoding="utf-8") 
 
LOGS_LIMIT = 25 

number_to_weekday = {
    0: 'Понедельник',
    1: 'Вторник',
    2: 'Среда',
    3: 'Четверг',
    4: 'Пятница',
    5: 'Суббота',
    6: 'Воскресенье',
}

def log(text: str): 
    time = (dt.now() + td(hours=5)).isoformat(sep=" ", timespec="seconds")  
    log_line = f"[{time}] {text}" 
    with open(LOGS_PATH, "r+", encoding="utf-8") as log_file: 
        current_logs = log_file.readlines() 
         
        logs_to_keep = current_logs[-LOGS_LIMIT + 1:] 
        logs_to_keep.append(log_line + "\n") 
         
        log_file.seek(0) 
        log_file.truncate() 
        log_file.writelines(logs_to_keep)