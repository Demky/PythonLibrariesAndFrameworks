# :bowtie: official Github :
https://github.com/rajatomar788/pywebcopy

<br>

Don't forget to install webcopy in your python env :
    
    pip install pywebcopy

Two scripts availlable :
- Download a website page
- Download the entire website

#### :warning: if you got an error : Exception has occurred: pywebcopy.exceptions.AccessError

that mean the webpage does not permit you to scrap the webpage.
**You can bypass that** by adding one more argument to the save_webpage call :


link to the issue : https://github.com/rajatomar788/pywebcopy/issues/1

_exemple :_

    save_webpage(
      url='https://www.grafikart.fr/demo/JS/GSAP/index.html',
      project_folder='D:/Users/demky/Pictures/test',
      bypass_robots=True
)