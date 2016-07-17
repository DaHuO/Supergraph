import scrapy
from scrapy.selector import Selector

class GithubSpider(scrapy.Spider):
	name = "Github"
	allowed_domains = ["github.com"]

	start_urls = ["https://github.com/search?l=Python&q=sorting&type=Repositories"]

	def parse(self, response):
		sel = Selector(response)

		item_urls = []
		for request in self.find_items_from_list_page(sel, item_urls):
			yield request

		list_urls = []
		for request in self.find_nexts_from_list_page(sel, list_urls):
			yield request

	def find_items_from_list_page(self, sel, item_urls):
		items_xpath = '//h3[@class="repo-list-name"]//@href'
		item_nodes = sel.xpath(items_xpath).extract()
		base = "https://github.com"
		for path in item_nodes:
			item_url = base + path
			item_urls.append(item_url)
			# requests.append(scrapy.Request(item_url, call_back = self.parse_item))
		print (item_urls)
		return item_urls

	def find_nexts_from_list_page(self, sel, list_urls):
		nexts_xpath = '//a[@class="next_page"]//@href'
		nexts = sel.xpath(nexts_xpath).extract()
		requests = []
		base = "https://github.com"
		for path in nexts:
			list_url = base + path
			list_urls.append(list_url)
			requests.append(scrapy.Request(list_url, callbase = self.parse))
		return requests



