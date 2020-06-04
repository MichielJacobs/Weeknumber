import schedule
import time

def refreshWeeknumber():
        print('Refresh...')

schedule.every(10).seconds.do(refreshWeeknumber)
#schedule.every().day.at("00:01").do(refreshWeeknumber)

while 1:
    schedule.run_pending()
    time.sleep(1)
