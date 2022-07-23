private_key = 721936211
doc = 6392213
doc_open = doc ^ private_key
print(doc_open)
doc_close = doc_open ^ private_key
print(doc_close)