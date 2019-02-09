rm -rf category_url.json
rm -rf books_url.json
scrapy runspider spider/spiders/category_url.py -o category_url.json -s FEED_EXPORT_ENCODING="utf-8"
scrapy runspider spider/spiders/dangdang.py -o books_url.json -s FEED_EXPORT_ENCODING="utf-8"