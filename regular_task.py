from pprint import pprint
import re
import csv
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

num_pattern = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)' \
              r'(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)' \
              r'(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'

num_pattern_new = r'+7(\4)\8-\11-\14\15\17\18\20'
contacts_list_new = list()
for page in contacts_list:
  page_string = ','.join(page)
  format_page = re.sub(num_pattern, num_pattern_new, page_string)
  page_list = format_page.split(',')
  contacts_list_new.append(page_list)


name_pattern = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)' \
               r'(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
name_pattern_new = r'\1\3\10\4\6\9\7\8'
contacts_list = list()
for page in contacts_list_new:
  page_string = ','.join(page)
  format_page = re.sub(name_pattern, name_pattern_new, page_string)
  page_list = format_page.split(',')
  if page_list not in contacts_list:
    contacts_list.append(page_list)


for i in contacts_list:
  for j in contacts_list:
    if i[0] == j[0] and i[1] == j[1] and i is not j:
      if i[2] is '':
        i[2] = j[2]
      if i[3] is '':
        i[3] = j[3]
      if i[4] is '':
        i[4] = j[4]
      if i[5] is '':
        i[5] = j[5]
      if i[6] is '':
        i[6] = j[6]
contact_list = list()
for page in contacts_list:
  if page not in contact_list:
    contact_list.append(page)

pprint(contact_list)


with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contact_list)