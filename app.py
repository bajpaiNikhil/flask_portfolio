from flask import Flask,render_template,send_file,request
from chatbot import chatbot
app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/Resume.pdf')
def Resume():
    p="Resume.pdf"
    return send_file(p,as_attachment=True)

# @app.route("/")
# def get_bot_response():
#     return render_template("MoreAboutMe.html")
#
# @app.route("/get")
# def getbotresponse():
#     userText = request.args.get('msg')
#     return str(chatbot.get_response(userText))



if __name__=="__main__":
    app.run(debug=True)



