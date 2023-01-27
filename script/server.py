import subprocess
import fire
import os
from loguru import logger
from colorama import init, Fore, Back, Style

init(autoreset=True)

# start_command = "nohup /opt/homebrew/bin/hugo server -s ~/Mind/blogpages -D -p 1313 --disableFastRender >/dev/null 2>&1 &"
start_command = "nohup /opt/homebrew/bin/hugo server -s ~/Mind/blogpages -e production -p 1313 --disableFastRender >/dev/null 2>&1 &"
stop_command = "ps -ef|grep -v grep|grep hugo|awk '{print $2}'|xargs kill -9"
develop_start_command = "nohup /opt/homebrew/bin/hugo server -s ~/Mind/blogpages -e production -p 1313 -D --disableFastRender >/dev/null 2>&1 &"

"""
vim ~/.zhsrc 定义 hugo-global 命令
alias hugo-global='python3' [script_path]
"""

def is_it_running():
    status_command = "ps -ef|grep -v grep|grep hugo|awk '{print $2}'"
    
    pid = os.popen(status_command).read().strip()
    if pid:
        return 'IS RUNNING', pid
    else:
        return 'NOT RUNNING', pid
    
def start():
    status, pid = is_it_running()
    if status == "IS RUNNING":
        print(f'{Fore.RED} [+] Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)')
    elif status == "NOT RUNNING":
        os.popen(start_command).read().strip()
        print(f'{Fore.GREEN} [+] Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)')

def stop():
    status, pid = is_it_running()
    
    if status == "IS RUNNING":
        os.popen(stop_command).read().strip()
        print(f'{Fore.GREEN} [-] Web Server is stopping')
    elif status == "NOT RUNNING":
        os.popen(stop_command).read().strip()
        print(f'{Fore.RED} [-] Web Server is stopping')
        
def status():
    status, pid = is_it_running()  # 查看运行状态并保存到 status 变量, 结果有 IS RUNNING / NOT RUNNING

    if status == "IS RUNNING":
        print(f'{Fore.GREEN} [+] Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)')
    elif status == "NOT RUNNING":
        print(f'{Fore.RED} [-] Web Server is stopping')
        
def restart():
    status, pid = is_it_running()  # 查看运行状态并保存到 status 变量, 结果有 IS RUNNING / NOT RUNNING
    if status == "IS RUNNING":
        os.popen(stop_command).read().strip()
        os.popen(start_command).read().strip()
        print(f'{Fore.GREEN} [-] Web Server is stopping')
        print(f'{Fore.GREEN} [+] Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)')
    elif status == "NOT RUNNING":
        os.popen(start_command).read().strip()
        print(f'{Fore.GREEN} [+] Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)')
        
def develop():
    print(f'{Fore.BLUE} [!] Run in developer mode')
    print(f'{Fore.BLUE} [!] http://localhost:1313/')
    os.popen(stop_command).read().strip()
    os.popen(develop_start_command).read().strip()

def services(action):
    if action == 'status':
        status()
    elif action == 'start':
        start()
    elif action == 'stop':
        stop()
    elif action == 'restart':
        restart()
    elif action == 'develop':
        develop()
    else:
        print(f'你要不再看看你输入的是啥? {action}')
            
if __name__ == '__main__':
    fire.Fire(services)
