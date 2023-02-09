from flask import Flask,request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app=Flask(__name__)

#here flask will create a local server
@app.route('/bot',methods=['POST'])
def bot():
    #this is the user msg,here userMsg will be stored
    userMsg=request.values.get('Body',' ').lower()
    #to integrate through twilio
    botResponse=MessagingResponse()
    #initializing the chatbot
    msg=botResponse.message()
    if 'hello' in userMsg:
        msg.body("Hi there!,How may i help you?")
    elif 'machine learning' in userMsg:
        msg.body("Machine learning (ML) is a type of artificial intelligence (AI) that allows software applications to become more accurate at predicting outcomes without being explicitly programmed to do so. Machine learning algorithms use historical data as input to predict new output values.")
        msg.body("You can learn MAchine Learning from https://www.javatpoint.com/machine-learning")
    elif 'certificates' in userMsg:
        if 'great learning' in userMsg:
            msg.body('https://olympus1.mygreatlearning.com/course_certificate/YYMRUDVF')
        elif ' c ' in userMsg:
            msg.body('https://www.sololearn.com/certificates/course/en/21777850/1089/landscape/png')
        elif 'data science' in userMsg:
            msg.body('https://www.sololearn.com/certificates/course/en/21777850/1161/landscape/png')
        elif "data structure" in userMsg:
            msg.body('https://www.sololearn.com/certificates/course/en/21777850/1159/landscape/png')
        elif 'intermediate python' in userMsg:
            msg.body('https://www.sololearn.com/certificates/course/en/21777850/1158/landscape/png')
        elif 'python core' in userMsg:
            msg.body('https://www.sololearn.com/certificates/course/en/21777850/1073/landscape/png')
        elif 'html' in userMsg:
            msg.body('https://www.sololearn.com/certificates/course/en/21777850/1014/landscape/png')
        elif 'cpp' in userMsg:
            msg.body('https://www.sololearn.com/certificates/course/en/21777850/1051/landscape/png')
    elif 'flask' in userMsg:
        msg.body('Flask is a web application framework written in Python. It was developed by Armin Ronacher, who led a team of international Python enthusiasts called Poocco.')
        msg.body("You can have complete details of Flask in https://www.google.com/search?q=flask&oq=flask&aqs=chrome..69i57j35i39l2j0i67j0i67i433l2j46i67j0i67j0i67i433l2.9040j0j15&sourceid=chrome&ie=UTF-8")
    elif 'bot' in userMsg:
        msg.body('A WhatsApp chatbot (WhatsApp bot) is a computer program designed to automatically answer customer questions about your products and services, share content, and send notifications regarding orders, payments, shipping on WhatsApp.')
        msg.body('https://www.freshworks.com/live-chat-software/customer-engagement/build-a-whatsapp-bot-blog/#:~:text=A%20WhatsApp%20chatbot%20(WhatsApp%20bot,%2C%20payments%2C%20shipping%20on%20WhatsApp.')
    elif 'quote' in userMsg:
        r=requests.get('https://api.quotable.io/random')
        #here 200 means the request is successful
        if r.status_code==200:
            data=r.json()
            quote=f'{data["content"]} ({data["author"]})'
        else:
            quote="I couldn't retrieve a quote at this moment,sorry"
        msg.body(quote)
    elif 'cat' in userMsg:
        msg.media('https://cataas.com/cat')  
    elif 'bored' in userMsg:
        msg.body("Come let's chat for a while")
    elif 'thankyou' in userMsg:
        msg.body('Welcome Dear')
    elif 'github' in userMsg:
        msg.body('https://github.com/Teju-Namala')
    elif 'linkedin' in userMsg:
        msg.body('https://www.linkedin.com/in/namala-tejaswini-a18b0b236/')
    elif 'instagram' in userMsg:
        msg.body('https://www.instagram.com/_teju_731_/')
    elif 'codechef' in userMsg:
        msg.body('https://www.codechef.com/')
    else:
        msg.body("Sorry,I didn't get what you have said!")
    return str(botResponse)

if __name__ == '__main__':
    app.run(debug=True)


