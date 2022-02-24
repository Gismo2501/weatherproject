"""

@Author: Leon Brenn
@Version: 1.0

"""

# Imports
import csv
import os
import logging
from datetime import datetime


def main():
    today = datetime.now()
    day = today.strftime("%b-%d-%Y-%H_%M")
    global nichtvorhanden
    print("### Willkommen beim Folder Renamer von Condition ###")
    # Remove print statements before release!!!!
    print("### Bitte beachten Sie, dass diese Version noch in der Alpha Phase ist! ###")
    print("### Bitte noch nicht in einer Produktivumgebung benutzen! ###")

    while True:
        # input folder destination
        input_folder = str(input("Bitte gib den Pfad der Ordner an!\n"))
        # check if folder is empty
        if input_folder == "":
            print("Der Pfad darf nicht leer sein!")
            continue
        # User check if destination is correct
        print("Ist der Pfad korrekt? \n" + '"' + input_folder + '"')
        input_correct_folder = str(input("Y für Ja | N für Nein | Andere Tasten für Abbruch\n"))

        # Switch Case of these options
        match input_correct_folder:
            case "Y":
                logging.basicConfig(filename=input_folder+"\\condition_renamer"+day+".log", encoding="utf-8", level=logging.INFO)
                logging.info("Folder Path: "+input_folder)
                print("Logging Pfad: "+input_folder+"\\condition_renamer"+day+".log")
                break
            case "y":
                logging.basicConfig(filename=input_folder+"\\condition_renamer"+day+".log", encoding="utf-8", level=logging.INFO)
                logging.info("Folder Path: " + input_folder)
                print("Logging Pfad: " + input_folder + "\\condition_renamer" + day + ".log")
                break
            case "N":
                print("#####")
            case "n":
                print("#####")
            case _:
                print("Das Programm wurde abgrebochen!")
                break

    while True:
        # Get file destination
        input_csv_file = str(input("Bitte gib den Pfad der CSV Datei an!\n"))
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
        input_correct_csv_file = str(input("Y für Ja | N für Nein | Andere Tasten für Abbruch\n"))

        # Switch Case for these options
        match input_correct_csv_file:
            case "Y":
                logging.info("CSV Path: "+input_csv_file)
                break
            case "y":
                logging.info("CSV Path: " + input_csv_file)
                break
            case "N":
                print("#####")
            case "n":
                print("#####")
            case _:
                print("Das Programm wurde abgrebochen!")
                break

    try:
        nichtvorhanden = []
        with open(input_csv_file) as csvdatei:
            csv_reader_object = csv.reader(csvdatei, delimiter=";")
            for row in csv_reader_object:
                if row.__contains__("Name"):
                    print("Header")
                else:
                    print(row[0]+" checking...")
                    logging.info(row[0]+" checking...")
                    if not os.listdir(input_folder).__contains__(row[0]):
                        print("Nicht vorhanden!")
                        logging.info(row[0] + " not available!")
                        nichtvorhanden.append(row[0])
                    else:
                        print(row[0]+" ist vorhanden!")
                        logging.info(row[0] + " found")
    except FileNotFoundError:
        print("Die Datei ist unter: " + input_csv_file + " nicht vorhanden"
                                                         "\noder der angegebene Ordner ist nicht vorhanden!"
                                                         "\nBitte starte das Programm erneut und gib den richtigen "
                                                         "Pfad an!")
        logging.error("File or Directory not found. Cancel program")
        quit()

    print("Folgende Ordner sind nicht vorhanden: ", nichtvorhanden)
    for not_available in nichtvorhanden:
        logging.info(not_available + " is not available")

    print("Möchten Sie mit der Umbennenung fortfahren?")
    input_continue = str(input("Y für Ja | N für Nein | Andere Tasten für Abbruch\n"))

    # Switch Case of these options
    match input_continue:
        case "Y":
            rename_folder(input_folder, input_csv_file)
        case "y":
            rename_folder(input_folder, input_csv_file)
        case "N":
            print("Das Programm wurde abgrebochen!")
            logging.error("Program cancelled due user interaction")
        case "n":
            print("Das Programm wurde abgrebochen!")
            logging.error("Program cancelled due user interaction")
        case _:
            print("Das Programm wurde abgrebochen!")
            logging.error("Program cancelled due user interaction")


def rename_folder(folder, csv_file):
    logging.info("Starting renaming folder...")
    try:
        with open(csv_file) as csvdatei:
            csv_reader_object = csv.reader(csvdatei, delimiter=";")
            for row in csv_reader_object:
                if row.__contains__("Name") and row.__contains__("Owner"):
                    print("Header")
                else:
                    if os.listdir(folder).__contains__(row[0]):
                        if row[0].__contains__("KUN") or row[0].__contains__("WO"):
                            if not row[0].__contains__("MO") or row[0].__contains__("mo") or row[0].__contains__("MM") or row[0].__contains__("mm") or row[0].__contains__("PD") or row[0].__contains__("pd")or row[0].__contains__("SL")or row[0].__contains__("sl")or row[0].__contains__("OR")or row[0].__contains__("or")or row[0].__contains__("DW")or row[0].__contains__("dw")or row[0].__contains__("TS")or row[0].__contains__("ts"):
                                match row[1]:
                                    case "CONDITION\\MO":
                                        name = row[1]
                                        os.rename(folder+"\\"+row[0], folder+"\\"+row[0]+"_"+name[10:])
                                        print(row[0] + " wurde in ", row[0]+"_"+name[10:], " verändert!")
                                        logging.info(row[0] + " changed to " + row[0]+"_"+name[10:])
                                    case "CONDITION\\MM":
                                        name = row[1]
                                        os.rename(folder+"\\"+row[0], folder+"\\"+row[0]+"_"+name[10:])
                                        print(row[0] + " wurde in ", row[0]+"_"+name[10:], " verändert!")
                                        logging.info(row[0] + " changed to " + row[0]+"_"+name[10:])
                                    case "CONDITION\\PD":
                                        name = row[1]
                                        os.rename(folder+"\\"+row[0], folder+"\\"+row[0]+"_"+name[10:])
                                        print(row[0] + " wurde in ", row[0]+"_"+name[10:], " verändert!")
                                        logging.info(row[0] + " changed to " + row[0]+"_"+name[10:])
                                    case "CONDITION\\SL":
                                        name = row[1]
                                        os.rename(folder+"\\"+row[0], folder+"\\"+row[0]+"_"+name[10:])
                                        print(row[0] + " wurde in ", row[0]+"_"+name[10:], " verändert!")
                                        logging.info(row[0] + " changed to " + row[0]+"_"+name[10:])
                                    case "CONDITION\\OR":
                                        name = row[1]
                                        os.rename(folder+"\\"+row[0], folder+"\\"+row[0]+"_"+name[10:])
                                        print(row[0] + " wurde in ", row[0]+"_"+name[10:], " verändert!")
                                        logging.info(row[0] + " changed to " + row[0]+"_"+name[10:])
                                    case "CONDITION\\DW":
                                        name = row[1]
                                        os.rename(folder+"\\"+row[0], folder+"\\"+row[0]+"_"+name[10:])
                                        print(row[0] + " wurde in ", row[0]+"_"+name[10:], " verändert!")
                                        logging.info(row[0] + " changed to " + row[0]+"_"+name[10:])
                                    case "CONDITION\\TS":
                                        name = row[1]
                                        os.rename(folder+"\\"+row[0], folder+"\\"+row[0]+"_"+name[10:])
                                        print(row[0] + " wurde in ", row[0]+"_"+name[10:], " verändert!")
                                        logging.info(row[0] + " changed to " + row[0]+"_"+name[10:])
                                    # lower
                                    case "CONDITION\\mo":
                                        name = row[1]
                                        os.rename(folder+"\\"+row[0], folder+"\\"+row[0]+"_"+name[10:])
                                        print(row[0] + " wurde in ", row[0]+"_"+name[10:], " verändert!")
                                        logging.info(row[0] + " changed to " + row[0]+"_"+name[10:])
                                    case "CONDITION\\mm":
                                        name = row[1]
                                        os.rename(folder+"\\"+row[0], folder+"\\"+row[0]+"_"+name[10:])
                                        print(row[0] + " wurde in ", row[0]+"_"+name[10:], " verändert!")
                                        logging.info(row[0] + " changed to " + row[0]+"_"+name[10:])
                                    case "CONDITION\\pd":
                                        name = row[1]
                                        os.rename(folder+"\\"+row[0], folder+"\\"+row[0]+"_"+name[10:])
                                        print(row[0] + " wurde in ", row[0]+"_"+name[10:], " verändert!")
                                        logging.info(row[0] + " changed to " + row[0]+"_"+name[10:])
                                    case "CONDITION\\sl":
                                        name = row[1]
                                        os.rename(folder+"\\"+row[0], folder+"\\"+row[0]+"_"+name[10:])
                                        print(row[0] + " wurde in ", row[0]+"_"+name[10:], " verändert!")
                                        logging.info(row[0] + " changed to " + row[0]+"_"+name[10:])
                                    case "CONDITION\\or":
                                        name = row[1]
                                        os.rename(folder+"\\"+row[0], folder+"\\"+row[0]+"_"+name[10:])
                                        print(row[0] + " wurde in ", row[0]+"_"+name[10:], " verändert!")
                                        logging.info(row[0] + " changed to " + row[0]+"_"+name[10:])
                                    case "CONDITION\\dw":
                                        name = row[1]
                                        os.rename(folder+"\\"+row[0], folder+"\\"+row[0]+"_"+name[10:])
                                        print(row[0] + " wurde in ", row[0]+"_"+name[10:], " verändert!")
                                        logging.info(row[0] + " changed to " + row[0]+"_"+name[10:])
                                    case "CONDITION\\ts":
                                        name = row[1]
                                        os.rename(folder+"\\"+row[0], folder+"\\"+row[0]+"_"+name[10:])
                                        print(row[0] + " wurde in ", row[0]+"_"+name[10:], " verändert!")
                                        logging.info(row[0] + " changed to " + row[0]+"_"+name[10:])
                                    case _:
                                        print(row[0]," mit Owner: "+row[1]," wurde nicht verändert!")
                                        logging.warning(row[0] + " with owner: "+row[1] + " did not change!")
                            else:
                                print(row[0], " wurde nicht verändert.")
                                logging.warning(row[0] + " did not change.")
    except FileNotFoundError:
        print("Die Datei ist unter: " + csv_file + " nicht vorhanden!"
                                                         "\nBitte starte das Programm erneut und gib den richtigen "
                                                         "Pfad an!")
        logging.error("File or directory not found. Cancel program")


# just the main method. Nothing special otter.
# Don't suspect me to do smth stupid :(
# Dragons can code | Okay i need to delete these comments


if __name__ == "__main__":
    main()
