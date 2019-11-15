# call-wdsl-bahasa.ui.ac.id

This file to use wdsl from bahasa.ui.ac.id

###how to using

```bash
from callwdsl import *

s ="saya makan nasi"
print(posttag(s))
```

result:
```bash
b'<document sentence="saya makan nasi">\n\t<element id="0">\n\t\t<word>saya</word>\n\t\t<postag>pr</postag>\n\t</element>\n\t<element id="1">\n\t\t<word>makan</word>\n\t\t<postag>vb</postag>\n\t</element>\n\t<element id="2">\n\t\t<word>nasi</word>\n\t\t<postag>nn</postag>\n\t</element>\n</document>'
```

###if you want to parser tag

```bash
from parserposttag import *

ss= posttag(s)
print(parsePostag(ss))
```

```bash
result:
{'saya': 'pr', ' makan': ' vb', ' nasi': ' nn'}
```