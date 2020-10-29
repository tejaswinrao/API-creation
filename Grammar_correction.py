
import pickle
import PyPDF2  
import docx2txt
from gingerit.gingerit import GingerIt
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/result",methods=['POST'])
def result():
    
    filename = request.form['file']
    fileExtension=filename.split(".")[-1]
    name = filename.split('.')[0]

    if fileExtension=="txt":
        with open(filename,'r') as f:
            lines = f.readlines()
        corrected = []
        for line in lines:
            parser = GingerIt()
            output = parser.parse(line)
            corrected.append(output['result']) 

    if fileExtension=='pdf':
        if fileExtension =='pdf':
            pdfFileObj = open(filename, 'rb')  
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            pageObj = pdfReader.getPage(0) 
            a = pageObj.extractText()
            with open(name + '.txt','wb') as f:
                pickle.dump(a,f)
            with open(name + '.txt','r') as g:
                lines = g.readlines()
                corrected = []
                for line in lines:
                    parser = GingerIt()
                    output = parser.parse(line)
                    corrected.append(output['result']) 
               
    if fileExtension =="docx":
        content = docx2txt.process(filename)
        with open(name + '.txt','wb') as f:
            pickle.dump(content,f)
        with open(name + '.txt','r') as g:
            lines = g.readlines()
        corrected = []
        for line in lines:
            parser = GingerIt()
            output = parser.parse(line)
            corrected.append(output['result']) 
    return render_template('result.html',results = corrected)
                