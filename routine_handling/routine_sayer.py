
def handle_routine(query):
        from main import speak
        if query is None:
            return None
        common_queries = {
            ("sunday","shunday"):lambda:speak("sir, First period will be taken by Ajay sir of data mining and warehouse subject, second period will be your practical lab of Software project management by Abhishek sir, and then third period will be theory Advance Java by Sudip sir, your fourth period will be theory class of principal of management by Rakesh sir. And then enjoy sir."),
            ("monday","munday"):lambda:speak("sir, First period will be taken by Ajay sir of data mining and warehouse subject,  second period will be your practical lab of advance java by sudip sir, and then third period will be theroy of Advance Java by Sudip sir, your fourth period will be theory class of principal of management by Rakesh sir. And then enjoy sir."),
            ("tuesday","toesday"):lambda:speak("sir, all are theory sessions today.The first two periods are data mining and warehouse subject by ajay sir and software project management by abhishek sir, and then third and fourth period are the theory session of advance java by sudip sir and principle of management by rakesh sir. And then enjoy sir."),
            ("wednesday","waynasday","weinesday"):lambda:speak("sir, all are theory sessions today.The first two periods are data mining and warehouse subject by ajay sir and software project management by abhishek sir, and then third and fourth period are the theory session of advance java by sudip sir and principle of management by rakesh sir. And then enjoy sir."),
            ("thursday","tustday"):lambda:speak("sir, First period will be your practical lab by abhishek sir of software project management subject, second period is theory session by abhishek sir, and then third period will also be your theory of data mining and warehouse subject by ajay sir, your fourth period is again theory class of principle of management by rakesh sir. And then enjoy sir."),
            ("friday","frayday"):lambda:speak("sir, First period will be you lab by ajay sir of data mining and warehouse subject, second period will be your theory of software project management by abhishek sir, and then third period will be your lab of advance java by sudip sir, last period will be of principle of management by rakesh sir. And then enjoy sir."),
            "saturday":lambda:speak("I think you need to remember about the tutions, or futsall program anywhere and if not then enjoy sir"),
        }
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

    