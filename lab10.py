import requests
guess=str(44)
for i in range (1,1000):
    r = requests.get('http://172.25.0.20/?guess=' + guess)
    currentPageText = r.text
    
    if "wrong" not in currentPageText:
        print(r.text)