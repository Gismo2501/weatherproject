"""

@Author: Leon Brenn
@Version: 1.0

"""


def main():
    print("### Willkommen beim Folder Renamer von Condition ###")
    # Remove print statements before release!!!!
    print("### Bitte beachten Sie, dass diese Version noch in der Alpha Phase ist! ###")
    print("### Bitte noch nicht in einer Produktivumgebung benutzen! ###")

    while True:
        input_csv_file = str(input("Bitte gib den Pfad der CSV Datei an!"))
        if input_csv_file == "":
            print("Der Pfad darf nicht leer sein!")
            continue
        if not input_csv_file.__contains__(".csv"):
            print("Bitte gib eine Datei mit der Dateiendung .csv an!")
            continue
        print("Ist der Pfad korrekt? \n" + '"' + input_csv_file + '"')
        input_correct_csv_file = str(input("Y für Ja | N für Nein | Andere Tasten für Abbruch"))

        match input_correct_csv_file:
            case "Y":
                break
            case "y":
                break
            case "N":
                print("#####")
            case "n":
                print("#####")
            case _:
                print("Das Programm wurde abgrebochen!")
                break

    while True:
        input_folder = str(input("Bitte gib den Pfad der Ordner an!"))
        if input_folder == "":
            print("Der Pfad darf nicht leer sein!")
            continue
        print("Ist der Pfad korrekt? \n" + '"' + input_folder + '"')
        input_correct_folder = str(input("Y für Ja | N für Nein | Andere Tasten für Abbruch"))

        match input_correct_folder:
            case "Y":
                break
            case "y":
                break
            case "N":
                print("#####")
            case "n":
                print("#####")
            case _:
                print("Das Programm wurde abgrebochen!")
                break


if __name__ == "__main__":
    main()


