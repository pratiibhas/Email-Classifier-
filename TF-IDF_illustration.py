# import required module
from sklearn.feature_extraction.text import TfidfVectorizer

# assign documents
d0 = ' This is a camera'
d1 = 'Photograph'
d2 = 'r2j'
# merge documents into a single corpus
string = [d0, d1, d2]

# create object
tfidf = TfidfVectorizer()
# get tf-df values
result = tfidf.fit_transform(string)


# get indexing
print('\nWord indexes:')
print(tfidf.vocabulary_)

# display tf-idf values
print('\ntf-idf values:')
print(result)


''' Word indexes:
{'this': 4, 'is': 1, 'camera': 0, 'photograph': 2, 'r2j': 3}

tf-idf values:
<Compressed Sparse Row sparse matrix of dtype 'float64'
	with 5 stored elements and shape (3, 5)>
  Coords	Values
  (0, 4)	0.5773502691896257
  (0, 1)	0.5773502691896257
  (0, 0)	0.5773502691896257
  (1, 2)	1.0
  (2, 3)	1.0'''
