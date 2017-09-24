import pickle
import re

# stems the words and performs email-specific modifications
def processText(str):
        newString = str.lower()
        newString = newString.replace("s ", " ")
        newString = newString.replace("es ", " ")
        newString = newString.replace("know ", " ")
        newString = newString.replace("email", " ")
        newString = newString.replace("http", " ")
        newString = newString.replace("subject", " ")
        newString = newString.replace("message", " ")
        newString = newString.replace("recipient", " ")
        newString = newString.replace("recipients", " ")
        newString = newString.replace("pm", " ")
        newString = newString.replace("pmto", " ")
        newString = newString.replace("www", " ")
        newString = newString.replace(".gov", " ")
        newString = newString.replace("send", " ")
        newString = newString.replace("sent", " ")
        newString = newString.replace("original", " ")
        newString = newString.replace(".com", " ")
        newString = newString.replace(".net", " ")
        newString = newString.replace(".edu", " ")
        newString = newString.replace("filename", " ")
        newString = newString.replace("attached", " ")
        newString = newString.replace(".org", " ")
        newString = newString.replace(".org", " ")
        newString = newString.replace(".ou", " ")
        newString = newString.replace(".cn", " ")
        newString = newString.replace(".et", " ")
        newString = newString.replace("enron", " ")
        newString = newString.replace("ed ", " ")
        newString = newString.replace("ing ", " ")
        newString = newString.replace("ies ", " ")
        newString = newString.replace("e ", " ")
        newString = newString.replace("ies ", " ")
        newString = newString.replace("y ", " ")
    
        return newString


pairList = pickle.load(open("pairList", 'rb'))

# extracts only alphabetical words from the data
r = re.compile('[A-Za-z][A-Za-z]+')
wordX = [r.findall(processText(x[2])) for x in pairList]

wordX = [' '.join(y) for y in wordX]
pickle.dump(wordX, open("pairX", 'wb'))