# python3 -m pip install textblob
from textblob import TextBlob
words = ["Data Scence", "Mahine learnin"]
corrected_words = []
for i in words:
    corrected_words.append(TextBlob(i))
print("Worng Words : ", words)
print("corrected Words are : ")
for i in corrected_words:
    print(i.correct(), end=" ")
