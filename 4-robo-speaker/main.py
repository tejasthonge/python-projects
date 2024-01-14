import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 0.1 Created by Tejas Thonge")

    while True:  #to avide the rerun code
        message = input("Enter what you want to speak: ")

        if message == "q":   #to break the input from user
            engine=pyttsx3.init()
            engine.say("ram ram good by")
            engine.runAndWait()
            break
        

        #to speek we use the only following tree line but above code for the our reialiblity
        engine = pyttsx3.init()
        engine.say(message)
        engine.runAndWait()


        '''
        Discription:
        pyttsx3 is a convenient library for adding text-to-speech capabilities to your Python projects, making it useful for applications such as voice assistants, accessibility features, or any scenario where spoken output is beneficial.
         --in theis project we created robo speeker
         --we import the pyttsx3
         --say:
            this method we use for speek that we want
            theis function internaly run :
            The say function is synchronous, meaning it blocks until the speech is complete.
            To perform asynchronous speech, you can use the engine.startLoop() and engine.iterate() functions.
        '''