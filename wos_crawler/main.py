# from gui.main_gui import *
import settings
from scrapy import cmdline
from analysis.cooccurrence.co_keyword import draw_cooccurrence_network

def crawl_by_journal(journal_list_path, output_path='../output', document_type='Article', output_format='bibtex'):
    cmdline.execute(
        r'scrapy crawl wos_journal_spider -a journal_list_path={} -a output_path={} -a output_format={}'.format(
            journal_list_path, output_path, output_format).split() + ['-a', 'document_type={}'.format(
            document_type)])


def crawl_by_query(query, output_path='../output', document_type='Article', output_format='bibtex'):
    cmdline.execute(
        r'scrapy crawl wos_advanced_query_spider -a output_path={} -a output_format={}'.format(
            output_path, output_format).split() +
        ['-a', 'query={}'.format(query), '-a', 'document_type={}'.format(document_type)])

def crawl_by_mixed_query(query, journal_list_path, output_path='../output', document_type='Article', output_format='bibtex'):
    cmdline.execute(
        r'scrapy crawl wos_mixed_query_spider -a output_path={} -a output_format={}'.format(
            output_path, output_format).split() +
        ['-a', 'query={}'.format(query), '-a', 'document_type={}'.format(document_type), '-a', 'journal_list_path={}'.format(journal_list_path)])

def crawl_by_gui():
    gui_crawler = GuiCrawler()
    gui_crawler.show()
    reactor.run()


if __name__ == '__main__':

    journal_list_path=r'..\input\journal_list.txt'
    query = 'TS=(warmth AND competence)'
    # query = 'TS=(recommendation agent)'

    # 按期刊下载
    # crawl_by_journal(journal_list_path=r'C:\Users\Tom\PycharmProjects\wos_crawler\input\journal_list_test.txt',
    #                  output_path='../output', output_format='bibtex', document_type='')

    # 按检索式下载
    # crawl_by_query(query='TS=information science AND PY=(2018)',
    #                output_path='../output', output_format='bibtex', document_type='proceedings paper')
    # crawl_by_query(query=query,
    #                output_path='../output', output_format='fieldtagged', document_type='')
    
    # 按检索和指定期刊下载
    # crawl_by_mixed_query(query=query, journal_list_path=journal_list_path,
    #                output_path='../output', output_format='fieldtagged', document_type='')

    # 使用GUI下载
    # crawl_by_gui()

    draw_cooccurrence_network(net_type='author',
                              db_path=r'../output/advanced_query/2019-03-21-22.29.05/result.db',
                              output_path=r'../output/analysis',
                              top_n=50)
    pass
