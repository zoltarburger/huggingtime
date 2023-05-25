from transformers import pipeline

classifier = pipeline("sentiment-analysis")

res = classifier("never going to give you up. never going to let you down")

print(res)