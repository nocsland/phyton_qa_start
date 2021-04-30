import csv
import json

users_json = []
with open('users.json', 'r') as f_json:
    j = f_json.read()
    users_dict = json.loads(j)

    for user in users_dict:
        users_json.append({key: value for key, value in user.items() if key in ['name', 'gender', 'address']})

books_csv = []
with open('books.csv') as f_csv:
    books_dict = csv.DictReader(f_csv)

    for book in books_dict:
        books_csv.append(
            {'books': [{key: value for key, value in book.items() if key in ['Title', 'Author', 'Height']}]})

result = []
for user_result, book_result in zip(users_json, books_csv):
    user_result.update(book_result)
    result.append(user_result)

with open('result.json', 'w') as result_f:
    result_f.write(json.dumps(result))
