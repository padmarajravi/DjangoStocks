from background_task import background
from util import downloader

@background(schedule=60*24)
def daily_download():
    downloader.Downloader.download()