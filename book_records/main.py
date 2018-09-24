import webapp2
import jinja2
from google.appengine.api import app_identity
from model import Book
import os



JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class start(webapp2.RequestHandler):
    def get(self):
        file = open('start.html')
        self.response.write(file.read())


class MainHandler(webapp2.RequestHandler):
    def get(self):
        file = open('header.html')
        self.response.write(file.read())
        file = open('addbook.html')
        self.response.write(file.read())
    
class AddBook(webapp2.RequestHandler):
    def get(self):
        bc = int(self.request.get('tfBC'))
        bt = self.request.get('tfBT')
        bp = self.request.get('tfBP')
        bpages = self.request.get('tfBPages')
        bpub = self.request.get('tfBPub')
        bdesc = self.request.get('tfBDesc')

        b1 = Book()
        b1.BCode = bc
        b1.BTitle = bt
        b1.BPrice = float(bp)
        b1.BPages = int(bpages)
        b1.BPub = bpub
        b1.BDesc = bdesc
        key = b1.put()
        self.response.write("<h3>"+str(key)+"</h3>")
        self.response.write("your response has been submitted .to add another form <a href='/form'>click here</a>")

    

class search(webapp2.RequestHandler):
    def get(self):
        file = open('header.html')
        self.response.write(file.read())
        file = open("search.html")
        self.response.write(file.read())

class viewBook(webapp2.RequestHandler):
    def get(self):
        file = open('header.html')
        self.response.write(file.read())
        book_all = Book.query()
        values = {"book_info":book_all}
        template = JINJA_ENVIRONMENT.get_template('viewbook.html')        
        html = template.render(values)
        self.response.write(html)

# class SearchBook(webapp2.RequestHandler):
#     def get(self):
#         file = open('header.html')
#         self.response.write(file.read())
#         query = self.request.get("query")
#         docs = BookSearch('book').search_doc(query)
#         self.response.write("<h3> Records Found : "+str(docs.number_found)+"</h3>")
#         self.response.write("<table border='1' cellspacing='10' cellpadding='10'>")
#         for doc in docs:
#             self.response.write("<tr>")
#             for item in doc.fields:
#                 self.response.write("<td>"+str(item.value)+"</td>")
#             self.response.write("</tr>")
#         self.response.write("</table>")

class searchByPages(webapp2.RequestHandler):
    def get(self):
        file = open('header.html')
        self.response.write(file.read())
        query = int(self.request.get("query"))
        BK = Book.query(Book.BPages <= query)
        self.response.write("<table align = 'center' border='1' cellspacing='10' cellpadding = '10'>")
        self.response.write("<tr>")
        self.response.write("<td><b>Book Code</b></td>")
        self.response.write("<td><b>Book Title</b></td>")
        self.response.write("<td><b>Book Price</b></td>")
        self.response.write("<td><b>Book Pages</b></td>")
        self.response.write("<td><b>Book Pub</b></td>")
        self.response.write("<td><b>Book Desc</b></td>")
        self.response.write("</tr>")
        for b in BK:
            self.response.write("<tr>")
            self.response.write("<td>"+str(b.BCode)+"</td>")
            self.response.write("<td>"+b.BTitle+"</td>")
            self.response.write("<td>"+str(b.BPrice)+"</td>")
            self.response.write("<td>"+str(b.BPages)+"</td>")
            self.response.write("<td>"+b.BPub+"</td>")
            self.response.write("<td>"+b.BDesc+"</td>")
            self.response.write("</tr>")
        self.response.write("</table")     
class searchByPrice(webapp2.RequestHandler):
    def get(self):
        file = open('header.html')
        self.response.write(file.read())
        query = float(self.request.get("query"))
        BK = Book.query(Book.BPrice <= query)
        self.response.write("<table border='1'align='center' cellspacing='10' cellpadding = '10'>")
        self.response.write("<tr>")
        self.response.write("<td><b>Book Code</b></td>")
        self.response.write("<td><b>Book Title</b></td>")
        self.response.write("<td><b>Book Price</b></td>")
        self.response.write("<td><b>Book Pages</b></td>")
        self.response.write("<td><b>Book Publication</b></td>")
        self.response.write("<td><b>Book Description</b></td>")
        self.response.write("</tr>")
        for b in BK:
            self.response.write("<tr>")
            self.response.write("<td>"+str(b.BCode)+"</td>")
            self.response.write("<td>"+b.BTitle+"</td>")
            self.response.write("<td>"+str(b.BPrice)+"</td>")
            self.response.write("<td>"+str(b.BPages)+"</td>")
            self.response.write("<td>"+b.BPub+"</td>")
            self.response.write("<td>"+b.BDesc+"</td>")
            self.response.write("</tr>")
        self.response.write("</table")           

class searchByTitle(webapp2.RequestHandler):
    def get(self):
        file = open('header.html')
        self.response.write(file.read())
        s = (self.request.get("query"))
        s = s.strip()
        BK = Book.query(Book.BTitle == s)
        self.response.write("<table border='1' align = 'center' cellspacing='10' cellpadding = '10'>")
        self.response.write("<tr>")
        self.response.write("<td><b>Book Code</b></td>")
        self.response.write("<td><b>Book Title</b></td>")
        self.response.write("<td><b>Book Price</b></td>")
        self.response.write("<td><b>Book Pages</b></td>")
        self.response.write("<td><b>Book Publication</b></td>")
        self.response.write("<td><b>Book Description</b></td>")
        self.response.write("</tr>")
        for b in BK:
            self.response.write("<tr>")
            self.response.write("<td>"+str(b.BCode)+"</td>")
            self.response.write("<td>"+b.BTitle+"</td>")
            self.response.write("<td>"+str(b.BPrice)+"</td>")
            self.response.write("<td>"+str(b.BPages)+"</td>")
            self.response.write("<td>"+b.BPub+"</td>")
            self.response.write("<td>"+b.BDesc+"</td>")
            self.response.write("</tr>")
        self.response.write("</table")           



app = webapp2.WSGIApplication([
    ('/form' , MainHandler),
    ('/', start),
    ('/addbook', AddBook),
    ('/search' ,search),
    ('/searchBypage', searchByPages),
    ('/searchByprice', searchByPrice),
    ('/searchBytitle', searchByTitle),
    ('/viewlist' , viewBook)
], debug=True)