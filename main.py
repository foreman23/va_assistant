import speech_recognition as sr
import pyttsx3
import program_class


def startApp(app):
    print("Virtual Assistant!")
    print("By: foreman23\n")

    # Init TTS engine
    engine = pyttsx3.init()

    print("help: Get list of commands\n")
    print("1: View current input device")
    print("2: Change input device")
    print("3: Record voice")
    print("4: Get last voice prompt\n")
    print("exit: Exit application\n")

    loop = True

    while loop:
        command = input("$  ")

        if command == "1":
            print(app.getMicName())

        if command == "2":
            app.setMic(None)

        if command == "3":
            app.recordPrompt()

        if command == "4":
            print(app.getPrompt())
            engine.say(app.getPrompt())
            engine.runAndWait()

        if command == "help":
            print("\nhelp: Get list of commands\n")
            print("1: View current input device")
            print("2: Change input device")
            print("3: Record voice")
            print("4: Get last voice prompt\n")
            print("exit: Exit application\n")

        if command == "exit":
            engine.say("Goodbye")
            engine.runAndWait()
            loop = False


if __name__ == "__main__":
    loopFlag = True
    app = program_class.ProgramLoop()
    if loopFlag:
        startApp(app)
