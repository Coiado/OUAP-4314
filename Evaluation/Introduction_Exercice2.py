from Introduction_Exercice1 import RequestHTTP
	
def delete(message):
     array = message.split()
     return ' '.join(array)
 	
r = RequestHTTP("http://www.esiee.fr/")
response = r.request(5)
print(delete(response.content[0:1000]))
