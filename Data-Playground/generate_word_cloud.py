from sklearn.feature_extraction import text
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# stop_words = text.ENGLISH_STOP_WORDS
# Suggested by autocomplete in VSCode
stop_words = ['dengan', 'yang', 'untuk', 'pada', 'adalah', 'dan', 'di', 'sebagai',
              'ini', 'itu', 'karena', 'atau', 'juga', 'dari', 'ke', 'akan', 'oleh', 'saat', 'jika']

wc = WordCloud(stopwords=stop_words, background_color="white", colormap="Dark2",
               max_font_size=150, random_state=42)


with open("data.txt", "r") as data_file:
    content = data_file.read()
    # Clean data from:
    # 1. Newlines
    # 2. Punctuations
    # 3. Delimiters ("===")
    cleaned = content.replace('\n', ' ')
    cleaned = cleaned.replace(',', '')
    cleaned = cleaned.replace("===", ' ')
    cleaned = cleaned.replace('.', '')
    cleaned = cleaned.replace('!', '')
    cleaned = cleaned.replace('?', '')
    cleaned = cleaned.replace(';', '')
    cleaned = cleaned.replace(':', '')
    cleaned = cleaned.replace('"', '')
    cleaned = cleaned.replace("'", '')
    cleaned = cleaned.replace('(', '')
    cleaned = cleaned.replace(')', '')
    cleaned = cleaned.replace('-', ' ')
    cleaned = cleaned.replace('_', ' ')
    cleaned = cleaned.replace('/', ' ')
    cleaned = cleaned.replace('\\', ' ')

    # Remove conjunctions and common words
    # for stop_word in stop_words:
    #     cleaned = cleaned.replace(f' {stop_word} ', ' ')
    
    wc.generate(cleaned)

    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.title("Full data text of Pantunis")
    
plt.show()