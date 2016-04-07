#!/usr/bin/env python

import urllib.request
import re

def main():
    year = input('Enter year: ')
    month = input('Enter month (01-12): ')
    vol = int(year) - 1969

    #http://66.170.18.227/mcb/vol-47-2016/MCB%202016-02.html
    url = ('http://66.170.18.227/mcb/vol-' + str(vol) + '-' + year + '/MCB%20' + 
          year + '-' + month + '.html')

    urllib.request.urlretrieve(url, 'webpage.txt')

    file = open('webpage.txt', 'r', encoding='utf-8')
    subjectFile = open('MCB_subject_' + year + month + '.txt', 'w',
                       encoding='utf-8')
    changesFile = open('MCB_changes_' + year + month + '.txt', 'w',
                       encoding='utf-8')
    deletesFile = open('MCB_deletes_' + year + month + '.txt', 'w',
                       encoding='utf-8')

    fileStr = file.read().replace(u'\xa0', ' ').replace('&nbsp;', ' ')
    fileStr = fileStr.replace(u'\u266d', ' ').replace(u'\u266f', ' ')#flat,sharp
    pList = re.split(r'<p>(.*?)</?p>', fileStr, flags=re.S)

    for a in pList:
        #subject LCCNs: prefix sh, sj, gf, or pp; followed by 10 digits
        if (('[sh' in a) or ('[sj' in a) or ('[gf' in a) or ('[pp' in a)):
            subjList = re.split(r'(\[.*?\])', a, flags=re.S)
            for x in subjList:
                if (('[sh' in x) or ('[sj' in x) or ('[gf' in x) or
                    ('[pp' in x)):
                    subjectFile.write(re.sub(r'^.*\[((sh|sj|gf|pp)[ 0-9][0-9]+)'
                                             '.*$', '\g<1>\n', x))

        if 'removed from undifferentiated record' in a:
            changesFile.write(re.sub(r'^.*?(n[ brso][ 0-9][0-9]+).*\((n[ brso]'
                                     '[ 0-9][0-9]+)?.*$', '\g<1>\n\g<2>\n', a,
                                     flags=re.S))
            
        elif (('deleted and added as a reference to' in a) or (('deleted' in a)
              and ('changed' in a))):
            if re.match(r'^.*?\((n[ brso][ 0-9][0-9]+).*deleted.*', a,
                        flags=re.S) is not None:
                deletesFile.write(re.sub(r'^.*?\((n[ brso][ 0-9][0-9]+).*'
                                         'deleted.*$', '\g<1>\n', a,
                                         flags=re.S))
            if re.match(r'^.*deleted.*\((n[ brso][ 0-9][0-9]+).*', a,
                        flags=re.S) is not None:
                changesFile.write(re.sub(r'^.*deleted.*\((n[ brso][ 0-9][0-9]+)'
                                         '.*$', '\g<1>\n', a, flags=re.S))            
            
        elif 'deleted' in a:
        #'deleted; represented by authorized access point'
        #'deleted; duplicated already existing authorized access point'
        #'deleted ... not needed'
            deletesFile.write(re.sub(r'^.*?\((n[ brso][ 0-9][0-9]+).*\(?(n'
                                     '[ brso][ 0-9][0-9]+)?.*$', '\g<1>\n', a,
                                     flags=re.S))
            
        elif 'to<br>' in a or 'To<br>' in a:
            changesFile.write(re.sub(r'^.*\((n[ brso][ 0-9][0-9]+).*$',
                                     '\g<1>\n', a, flags=re.S))

    subjectFile.close()                                     
    changesFile.close()
    deletesFile.close()

if __name__ == "__main__":
    main()
