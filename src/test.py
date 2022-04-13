# from sari import Sari
sources=["i like monday"]
predictions=["i like monday"]
references=[["i like monday"]]

# asari = Sari()

# print(asari.compute(sources=sources, predictions=predictions, references=references))
import datasets

sari = datasets.load_metric("sari")
results = sari.compute(sources=sources, predictions=predictions, references=references)
print(results)

