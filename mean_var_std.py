import numpy as np

def calculate(nine):
   # This doesn"t actually make sure that the elements are numbers, though...
   if len(nine) != 9:
      raise ValueError("List must contain nine numbers.")
 
   a = np.array(nine).reshape(3, 3)

   return {
      "mean": [np.mean(a, axis = 0).tolist(), np.mean(a, axis = 1).tolist(), np.mean(a).tolist()],
      "variance": [np.var(a, axis = 0).tolist(), np.var(a, axis = 1).tolist(), np.var(a).tolist()],
      "standard deviation": [np.std(a, axis = 0).tolist(), np.std(a, axis = 1).tolist(), np.std(a).tolist()],
      "max": [np.max(a, axis = 0).tolist(), np.max(a, axis = 1).tolist(), np.max(a).tolist()],
      "min": [np.min(a, axis = 0).tolist(), np.min(a, axis = 1).tolist(), np.min(a).tolist()],
      "sum": [np.sum(a, axis = 0).tolist(), np.sum(a, axis = 1).tolist(), np.sum(a).tolist()]
   }
