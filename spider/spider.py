import re
from urllib import request


class Spider():
    url = 'https://www.huya.com/g/2793'

    root_pattern = '<span class="txt">([\s\S]*?)</span>\n</li>'
    name_pattern = '<i class="nick" title="([\s\S]*?)">'
    num_pattern = 'class="js-num">([\s\S]*?)</i></span>'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern, htmls)
        dics = []
        for html in root_html:
            name = re.findall(Spider.name_pattern, html)
            num = re.findall(Spider.num_pattern, html)
            dic = {'name': name[0], 'num': num[0]}
            dics.append(dic)
        return dics

    """ def __refine(self,dics):
        l = lambda dic: {
            'name':dic['name'][0].strip(),
            'num':dic[num][0]
        }
        return map(l,dics)
 """

    def __sort(self, dics):
        dics = sorted(dics,key=self.__sort_seed,reverse=True)
        return dics
    
    def __sort_seed(self,dics):
        r = re.findall('\d*',dics['num'])
        number = float(r[0])
        if '万' in dics['num']:
            number*=10000
        return number

    def __show(self, dics):
        rank=1
        for dic in dics:
            print(str(rank)+': '+dic['name']+' --- '+dic['num'])
            rank+=1

    def go(self):
        htmls = self.__fetch_content()
        dics = self.__analysis(htmls)
        dics = self.__sort(dics)
        self.__show(dics)


spider = Spider()
spider.go()
