'Markdown server'

import web
import markdown
import os 

__version__ = '0.01beta' 
__author__  = 'Giulio, Giulio.ungaretti@gmail.com' 

# define the urls of the web page

urls =  (
    # '/', 'index'  #matches the / regex to the  class index
    '/(.*)', 'page',
    )

# templates are found in the templates directory

render = web.template.render('templates')
# markdown stuff
md = markdown.Markdown(output_format='html4')


# define classes for the website

class index:
    '''
    class to define the index page of my web site
    '''
    def GET(self):
        return "hello Giulio"


class page:
    '''
    class to define the other pages of  my web site
    '''
    def GET(self,url):
        if url == "" or url.endswith("/"):
            url += "index"
        print url
        # Each URL maps to the corresponding .txt file in pages/
        page_file = 'pages/%s.md' %(url)     

        # Try to open the text file, returning a 404 upon failure
        try:
            f = open(page_file, 'r')
        except IOError:
            return web.notfound()

        # Read the entire file, converting Markdown content to HTML
        content = f.read()
        content = md.convert(content)

        # Render the page.html template using the converted content
        return render.page(content)



if __name__ == "__main__":
    app = web.application(urls,globals())
    app.run()


