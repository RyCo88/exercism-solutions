def response(hey_bob):
    #Remove whitespace from start or end of string
    hey_bob = hey_bob.strip()

    #Check for silence
    if hey_bob == '':
        return "Fine. Be that way!"

    #Check if hey_bob is in all CAPS
    if hey_bob.isupper():
        if hey_bob[-1] == '?':
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"

    #Check if hey_bob is a question
    if hey_bob[-1] == '?':
        return "Sure."
    
    #Default response for anything else
    return "Whatever."