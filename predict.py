import sim as sm
def predict(session_lowest):
  ip_temp = ip_a
  op_temp = op_a
  sims = []
  simtemp = []
  preds = []
  ip_temp = [x for x in ip_a if x not in session_lowest]
  ip_temp = [x for x in ip_temp if x not in pr_]  
  try:
   for x in range(len(session_lowest)):
     for l in range(len(ip_temp)):
       simtemp.append(sm.sim(session_lowest[x],ip_temp[l]))      

     preds.append(ip_temp[ip_temp.index(ip_temp[np.argmax(simtemp)])])
     pr_.append(ip_temp[ip_temp.index(ip_temp[np.argmax(simtemp)])])     
     ip_temp = [x for x in ip_temp if x not in pr_]            
     simtemp = []
   return pr_
  except Exception as e:
   return [pr_]

