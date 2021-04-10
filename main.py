from brightermodays.main import main as brightermodays
from jobsearchke.main import main as jobsearchke
from ihub.main import main as ihub
from linkedin.main import main as linkedin
from found_dev.main import main as found_dev
import schedule
import time
from dotenv import load_dotenv

load_dotenv()

schedule.every(3).hours.do(brightermodays)
schedule.every(3).hours.do(jobsearchke)
schedule.every(3).hours.do(ihub)
schedule.every(3).hours.do(linkedin)
schedule.every(3).hours.do(found_dev)

if __name__ == "__main__":
    found_dev()
    time.sleep(1)
    linkedin()
    time.sleep(1)
    brightermodays()
    time.sleep(1)
    jobsearchke()
    time.sleep(1)
    ihub()
    while True:
        schedule.run_pending()
        time.sleep(1)
