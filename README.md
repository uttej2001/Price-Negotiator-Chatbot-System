# Negotiation Chatbot
AI Chatbot developed through Rasa. Rasa is helpful in understanding messages, holding conversations, and connecting to messaging channels and APIs.

Commands:
1. Fork the repository
2. Open a folder where to run this chatbot(cd ..)
3. Install rasa and activate the rasa environment using "conda activate rasa" command
4. Using "rasa init" run Basic model given by rasa  
5. Through Initial Rasa Model we can customize things as much as we want and build our own chatbot.
6. Train the model using command "rasa train"
7. Run the trained model using "rasa run actions & rasa shell"
8. For deployment run this command "rasa run -m models --enable-api --cors "*" --debug" and open index.html

Note: It may take 1-2 minutes to deploy your model through index.html
