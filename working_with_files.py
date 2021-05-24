#Exercise 1 - Reading Text
with open("welcome.txt") as text_file:
  text_data = text_file.read()

print(text_data)

#Exercise 2 - Reading the lines within the text
with open("how_many_lines.txt") as lines_doc:
  for lines in lines_doc:
    print(lines)

#Exercise 3 - Reading the first line of the document
with open("just_the_first.txt") as first_line_doc:
  first_line = first_line_doc.readline()

print(first_line)

#Exercise 4 - Writing to a document
with open("bad_bands.txt", "w") as bad_bands_doc:
  bad_bands_doc.write("Muse") #(Please don't judge me for not liking Muse)

  print(bad_bands_doc)

#Exercise 5 - Appending information onto an existing document
with open("cool_dogs.txt", "a") as cool_dogs_file:
  cool_dogs_file.write("Air Buddy")

#Exercise 6 - <with> commands automatically close the document once the block of code is exited.
with open("fun_file.txt") as close_this_file:

  setup = close_this_file.readline()
  punchline = close_this_file.readline()

print(setup)
print(punchline)

#Exercise 7 - Opeining and reading CSV (Comma Seperated Values) files
with open("logger.csv") as log_csv_file:
  print(log_csv_file.read())

#Exercise 8 - Converting a CSV file into a dictionary using the code below.
import csv

with open("cool_csv.csv") as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for row in cool_csv_dict:
    print(row["Cool Fact"])

#Exercise 9 - Use a <delimiter> to split up sentences with "@" between them, creating a space.
import csv

with open("books.csv") as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter = "@")
  isbn_list = [books["ISBN"] for books in books_reader]


#Exercise 10 - Converting dictionaries into a CSV file with a header of the field above, and the information seperated
#by commas.
access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'},
              {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'},
              {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'},
              {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'},
              {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'},
              {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'},
              {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'},
              {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'},
              {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'},
              {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

import csv

with open("logger.csv", "w") as logger_csv:
  log_writer = csv.DictWriter(logger_csv, fieldnames=fields)

  log_writer.writeheader()
  for item in access_log:
    log_writer.writerow(item)

#Exercise 11 - Reading from a JSON file
import json

with open("message.json") as message_json:
  message = json.load(message_json)

print(message["text"])

#Exercise 12 - Writing to a JSON file
data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

import json

with open("data.json", "w") as data_json:
  json.dump(data_payload, data_json)

#Exercise 13
