from brightermodays.main import main as brightermodays
import schedule
import time

schedule.every(3).hours.do(brightermodays)

if __name__ == "__main__":
    brightermodays()
    while True:
        schedule.run_pending()
        time.sleep(1)
