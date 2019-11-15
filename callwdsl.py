from zeep import Client
import xml.etree.ElementTree as ET

def stemmer(s):
    stemming = Client("http://fws.cs.ui.ac.id/Stemmer/Stemmer?wsdl")
    return stemming.service.StemSentence(s)

def stopwordremove(s):
    stopword = Client("http://fws.cs.ui.ac.id/StopwordRemover/StopwordRemover?wsdl")
    return stopword.service.removeStopword(s)

def posttag(s):
    postTags = Client("http://fws.cs.ui.ac.id/RESTFulWSStanfordPOSTagger/POSTagger?wsdl")
    hasil = postTags.service.getPOSTag(s)
    xmlhsl = ET.fromstring(hasil)
    return ET.tostring(xmlhsl, encoding='utf-8', method='xml')

def kamus(s):
    cekkamus = Client("http://fws.cs.ui.ac.id/RESTKBBI/kbbi?wsdl")
    return cekkamus.service.getMean(s)
