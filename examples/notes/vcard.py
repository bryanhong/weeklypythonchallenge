''' A true, old, and lurid tale of Python
    featuring pushy relatives, checkerboards,
    business cards, raisins, and getting much
    need rest.
'''

import csv
import urllib

# QR Code from the Google Chart REST API documented at
# https://developers.google.com/chart/infographics/docs/qr_codes
root_url = 'https://chart.googleapis.com/chart?'

vcard_template = '''BEGIN:VCARD
VERSION:2.1
N:%s;%s
FN:%s %s
ORG:Raisins R Us, Inc.
TITLE:%s
TEL;WORK;VOICE:%s
ADR;WORK:;;100 Flat Grape Dr;Fresno;CA;95555;United States of America
EMAIL;PREF;INTERNET:%s
REV:20150728T195243Z
END:VCARD
'''

def create_qr_code(text):
    'Use the Google Chart REST API to create a QR code from the text'
    query = {'cht': 'qr', 'chs': '300x300', 'chl': text}
    url = root_url + urllib.urlencode(query)
    u = urllib.urlopen(url)
    return u.read()

def make_vcard(fname, lname, title, phone, email=''):
    'Convert common contact info into an electronic business'
    return vcard_template % (lname, fname, fname, lname, title, phone, email)

if __name__ == '__main__':

    with open('notes/raisin_team_update.csv') as f:
        for lname, fname, title, email, phone in csv.reader(f):

            vcard = make_vcard(fname, lname, title, phone, email)
            filename = '%s_%s.vcf' % (fname, lname)
            with open(filename, 'w') as vcard_file:
                vcard_file.write(vcard)

            image = create_qr_code(vcard)
            filename = '%s_%s.png' % (fname, lname)
            with open(filename, 'wb') as image_file:
                image_file.write(image)
