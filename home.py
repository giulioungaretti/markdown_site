'Markdown server'

import web
import markdown
import os 
import inspect
import glob

__version__ = '0.01beta' 
__author__  = 'Giulio, Giulio.ungaretti@gmail.com' 

# define the urls of the web page

urls =  (
 #   '/^(?!index).*', 'page',  #matches the / regex to the  class index
    '/(.*)', 'index',
    )

# templates are found in the templates directory

render = web.template.render('templates')
# markdown stuff
md = markdown.Markdown(output_format='html4')


# define classes for the website

# class index:
#     '''
#     class to define the index page of my web site
#     '''
#     def GET(self):
#         return "hello Giulio "



class page:
    '''
    class to define the other pages of  my web site
    '''
    def GET(self,url):
        # Each URL maps to the corresponding .txt file in pages/
        # page_file = 'pages/%s.md' %(url)     
        print url
        # # Try to open the text file, returning a 404 upon failure


        # # Read the entire file, converting Markdown content to HTML
        # content = f.read()
        # content = md.convert(content)

        # # Render the page.html template using the converted content
        return render.page(url)

class index:
  def GET(self,url):
    home = expanduser("~")
    if url == "index": 
        all_f = [] 
        for dirname,dirpath,filez in os.walk('/home/giulio/Dropbox/Documents/'):
            for i in filez:
                if i[-3:] == '.md':
                    all_f.append([ dirname,i])
        return render.list(all_f)  
    else:
        
        file_name = url.split('/')[-1]
        folder_path = '/'.join(url.split('/')[:-1])
        total = '/'.join([folder_path,file_name])
        try:
            f = open('/'+total, 'r')
            content = f.read()
            content = md.convert(content)
        except IOError:
            return web.notfound()
        return render.page(content)



if __name__ == "__main__":
    app = web.application(urls,globals())
    app.run()