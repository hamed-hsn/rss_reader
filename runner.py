from rss.concretes import CommonRssReader
from downloader.concretes import CommonDownloader
from scraper.concretes import CommonScraper


farsnews_rss_link = 'https://www.farsnews.ir/rss'
fars_news_pattern = {'titr': '.d-block.text-justify', 'summary': '.p-2'}

if __name__ == '__main__':
    rssReader = CommonRssReader(farsnews_rss_link, CommonDownloader, CommonScraper, fars_news_pattern)
    rssReader.run()
    # now every data is stored in rssReader.data
    print(rssReader.data)