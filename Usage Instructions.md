scholar.py
==========
(1)scholar.py can fetch Bibtex of all the articles citing that article.

(2)journal_name.py can make some visualizations based on that Bibtex corpus(journals vs conferences vs others,which journals cite most,citations over time etc).

(3)Pubmed_searchkeywords.py can query Pubmed for each of the articles in the Bibtex corpus fetch various extra items not available from bibtex (currently,keywords, but later we could potentially fetch grants cited in those articles and whatever other metainfo is available).

(4) make some visualizations based on pubmed query results (initial idea is to just look at the word cloud for keywords).


Usage Instructions:
----------
(1)To fetch Bibtex of all the articles citing that article.
* get the cited number on google scholarof that article, eg  "https://scholar.google.com/scholar?oi=bibs&hl=en&cites=6675397154864859782&as_sdt=5" and the cited number is "6675397154864859782".
* input the following code in your terminal python scholar.py -c 100 -T 6675397154864859782 --citation "bt" .
  100 represents the number of article you want to get from google scholar.(if you input 100,it will get 200 results back)
  citation "bt" represents get the bibtex of every article.
* Then all the "Bibtex" information will be download into a jsaon file.

(2)To figure out what type of citations it is(journal,conference proceeding or something else) and calculate statistics for each journal title.
Run the program journal_name.py .

(3)To search the keywords of every journal, run Pubmed_searchkeywords.py. It will get the keywords on Pubmed.

Prerequisite Packages:
----------
(1)Requires [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
For example:
pip install beautifulsoup4

(2)Requires [matplotlib] (to draw the diagram of journals)
For example:
pip install matplotlib

(3)Requires [Biopython](https://marcobonzanini.com/2015/01/12/searching-pubmed-with-python/)(to parse Pubmed)
For example:
sudo pip install biopython

(4)Requires [wordcloud](https://github.com/amueller/word_cloud/)(draw the diagram of keywords)
For example:
pip install wordcloud




