# Importar el paquete numpy como np
import numpy as np

# Crear dos nuevas listas, height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Crear 2 array numpy desde height y weight
np_height = np.array(height)
np_weight = np.array(weight)

np_res = np_height + np_weight

print(np_res)
