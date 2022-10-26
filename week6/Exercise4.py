import os
import urllib.request

def is_exit(fn):
    def wrapper(url):
        if os.path.exists(url.split('.')[1]+'.html'):
            pass
        else:
            fn(url)
    
    return wrapper

@is_exit
def download_url(url):
    html = urllib.request.urlopen(url).read()
    file_name=url.split('.')[1]
    with open(file_name+'.html','wb') as f:
        f.write(html)
    return file_name+'.html'
    

download_url('https://www.sohu.com/')
    