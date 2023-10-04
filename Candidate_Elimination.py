import csv
with open("enjoysport.csv") as f:
   csv_file=csv.reader(f)
   data=list(csv_file)
print(data)
print("--------------------")
s=data[1][:-1] #extracting one row or instance or record
g=[['?' for i in range(len(s))] for j in range(len(s))]
print(s)
print("--------------------")
print(g)
print("--------------------")
for i in data:
    if i[-1]=="Yes":
        for j in range(len(s)):
           if i[j]!=s[j]:
              s[j]='?'
              g[j][j]='?'
    elif i[-1]=="No":
       for j in range(len(s)):
          if i[j]!=s[j]:
             g[j][j]=s[j]
          else:
             g[j][j]="?"
print("\nSteps of Candidate Elimination Algorithm",data.index(i)+1)
print(s)
print(g)
gh=[]
for i in g:
    for j in i:
       if j!='?':
          gh.append(i)
          break
print("\nFinal specific hypothesis:\n",s)
print("\nFinal general hypothesis:\n",gh)