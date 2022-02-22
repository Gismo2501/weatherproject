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
        # Get file destination
        input_csv_file = str(input("Bitte gib den Pfad der CSV Datei an!"))
        # check if input is empty
        if input_csv_file == "":
            print("Der Pfad darf nicht leer sein!")
            continue
        # check if input contains .csv
        if not input_csv_file.__contains__(".csv"):
            print("Bitte gib eine Datei mit der Dateiendung .csv an!")
            continue
        # User check if destination is correct
        print("Ist der Pfad korrekt? \n" + '"' + input_csv_file + '"')
        input_correct_csv_file = str(input("Y für Ja | N für Nein | Andere Tasten für Abbruch"))

        # Switch Case for these options
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
        # input folder destination
        input_folder = str(input("Bitte gib den Pfad der Ordner an!"))
        # check if folder is empty
        if input_folder == "":
            print("Der Pfad darf nicht leer sein!")
            continue
        # User check if destination is correct
        print("Ist der Pfad korrekt? \n" + '"' + input_folder + '"')
        input_correct_folder = str(input("Y für Ja | N für Nein | Andere Tasten für Abbruch"))

        # Switch Case of these options
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

# just the main method. Nothing special otter.
# Don't suspect me to do smth stupid :(
# Dragons can code | Okay i need to delete these comments


if __name__ == "__main__":
    main()


