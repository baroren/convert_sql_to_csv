

def convert_sql_to_csv(file_name):

    sql_file = open(file_name, "r")
    for line in sql_file:
        values_list = []
        if "CREATE TABLE" in line:
            fields = extract_fields(sql_file, line)
            print (fields)
            print("end of table\n")
    sql_file.seek(0,0)
    for line in sql_file:
        if "INSERT INTO" in line:
            values_list = line.split("),(")
            values_list[0] = line.split("(")[1]
            values_list[-1] = values_list[-1][:-3]
            values = "".join(values_list)
            print(values)
            print("end of values\n")


def extract_fields(sql_file, line):
    line = next(sql_file)
    first_word = line.split()[0]
    field_list = []
    while first_word != ')':
        if is_field(first_word):
            field_list.append(first_word)
        line = next(sql_file)
        first_word = line.split()[0]
    fields = ','.join(field_list)
    return fields


def is_field(first_word):
    return first_word[0] == first_word[-1] == '`'


convert_sql_to_csv("demo.sql")
