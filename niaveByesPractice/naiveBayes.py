
print("Naive Bayes Classification")
print("Taking two attributes covid and flu and on basis \nof these two I am predicting whether person has fever or not")

#hard data figures
covid = [1,0,1,0,1,0,1,1,0,0]
flu = [0,1,1,0,0,0,0,0,1,1]
#class
fever = [1,1,1,0,1,1,1,0,1,0]

#calculating initial probabilities

#yes and no probability in fever
feverYesProb = 0
feverNoProb = 0
for item in fever:
    if item == 1:
        feverYesProb += 1
    elif item == 0:
        feverNoProb += 1
feverYesProb = feverYesProb/len(fever)
feverNoProb = feverNoProb/len(fever)
print("")
print("Fever yes and no probabilities")
print(f"Fever Yes: {feverYesProb} Fever NO: {feverNoProb}")

#now we will calculate covid yes fever yes covid no fever no and same for flu
covidYesProb = 0
convidNoProb = 0
fluYesProb = 0
fluNoProb = 0
for num in range(0,len(fever)):
    if flu[num] == 1 and fever[num] == 1:
        fluYesProb+=1
    if flu[num] == 0 and fever[num] == 0:
        fluNoProb+=1
    if covid[num] == 1 and fever[num] == 1:
        covidYesProb +=1
    if covid[num] == 0 and fever[num] == 0:
        convidNoProb +=1
feverYes = feverYesProb*10
feverNO = feverNoProb*10

covidYesProb = covidYesProb/feverYes
convidNoProb = convidNoProb/feverNO
fluYesProb = fluYesProb/feverYes
fluNoProb = fluNoProb/feverNO
print("")
print("below are related probabilities of attributes")
print("")
print(f"Covid yes: {covidYesProb}\nCovid no: {convidNoProb}\nFlu Yes: {fluYesProb}\nFlu NO: {fluNoProb}")


#now in above written code we have calculated all of our rewuired probabilities
#now we only need to examine the give input by the user
# if user enter yes and no for covid and fever we will find it for yes using the naive byes algorithm
# same case for low and on base of both yes and no we will decide the class havimg more probability

covidStatus = input("Do you have covid") 
fluStatus = input("Do you have flue")
print("")
print("Wait for your fever statu")
print("")
if covidStatus == 'yes':
    covidStatus = 1
elif covidStatus =='no':
    covidStatus = 0
if fluStatus == 'yes':
    fluStatus =1
elif fluStatus =='no':
    fluStatus=0
def naiveByes(prob1,prob2,feverYes,feverNO):
    FYes = prob1 * prob2 * feverYes
    FNo = prob1 * prob2* feverNO
    return FYes,FNo



if covidStatus == 1 and fluStatus == 1:
    yes,no = naiveByes(covidYesProb,fluYesProb,feverYes,feverNO)
    print(f"{yes}and {no}")
elif covidStatus == 0 and fluStatus == 0:
    yes,no = naiveByes(convidNoProb,fluNoProb,feverYes,feverNO)
elif covidStatus == 1 and fluStatus == 0:
    yes,no = naiveByes(covidYesProb,fluNoProb,feverYes,feverNO)
elif covidStatus == 0 and fluStatus == 1:
    yes,no = naiveByes(convidNoProb,fluYesProb,feverYes,feverNO)

#person(flu,covid)
if yes>no:
    print("You have fever")
else:
    print("You  dont have fever")

