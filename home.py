'Markdown server'

import web
import markdown
import os 
import inspect
import glob

__version__ = '0.1alpha' 
__author__  = 'Giulio, Giulio.ungaretti@gmail.com' 

# define the urls of the web page

urls =  (
    '/(.*)', 'index',  #matches the / regex to the  class index
    )

# templates are found in the templates directory

render = web.template.render('templates')
# markdown stuff
md = markdown.Markdown(output_format='html4')


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