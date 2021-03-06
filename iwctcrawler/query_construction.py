#coding=utf-8

class QueryFactory:
    
    @staticmethod
    def mainpage_query(user_id):
        return "http://weibo.com/u/%s" % user_id 

    @staticmethod
    def info_query(page_id,pid):
        return "http://weibo.com/p/%s/info?from=page_%s&mod=TAB#place" % (page_id,pid)

    @staticmethod
    def weibo_page_num_query(page_id,page_num):
        return 'http://weibo.com/p/aj/mblog/mbloglist?id=%s&page=%s&pre_page=%s&pagebar=1' % (page_id,page_num,page_num)

    @staticmethod
    def weibo_js_query(page_id,page_num):
        page_original      = 'http://weibo.com/p/aj/mblog/mbloglist?id=%s&page=%s' % (page_id,page_num)
        page_first_toggle  = 'http://weibo.com/p/aj/mblog/mbloglist?id=%s&page=%s&pre_page=%s&pagebar=0' % (page_id,page_num,page_num)
        page_second_toggle = 'http://weibo.com/p/aj/mblog/mbloglist?id=%s&page=%s&pre_page=%s&pagebar=1' % (page_id,page_num,page_num)

        page_list = [page_original,page_first_toggle,page_second_toggle]
        return page_list

