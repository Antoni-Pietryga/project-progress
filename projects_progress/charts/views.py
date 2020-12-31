from django.http import HttpResponse
from django.shortcuts import render
from csv import reader


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def get_data_from_csv():
    with open('charts/progress_report.csv', 'r', encoding="utf8") as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)

    mapa = {}

    OTWORY, KORYTKA, LISTWY, SZAFY, KABLI, ZARABIANIE, OZNAKOWANIE, POMIARY = None, None, None, None, None, None, None, None

    for idx, col_name in enumerate(list_of_rows[0]):
        if col_name == "OTWORY":
            OTWORY = idx
        elif col_name == "KORYTKA":
            KORYTKA = idx
        elif col_name == "LISTWY":
            LISTWY = idx
        elif col_name == "SZAFY":
            SZAFY = idx
        elif col_name == "KABLI":
            KABLI = idx
        elif col_name == "ZARABIANIE":
            ZARABIANIE = idx
        elif col_name == "OZNAKOWANIE":
            OZNAKOWANIE = idx
        elif col_name == "POMIARY":
            POMIARY = idx

    data = {}

    for i in list_of_rows[1:]:
        project_name = i[0]

        if project_name not in data:
            data[project_name] = {}
            data[project_name]["OTWORY"] = [i[OTWORY]]
            data[project_name]["KORYTKA"] = [i[KORYTKA]]
            data[project_name]["LISTWY"] = [i[LISTWY]]
            data[project_name]["SZAFY"] = [i[SZAFY]]
            data[project_name]["KABLI"] = [i[KABLI]]
            data[project_name]["ZARABIANIE"] = [i[ZARABIANIE]]
            data[project_name]["OZNAKOWANIE"] = [i[OZNAKOWANIE]]
            data[project_name]["POMIARY"] = [i[POMIARY]]
        else:

            data[project_name]["OTWORY"].append(i[OTWORY]),
            data[project_name]["KORYTKA"].append(i[KORYTKA]),
            data[project_name]["LISTWY"].append(i[LISTWY]),
            data[project_name]["SZAFY"].append(i[SZAFY]),
            data[project_name]["KABLI"].append(i[KABLI]),
            data[project_name]["ZARABIANIE"].append(i[ZARABIANIE]),
            data[project_name]["OZNAKOWANIE"].append(i[OZNAKOWANIE]),
            data[project_name]["POMIARY"].append(i[POMIARY])

    return data


def indexPage(request):
    data = get_data_from_csv()

    context = {"data": data}
    return render(request, "index.html", context)



