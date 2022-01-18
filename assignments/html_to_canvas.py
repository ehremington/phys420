import urllib.parse as parse
import sys

infile = sys.argv[1]

def to_canvas(latex, inline = False):
    '''Converts Latex expression to canvas used <img> class.'''
    modelo = '<img class="equation_image" title="{0}" src="/equation_images/{1}" alt="Latex: {0}" data-equation-content="{0}" />' 
    out = modelo.format(latex.replace('&amp;','&'),parse.quote(parse.quote(latex.replace('&amp;','&'), safe='()'), safe='()&'))
    if not inline:
        out = '</p>' + out + '</p>'
    return out

with open(infile) as f:
    start = 0
    for line in f:
        if start == 0:
            if 'script' in line:
                start = 1
            else:
                print(line)
        elif start == 1:
            if '<body>' in line:
                print('</head>')
                start = 2
        elif start == 2:
            if '<img src=' in line:
                print(line)
            elif '$$' in line:
                chunks = line.split('$$')
                for i, ch in enumerate(chunks):
                    if i % 2 == 0:
                        print(ch)
                    else:
                        print(to_canvas(ch))
            elif '$' in line:
                chunks = line.split('$')
                for i, ch in enumerate(chunks):
                    if i % 2 == 0:
                        print(ch)
                    else:
                        print(to_canvas(ch, inline=True))
            else:
                print(line)