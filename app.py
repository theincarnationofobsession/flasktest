from flask import Flask
from flask import render_template, request

app=Flask(__name__)

credential = {'admin1':'id1', 'admin2':'id2', 'admin3':'id3', 'admin4':'id4', 'admin5':'id5'}
value = 'Close'

@app.route('/',methods=["GET","POST"])
def portal_form():
  username = 'admin1'
  idv = 'id1'               # idv stands for identity verification
  if(username in credential):
    if(credential[username] == idv):
      if(value != 'Open'):
        if request.method == "POST":
          option = request.form['options']
          if(option=='Open'):
            return render_template('open.html')
          else:
            return render_template('close.html')
        else:
          return render_template("form.html")
      else:
        return render_template("open.html")
    else:
        return render_template("invalid.html")
  else:
    return render_template("invalid.html")
if __name__=='__main__':
   app.run()