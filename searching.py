dataframe = [
 ["A94160", "Mukisa Isaiah", "S21B23/007"],
 ["A94170", "Mabira Conrad William", "S21B23/017"],
 ["A96447", "Muganga Charles", "J22B23/032"],
 ["A95681", "Najjoba Tracy", "S21B23/016"],
 ["A96447", "Katukunda Rochelle", "S21B23/034"],
 ["Ukraine", "380"],
 ["Tanzania", "255"],
 ["Saint Vincent and the Grenadines", "1-784"],
 ["Afghanistan", "93"],
 ["Fiji", "679"],
 ["Bahamas", "1-242"],
 
]

def search(frame, k):
 for i in frame:
   for j in i:
     if k == j:
      return i 
 return None

print("Search Result: " + str(search(dataframe, "Mabira Conrad William")))
