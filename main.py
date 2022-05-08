import random
import welcome

loremWords = []

with open("lorem.txt", "r") as loremSource:
    for line in loremSource:
        strippedLines = line.strip()
        words = strippedLines.split()
        loremWords.extend(words)

    paragraphNum = 0

    welcome.seperator(180)
    welcome.intro()
    welcome.seperator(180)

    try:
        words = int(input("How many words do you want?  "))
        sentences = int(input("How many sentences do you want?  "))
        paragraphs = int(input("How many paragraphs do you want?  "))
    except ValueError:
        print("Wrong value entered. Bye")
        quit()

    welcome.seperator(180)

    with open("pysum.txt", "a") as generatedFile:
        while paragraphNum < paragraphs:
            generatedFile.write("\n")
            print("\n\n")
            sentenceNum = 0

            while sentenceNum < sentences:
                generatedLoremIpsum = ["Lorem", "ipsum"]
                generatedString = ""

                wordNum = 0
                while wordNum < words:
                    randomNum = random.randint(0, len(loremWords)-1)
                    generatedLoremIpsum.append(loremWords[randomNum])
                    generatedString = " ".join(generatedLoremIpsum)
                    wordNum += 1

                generatedString += "."

                print(generatedString)

                generatedFile.write(generatedString + "\n")
                sentenceNum += 1

            paragraphNum += 1

print("\n\n")
welcome.seperator(180)
