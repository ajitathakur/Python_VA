import wikipedia
input = input.split(' ')
                input=" ".join(input[0:])
                speak.Speak("I am searching for "+input)
                print(wikipedia.summary(input,sentences=2))
                
