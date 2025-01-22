import os
import requests
import time
import subprocess
import setproctitle

setproctitle.setproctitle("bgremove-monitor")

def is_app_alive(url):
    try:
        response = requests.get(url)
        if response.status_code == 200 and response.text == "ok":
            return True
    except requests.RequestException:
        pass
    return False

def restart_app():
    subprocess.Popen(["python", "ser.py"])

def monitor_app():
    url = "http://localhost:5000/bg?ping=true"
    check_interval = 10  # Check every 60 seconds

    while True:
        if not is_app_alive(url):
            print("App is not responding. Restarting...")
            restart_app()
        else:
            print("App is running fine.")
        time.sleep(check_interval)

if __name__ == "__main__":
    monitor_app()