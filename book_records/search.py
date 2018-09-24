# from google.appengine.api import search

# class BookSearch:
#     'to define search index'

#     def __init__(self, index_name):
#         'to create or access an index'
#         self.index = search.Index(index_name)
    
#     def set_doc(self, data):
#         'to create a document and put into index'
#         d_id = data.key.urlsafe()
#         b_title = search.TextField(name="book_title", value=data.BTitle)
#         b_desc = search.TextField(name="book_description", value=BookSearch.tokenize(data.BDesc))
#         b_pub = search.TextField(name="book_publication", value=data.BPub)
#         b_price = search.NumberField(name="book_price", value=data.BPrice)

#         list = [b_title, b_desc, b_pub, b_price]
#         # creating a Document
#         doc = search.Document(doc_id=d_id, fields = list)
#         self.index.put(doc)

#     def search_doc(self, query):
#         'to search a document from search indexes'
#         docs = self.index.search(query)
#         return docs

#     def search_doc_id(self, doc_id):
#         'to search a document by doc_id'
#         doc = self.index.get(doc_id)
#         return doc

#     @staticmethod
#     def tokenize(words = ""):
#         ''' Static method to tokenize the given string property '''
#         words = words.lower()
#         word_arr = words.split()
#         for _word in word_arr:
#             to_add = ""
#             while _word:
#                 to_add += _word[0]
#                 if len(to_add) > 2 and to_add not in word_arr:
#                     word_arr.append(to_add)
#                 _word = _word[1:]
#             word_arr = list(word_arr)
#         return ' '.join(word_arr)