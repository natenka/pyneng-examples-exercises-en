# -*- coding: utf-8 -*-

    return datetime.datetime.strftime(datetime_obj, "%d/%m/%Y %H:%M")


def write_last_log_to_csv(source_log, output):
    with open(source_log) as f:
        data = list(csv.reader(f))
        header = data[0]
    result = {}
    sorted_by_date = sorted(
        data[1:], key=lambda x: convert_str_to_datetime(x[2])
    )
    for name, email, date in sorted_by_date:
        result[email] = (name, email, date)
    with open(output, "w") as dest:
        writer = csv.writer(dest)
        writer.writerow(header)
        for row in result.values():
            writer.writerow(row)


if __name__ == "__main__":
    write_last_log_to_csv("mail_log.csv", "example_result.csv")
