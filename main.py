from brightermodays.main import main as brightermodays
from jobsearchke.main import main as jobsearchke
from ihub.main import main as ihub
import schedule
import time
from dotenv import load_dotenv

load_dotenv()

schedule.every(3).hours.do(brightermodays)
schedule.every(3).hours.do(jobsearchke)
schedule.every(3).hours.do(ihub)

if __name__ == "__main__":
    brightermodays()
    jobsearchke()
    ihub()
    while True:
        schedule.run_pending()
        time.sleep(1)
