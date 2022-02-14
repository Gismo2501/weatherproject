# Condition Ordner umbenennen

## Wofür das Programm gebraucht wird
Es müssen Ordner umbenannt werden, ahand des Ordnererstellers.
Ich muss eine CSV Datei in das Programm importieren können. Dort bekommt es die Spalten "Name","Owner"


## Anforderungen
* Wenn Name LIKE WO* ODER KUN* Dann Ordnername = Uhrsprünglicher Ordnername + _(Kürzel des Erstellers)
* Das Programm muss von mir verlangen, wo die CSV Datei zum importieren liegt
* Das Programm muss einen Pfad von mir verlangen, wo die Ordner aus der CSV liegen
* Das Progrmam muss anhand des ersten Datensatzes Prüfen, ob die Ordner überhaupt an der Stelle vorhanden sind (Gibt es den Namen aus dem obersten Datensatz der CSV wirklich am angegebenen Pafd? Ja/Fortfahren Nein/Programm mit Meldung beenden
* Am Ende sollte eine Logfile mit ausgeben werden, welche Daten alle geändert worden sind. (Dort ablegen, wo auch die Ordner zum umbennen lagen)
Beispiel: 
Ordner WO-8888 wurde von CONDITION\mo angelegt und wurde daher nach WO-8888_mo umbenannt.
Ordner KUN-9999 wurde von CONDITION\mf angelegt und wurde daher nicht umbenannt. (Ordner von mf sollen bewusst nicht umbenannt werden)

## Möglichkeiten in der Spalte Owner
1. CONDITION\mo =   MO
2. CONDITION\mm =   MM
3. PD
4. SL
5. OR
6. DW
7. TS
8. DEFAULT = NICHS ÄNDERN!
