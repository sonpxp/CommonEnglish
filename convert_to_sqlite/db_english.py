import json
import sqlite3


def insertVaribleIntoTable():
    try:
        conn = sqlite3.connect("../database/data_english.db")
        c = conn.cursor()

        with open("../database/data_english_phrases.json", encoding="utf-8") as json_file:
            json_data = json.load(json_file)
            json_file.close()

            create_table_phrase = """CREATE TABLE phrase (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                phrase TEXT,
                                content TEXT
                                )"""

            create_table_example = """CREATE TABLE example (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                ex TEXT,
                                mean TEXT
                                )"""

            c.execute(create_table_phrase)
            c.execute(create_table_example)

            for data in json_data:
                dict_mean = {}
                dict_item = {}

                phrase = data.get('phrase')
                mean = data.get('mean')
                example = data.get('example')

                # json_string = json.dumps(example, indent=4, ensure_ascii=False).encode('utf8')
                # print(json_string.decode())

                dict_item['mean'] = mean
                dict_item['example'] = example
                dict_mean['means'] = dict_item

                json_content = json.dumps(dict_mean, indent=4, ensure_ascii=False).encode('utf8')
                print(json_content.decode())

                # print(dict_mean)

                sql_example = "INSERT INTO example (ex,mean) values (?, ?)"
                sql_phrase = "INSERT INTO phrase (phrase, content) values (?, ?)"

                c.execute(sql_phrase, (phrase, json_content))
                for e in example:
                    en = e.get('en')
                    vi = e.get('vi')
                    # print(f"en: {en}, vi: {vi}")

                    c.execute(sql_example, (en, vi))
                    # print(sql_example)

                    conn.commit()

            # print(dict_content)
            c.close()

    except sqlite3.Error as error:
        print("Failed to insert table -->", error)

    finally:
        # conn.close()
        pass


insertVaribleIntoTable()
