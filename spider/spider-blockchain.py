import re
from urllib import request

class Spider():
    url = 'https://www.blockchain.com/btc/block/000000000000000000173f2753b0c48eaa7d588a19a48dcfb4373de031b590b5'
    root_pattern = '<div id="tx-([\s\S]*?)</div></div>'
    button_pattern = 'btn btn-success cb">([\s\S]*?)</button>'
    number_pattern = '">([\s\S]*?) BTC</span>'
    sender1_pattern = '<a href="/btc/address([\s\S]*?)<span class="pull-right hidden-phone">'
    sender2_pattern = '">([\s\S]*?)</a>'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    def __analysis(self, htmls):
        trans_html = re.findall(Spider.root_pattern, htmls)
        dics = []
        i=1
        for html in trans_html:
            num1_html = re.findall(Spider.button_pattern, html)
            sender1 = re.findall(Spider.sender1_pattern, html)
            if len(sender1) == 0:
                continue
            num2_html = re.findall(Spider.number_pattern, num1_html[0])
            sender2 = re.findall(Spider.sender2_pattern, sender1[0])
            dic = {'sender': sender2[0], 'BTC num': num2_html[0]}
            dics.append(dic)
            i+=1
        return dics

    """ def __refine(self,dics):
        l = lambda dic: {
            'name':dic['name'][0].strip(),
            'num':dic[num][0]
        }
        return map(l,dics)
 """

    def __sort(self, dics):
        dics = sorted(dics,key=self.__sort_seed)
        return dics
    
    def __sort_seed(self,dics):
        number = float(dics['BTC num'])
        return number

    def __show(self, dics):
        rank=1
        for dic in dics:
            print(str(rank)+': Account: '+dic['sender']+' --- '+dic['BTC num']+' BTC')
            rank+=1

    def go(self):
        htmls = self.__fetch_content()
        dics = self.__analysis(htmls)
        dics = self.__sort(dics)
        self.__show(dics)


spider = Spider()
spider.go()
