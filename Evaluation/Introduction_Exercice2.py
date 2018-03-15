from Introduction_Exercice1 import RequestHTTP
	
def delete(message):
     array = message.split()
     return ' '.join(array)

def deleteEspChar(message):
    return ''.join(e for e in string if e.isalnum())

def domaine(message):
    array = message.split('.')
    del(array[0])
    mesEnd = ''.join(array).split('/')
    return mesEnd[0]
 	
r = RequestHTTP("http://www.esiee.fr/")
response = r.request(5)
print(delete(response.content[0:1000]))
print(deleteEspChar(response.content[0:1000]))
print(domaine("http://www.esiee.fr/"))

