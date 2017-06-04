import os
import jinja2

import datetime
template = 'post.j2'

fmt_date = "%Y-%m-%d-%H%M"
date = datetime.datetime.utcnow().strftime(fmt_date)


details = { 'date': date }

PATH = os.path.dirname(os.path.abspath(__file__))
templateLoader = jinja2.FileSystemLoader((os.path.join(PATH, 'templates')),)
templateEnv = jinja2.Environment( loader=templateLoader )

template = templateEnv.get_template(template)
outputText = template.render( details )


with open('./content/' + date + '.md', "w") as myfile:
    myfile.write(outputText)