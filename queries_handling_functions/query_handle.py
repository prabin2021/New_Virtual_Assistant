
def handle_query(query):
        from main import speak
        if query is None:
            return None
        # query = query.lower()
        common_queries = {
            ("how are you","what is the","are you fine"):lambda:speak("I am fine sir,thank you for asking and what about you sir."),
            "fuck you bro ":lambda:speak("thank you for your complementary, same to you sir."),
            ("fuck you bharat","fuck you varat"):lambda:speak("yes sir, fuck him fast, fuck you bharat"),
            "who are you":lambda:speak("I am Jarwis, the virtual assistant of Mr. Prabin."),
            "what can you do":lambda:speak("I can perform several tasks like opening youtube,search anything on youtube , google, opening camera, typing, cursor controllingby your eyes or hands , and many more, what do you want me to do?"),
            ("i am bored","bored","feeling bored"):lambda:speak("Ok sir, What can I do for you then? Would you like to watch any videos in youtube?"),
            ("hey jarvis","hi jarvis"):lambda:speak("Yes sir,any command for me?"),
            "chandrama":lambda:speak("Oh, yeah sir, she is your wife. You have married the beautiful girl sir."),
            "bijan":lambda:speak("Oh, yeah I know him sir. He is your student. He feels bored while studying but he loves to play football. You should train him well."),
            "sahil":lambda:speak("Oh, yeah I know him sir. He is your student. He is in A level now. You should train him well."),
            "roshan":lambda:speak("Oh, yeah I got it. The few days ago you checked his bag when you lost your phone. He is really a silly guy sir."),
            ("assam","yasam"):lambda:speak("Oh, yeah I got it. He used to offer you bhola sir."),
            ("hari","hari","sigdel"):lambda:speak("Oh, yeah I got it. He is your dad sir."),
            ("deepa","dipa"):lambda:speak("Yes sir, she is your mom."),
            ("sansar","sanchar"):lambda:speak("Oh, yeah I got it. You saved his contact number as hancy hero sir."),
            ("saughat","saugat","sugat"):lambda:speak("Oh, yeah I got it sir.He is your friend since 11 class. He has same MT 15 bike as yours."),
            ("anurag","anuragh"):lambda:speak("Oh, yeah I got it sir. Your silly friend. He always argue with saugat."),
            "ishan":lambda:speak("Oh, yeah I got it. He always seems to come with you while going to college."),
            "hemanta":lambda:speak("Oh, yeah I know him sir, he is principal of Genius school and I think he is pro in smoking."),
            "nikesh":lambda:speak("Yes, of course sir, last time he became famous when he got drunk, he messed up with Abhishek sir too. His profile is in Alpha male group."),
            "sumit":lambda:speak("Oh, yeah I know him sir, he is coordinator of Genius school and I think he loves to dance when he is drunk."),
            "abhishek":lambda:speak("Oh, yes I know him sir, he always uses the word 'muji' when he is drunk, he needs to eat a lot at a single time."),
            "puran":lambda:speak("Oh, yeah I know him sir, he is a sports teacher, he plays basketball well."),
            "rupes":lambda:speak("Oh, yeah I know him sir, he is an accountant in Genius school, he always shakes hands with you when he meets with you."),
            "kevin":lambda:speak("Oh, yeah I know him sir, he is your student, he is currently in A level"),
            ("kevin hero"):lambda:speak("kevin is hero sir"),
            ("same here","i am also fine","i am also good","i am good too","i am fine too"):lambda:speak("That's nice to hear sir.")
            
            
        }
        # query_lower = query.lower()
        # for key, response in common_queries.items():
        #     if key == query_lower:  # Check for exact match
        #         response()
        #         return  # Stop processing further queries
        #     elif isinstance(key, tuple) or query_lower in key:  # Check for partial match within tuple
        #         response()
        #         return  # Stop processing further queries
        # return None
        query_lower = query.lower()
        for key, response in common_queries.items():
            if isinstance(key, tuple):
                for k in key:
                    if k in query_lower:
                        response()
                        break
            else:
                if key in query_lower:
                    response()
        
        return response
