import random
import time
import speech_recognition as sr
from sage_main import speak


# hints are to be added
def recognize_speech(recognizer, microphone):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be Recognizer` instance")
    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")
    
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)

    #setting up response object
    response={
        "success": True,
        "error": None,
        "transcription": None
    }
    try:
        response["transcription"]=recognizer.recognize_google(audio)
    except sr.RequestError:
        #in case of unresponsive API
        response["success"]=False
        response["error"]="API unavailable"
    except sr.UnknownValueError:
        response["error"]= "Unable to recognize speech"

    return response

if __name__ == "__main__":
    Options= ["bear","coconut","sunflower","chocolate","pasta","stars"]
    NumOfGuesses=3 
    PromptLimit=5

    recognizer=sr.Recognizer()
    microphone=sr.Microphone()

    word=random.choice(Options)

    instructions=(
        "I'm thinking of one of these words:\n"
        "{words}\n"
        "You have {n} number of tries to guess the word.\n"
    ).format(words=', '.join(Options), n=NumOfGuesses)

    #Instructions will be displayed and there will be a wait of 3 sec before starting the game
    print(instructions)
    time.sleep(3)

    for i in range(NumOfGuesses):
        for j in range(PromptLimit):
            print('Guess {}. Speak!'.format(i+1))
            guess= recognize_speech(recognizer,microphone)
            if guess["transcription"]:
                break
            if not guess["success"]:
                break
            print("Please say it again.\n")
        
        #game will stop in case of error
        if guess["error"]:
            print("ERROR: {}".format(guess["error"]))
            break

        #show transcription
        print("You said- {}".format(guess["transcription"]))

        if guess["transcription"]== word:
            print("Correct! You win!".format(word))
            speak("Correct! You win!")
            break
        elif i-1<NumOfGuesses:
            print("Incorrect. Try again.\n")
            speak("Incorrect! Try again.")
        else:
            print("Sorry, you lose!\n I was thinking of '{}'.".format(word))
            speak("Sorry, you lose!")
            break
            