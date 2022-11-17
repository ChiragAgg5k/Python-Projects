import getZipCode
import mainScreen

finalApi = ""

getZipCode.askZipCode()
try:
    finalApi = getZipCode.finalApi

except AttributeError:
    print("program terminated.")

if finalApi != "":
    mainScreen.showData(finalApi)
