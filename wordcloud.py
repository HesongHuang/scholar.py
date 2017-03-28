from os import path
from wordcloud import WordCloud

if __name__=="__main__":
	d = path.dirname(__file__)
	text = open(path.join(d, 'keywords.txt')).read()
	wordcloud = WordCloud().generate(text)
	import matplotlib.pyplot as plt
	plt.imshow(wordcloud)
	plt.axis("off")
	wordcloud = WordCloud(max_font_size=40).generate(text)
	plt.figure()
	plt.imshow(wordcloud)
	plt.axis("off")
	plt.show()
