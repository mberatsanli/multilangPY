'''
    @date 30/09/2019
    @author Melih Berat SANLI
'''
import os, json

class multilang:
    lang = "tr"
    directory = "multilang/languages/"
    data = ()

    def __init__(self):
        self.loadLangFile()

    def loadLangFile(self):
        jsonPATH = self.directory + self.lang + '.json'
        if os.path.exists(jsonPATH):
            if os.access(jsonPATH, os.R_OK):
                with open(self.directory + self.lang + '.json') as jsonFile:
                    self.data = json.load(jsonFile)
            else:
                print("multilangPY: ERROR! THE FILE IS NOT READABLE!") 
                exit()
        else:
            print("multilangPY: ERROR! NOT FOUND FILE!")
            exit()
  
    def set(self, type, value):
        if type in ["lang", "language"]:
            self.lang = value
            self.loadLangFile()
        elif type in ["directory", "dir"]:
            self.directory = value
            self.loadLangFile()

    def get(self, callName):
        if self.data[callName]:
            return self.data[callName]
        else:
            return "multilangPY: ERROR! NOT FOUND TEXT/WORD!"
            exit()
    
    def languages(self, print4me = False, helper = False):
        onlyfiles = [f for f in os.listdir(self.directory) if os.path.isfile(os.path.join(self.directory, f)) and ".json" in f]
        if print4me:
            if helper:
                print "-" * 50
                print("multilangPY: We found %s json %s in directory (%s) " % (len(onlyfiles), ("files" if len(onlyfiles) > 1  else "file" ),self.directory))
                for fileLang in onlyfiles:
                    print ("> %s (Selected)" if fileLang == self.lang+".json" else "  %s") % fileLang
                print "-" * 50
            else:
                print(onlyfiles)
        else:
            if helper:
                print("multilangPY: DANGER! helper PARAMETER IS USED ONLY WITH print4me \n")
            return onlyfiles

    def whatIs(self, value, print4me = False):
        if value in ["lang", "language"]:
            if print4me: print("multilangPY: Your current language is %s" % self.lang)
            else: return self.lang
        elif value in ["directory", "dir"]:
            if print4me: print("multilangPY: Your current directory is %s" % self.directory)
            else: return self.directory
        else:
            if print4me: print("multilangPY: What do you want brooo, '%s' is not defined in multilangPY" % value)
            else: return "multilangPY: NOT FOUND! >> whatIs(%s)" % value
