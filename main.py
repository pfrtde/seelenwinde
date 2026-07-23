#!/usr/bin/python3

from datetime import datetime

geschi=list()

fh_head=open('tools/skel_header.html', 'r')
for line_head in fh_head:
    geschi.append(line_head)
fh_head.close()

dt = datetime.now()
iso_datum = dt.strftime("%Y-%m-%d")
geschi.append('letzte Änderung: ' + iso_datum)

geschi.append('<br>')

fh_text_liste=open('tools/text-liste.txt', 'r')
for list_item in fh_text_liste:
    list_item=list_item.strip()
    base=list_item[:len(list_item)-3]
    desc=base.replace('-', ' ')
    geschi.append('<br><h4>'+desc+'</h4>')
    fh_item=open('story/'+list_item, 'r')
    for item_line in fh_item:
        geschi.append(item_line)
    fh_item.close()
fh_text_liste.close()

fh_foot=open('tools/skel_footer.html', 'r')
for line_foot in fh_foot:
    geschi.append(line_foot)
fh_foot.close

fh_web=open('docs/index.html', 'w')
for web_line in geschi:
    fh_web.write(web_line)
fh_web.close()
