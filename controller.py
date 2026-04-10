import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None

    def handleSpellCheck(self,e):
        frase_scritta = self._view.txtIn.value
        lingua_scelta = self._view.ddLanguage.value
        modalita_scelta = self._view.ddModality.value

        if frase_scritta == "":
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text("Add a sentence"))
            return

        if lingua_scelta == "":
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text("Select a language"))
            return

        if modalita_scelta == "":
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text("Select a modality"))
            return

        parole,tempo = self.handleSentence(frase_scritta,lingua_scelta,modalita_scelta)

        self._view.txtOut.controls.clear()
        self._view.txtOut.controls.append(ft.Text("Sentence: " + frase_scritta))
        self._view.txtOut.controls.append(ft.Text("Wrong word/s: " + parole))
        self._view.txtOut.controls.append(ft.Text("Time: " + str(tempo)))

        self._view.update()



    def handleLanguageSelection(self,e):
        lingua_scelta = self._view.ddLanguage.value
        self._view.txtOut.controls.append(ft.Text("Selected Language: " + lingua_scelta))
        self._view.update()

    def handleModalitySelection(self,e):
        modalita_scelta = self._view.ddModality.value
        self._view.txtOut.controls.append(ft.Text("Selected Modality : " + modalita_scelta))
        self._view.update()


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text