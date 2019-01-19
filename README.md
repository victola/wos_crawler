# Web of Science 爬虫 / Web of Science Crawler
一个导出Web of Science题录数据的爬虫，支持以下两种方式：

- 给定所需的期刊名称列表，下载列表中所有期刊上的Article类型的文献
- 给定合法的WoS高级检索式，下载检索式得到的Article类型的结果
- PS:（因为WoS本身的限制，单个检索式超过10万个结果的话，10万条后面的结果无法导出，请通过年份限定的方式修改检索式进行分别爬取）

A crawler that downloads bibliographic data from Web of Science, given:

- A list of the desired journals' names, the crawler will download all bibliographic data of the articles (DocumentType = Article) in these journals.
- Or a legal Web of Science advanced query, the crawler will download the bibliographic data of the query result.
- PS: (Due to restrictions of Web of Science, users can only export the first 100K records, so if your query returns more than 100K results, please add a time constraint on it to split your query into serval parts. eg: add "PY=(year1-year2)")

## 使用方法 / Usage

使用图形界面 / Using GUI

- 可以使用编译好的程序 / Executable program：[Wos_GUI_Crawler-v0.1-alpha](https://github.com/tomleung1996/wos_crawler/releases)

- 将`main.py`的第30行取消注释，调用`crawl_by_gui()`，然后根据指示进行操作（GUI在爬取时会发生假死情况，请耐心等待爬取结束）

- Uncomment line 30 in `main.py`, calling `crawl_by_gui()`, and follow the guide (GUI will become no response while scraping, please be patient)

给定期刊列表 / Given a list of journals' name

- 将`main.py`的第22-23行取消注释，调用`crawl_by_journal()`，传递期刊列表文件路径和输出保存路径

- Uncomment line 22-23 in `main.py`, calling `crawl_by_journal()`, passing journal list file path and output path to that function.

给定高级检索式 / Given a advanced query

- 将`main.py`的第26-27行取消注释，调用`crawl_by_query()`，传递检索式和输出保存路径

- Uncomment line 26-27 in `main.py`, calling `crawl_by_query()`, passing query and output path to that function.



## 输出格式 / Output format

输出格式为WoS导出的纯文本（全部字段，包含参考文献），默认保存于`output`文件夹。

- 如果使用的是期刊列表进行爬取，则输出文件存放的方式为每个期刊一个独立文件夹
- 如果使用的是高级检索式进行爬取，则输出文件的存放文件夹命名为爬虫启动的时间

The output format is WoS Plain Text, the same as the file you manually download from Web of Science. The files are stored in the `output` folder if not specified.

- If you run the crawler in the journal list mode, each journal will have its own folder
- If you run the crawler in the advanced query mode, the result folder will be named by current time.
