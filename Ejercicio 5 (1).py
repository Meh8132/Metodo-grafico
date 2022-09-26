# Programa de python para la clasificacion de trabajos usando programacion dinamica
# Clase que representa un trabajo
class Job: 
	def __init__(self, start, finish, profit): 
		self.start = start 
		self.finish = finish 
		self.profit = profit 
    
    
#Algoritmo de busqueda binaria
def binarySearch(job, start_index): 
    
	lo = 0
	hi = start_index - 1
    
	# Busqueda binaria iterativa
	while lo <= hi: 
		mid = (lo + hi) // 2
		if job[mid].finish <= job[start_index].start: 
			if job[mid + 1].finish <= job[start_index].start: 
				lo = mid + 1
			else: 
				return mid 
		else: 
			hi = mid - 1
	return -1
    
# La funcion principal que devuelve la ganancia maxima del arreglo
def schedule(job): 
	# Clasifica los trabajos
	job = sorted(job, key = lambda j: j.start) 
    
	# Crea un array apra guardar soluciones de sub problemas
	# Almacena las ganancias en el array
	n = len(job) 
	table = [0 for _ in range(n)] 
    
	table[0] = job[0].profit; 
    
	# Rellena table[] 
	for i in range(1, n): 
    
		# Encuentra ganancia incluyendo el trabajo actual 
		inclProf = job[i].profit 
		l = binarySearch(job, i) 
		if (l != -1): 
			inclProf += table[l]; 
    
		# Guarda el maximo
		table[i] = max(inclProf, table[i - 1]) 
    
	return table[n-1] 
    
# Codigo para testear el programa
job = [Job(1, 2, 50), Job(3, 5, 20), 
    	Job(6, 19, 100), Job(2, 100, 200)] 
print("Ganancia optima"), 
print(schedule(job))