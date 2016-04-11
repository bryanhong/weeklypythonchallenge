# qrcode.py

import csv
import urllib

vcard_template = '''
BEGIN:VCARD
VERSION:4.0
N:%s;%s;;;
FN:%s
ORG:Sunmead Raisin Corp
TITLE:%s
TEL;TYPE=work,voice;VALUE=uri:tel:%s
ADR;TYPE=work;LABEL="125 Tasman, San Jose, CA 95134"
EMAIL:%s
REV:20160405T103923Z
END:VCARD
'''

root_url = 'https://chart.googleapis.com/chart?'

def make_vcard(firstname, lastname, title, email='', phone=''):
    'creates a vcard with the suppplied information'
    fullname = firstname + ' ' + lastname
    return vcard_template % (lastname, firstname, fullname, title, phone, email)

def create_qrcode(text):
    'creates a QR-code from the text using the Google Chart API'
    query = {'cht': 'qr',
             'chs': '300x300',
             'chl': vcard}
    url = root_url + urllib.urlencode(query)
    u = urllib.urlopen(url)
    return u.read()

filename = 'notes/raisin_team.csv'
with open(filename) as f:
    for lastname, firstname, title, email, phone in csv.reader(f):
        vcard = make_vcard(firstname, lastname, title, email, phone)

        vcard_filename = 'notes/%s_%s' % (firstname, lastname)
        with open(vcard_filename, 'w') as vcard_file:
            vcard_file.write(vcard)

        qrcode = create_qrcode(vcard)
        qrcode_filename = 'notes/%s_%s.png' % (firstname, lastname)
        with open(qrcode_filename, 'wb') as qrcode_file:
            qrcode_file.write(qrcode)
