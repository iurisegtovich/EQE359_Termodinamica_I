'''usage:
once:
import python_tutor_magic
target cells, on the first line as usual:
%%pythontutor
this will generate a url for python tutor wuth the current cell code
this will only convert the code to url, this will not try to run the code in the current kernel'''

from IPython.core.magic import (Magics, magics_class, line_magic, cell_magic, line_cell_magic)
from IPython.display import display, HTML

@magics_class
class pythontutor(Magics):
    
    @cell_magic
    def pythontutor(self, line, cell):
        "cell magic to encode curent cell code to python tutor url"
        print("Encoding the current cell code into a python tutor url...")
        link_t = "<a href='{href}'>Your URL is ready: click to try this code on python tutor [ . > ]</a>"
        tutor_url=genPythonTutorLink(cell)
        html = HTML(link_t.format(href=tutor_url))
        # display the HTML object to put the link on the page:
        display(html)
        return

#backendish functions
def genPythonTutorLink(code):
    import urllib
    base="http://pythontutor.com/live.html#code="
    qcode=urllib.parse.quote(code)
    return base+qcode

#unittestish functions
def test_genPythonTutorLink():
    cases=["x=1"]
    result=[]
    for case in cases:
        result.append(genPythonTutorLink(case))
    return result

# register to make the module have effect in the notebook
ip = get_ipython()
ip.register_magics(pythontutor)

#references 

# 1. http://pythontutor.com/
# 2. https://ipython.org/ipython-doc/3/config/custommagics.html
# 3. https://stackoverflow.com/questions/34986646/how-to-insert-a-variable-in-href-link-in-ipython-markup