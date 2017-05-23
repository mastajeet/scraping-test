import scrapy
import regex as re
SEARCH_RESULTS_TEXT = "Search results"
INFORMATION_HEADER = ['Products','Industry']


class WikiSpider(scrapy.Spider):
    name = "quotes"


    def start_requests(self):
        url = 'https://en.wikipedia.org/w/index.php?search='
        company_name = getattr(self, 'cname').replace(' ','+')

        if company_name is not None:
            url = url  + company_name + '+(company)'
        yield scrapy.Request(url, self.parse)

    def parse(self, response):

        if self.is_search_page(response):
            url = self.obtain_first_search_result(response)
            yield response.follow(url, callback=self.parse)
        else:
            yield self.obtain_content(response)


    def is_search_page(self,response):
        heading = response.css('h1.firstHeading::text').extract_first()
        self.log(heading);
        if heading == SEARCH_RESULTS_TEXT:
            return True
        else:
            return False

    def obtain_content(self,response):
        # sel = scrapy.Selector(response)
        name = response.css('h1.firstHeading::text').extract_first()
        information = {'name':name}
        first_infobox_table = response.xpath('//table[@class="infobox vcard"]')[0]
        for tr in first_infobox_table.css('tr'):
            header = tr.xpath('th//text()').extract_first()
            if header in INFORMATION_HEADER:

                content = self.obtain_cell_content(tr)
                self.log(header+ " : "+content)
                information[header] = content

        return information


    def obtain_first_search_result(self,response):
        url = response.css('ul.mw-search-results div.mw-search-result-heading a::attr(href)').extract()[0]
        self.log(url)
        return response.css('ul.mw-search-results div.mw-search-result-heading a::attr(href)').extract()[0]

    def obtain_cell_content(self,selector):
        content = ""

        #obtain text
        content = content + selector.xpath('td//text()').extract_first() + ", "

        if not self.contains_real_letters(content):
            content = "";

        self.log("apres reset si non alpha : " + content)


        #Obtain list
        inner_list = selector.css('ul')
        if inner_list != []:
            list_items = inner_list.css('li::text').extract()
            for li in list_items:
                content = content + li + ", "

        if len(content) > 1:
            content = content[:-2]

        return content

    def contains_real_letters(self,string):
        return re.search('[a-zA-Z]', string)