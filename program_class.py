import speech_recognition as sr
import configparser

config = configparser.ConfigParser()
config.read('settings.ini')


class ProgramLoop:

    def __init__(self):
        self.mic_name = sr.Microphone.list_microphone_names()[int(config['main']['micindex'])]
        self.mic_obj = sr.Microphone()
        self.prompt = None

    def getMicName(self):
        """
        Returns the NAME of the current mic
        """
        return self.mic_name

    def getMicObj(self):
        """
        Returns the current mic OBJECT
        """
        return self.mic_obj

    def getPrompt(self):
        """
        Returns the most recent prompt
        """
        return self.prompt

    def setMic(self, index):
        """
        Sets the current mic from system list (optional index param)
        """
        mic_arr = sr.Microphone.list_microphone_names()
        if index is not None:
            mic_obj = sr.Microphone(device_index=index)
            self.mic_name = mic_arr[index]
            self.mic_obj = mic_obj

        else:
            for i in range(len(mic_arr)):
                print(i, mic_arr[i])
            val = input("Select an input device from the list...")
            index = int(val)
            mic_obj = sr.Microphone(device_index=index)
            self.mic_name = mic_arr[index]
            self.mic_obj = mic_obj

    def recordPrompt(self):
        """
        Records speech from mic and sets prompt
        """
        r = sr.Recognizer()

        with self.mic_obj as source:
            audio = r.listen(source)

        # recognize speech using Sphinx
        try:
            speech = r.recognize_sphinx(audio)
            print(speech)
            self.prompt = speech
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))
