import re


class Spider():
    root_pattern = '<span data-v-3e12421a="">85</span></li></ul></div>([\s\S]*?)<div><div class="answerCard_tit">'
    item_pattern = '<p data-v-8cf065b0="">([\s\S]*?)</p></div>  <div data-v-8cf065b0=""'
    item2_pattern = '<div class="subject_describe"><p>([\s\S]*?)</p></div>  <div class="images-wrap"'
    item3_pattern = '<div data-v-5a15039b="" class="subject_describe"><p data-v-5a15039b="">([\s\S]*?)</p></div>  <div data-v-5a15039b="" class="images-wrap"'

    def __fetch_content(self):
        r = open("1.txt", encoding='utf-8')
        htmls = r.read()
        return htmls

    def __analysis(self, htmls):
        html = re.findall(Spider.root_pattern, htmls)
        items = re.findall(Spider.item_pattern, html[0])
        items2 = re.findall(Spider.item2_pattern, html[0])
        items3 = re.findall(Spider.item3_pattern, html[0])
        dics = []
        i = 1
        for item in items:
            dic = {'num': i, 'item': item}
            i += 1
            dics.append(dic)
        for item2 in items2:
            dic = {'num': i, 'item': item2}
            i += 1
            dics.append(dic)
        for item3 in items3:
            dic = {'num': i, 'item': item3}
            i += 1
            dics.append(dic)
        return dics

    def __show(self, dics):
        for i in dics:
            print(str(i['num']) + ':' + str(i['item']))

    def go(self):
        htmls = self.__fetch_content()
        dics = self.__analysis(htmls)
        self.__show(dics)


spider = Spider()
spider.go()
