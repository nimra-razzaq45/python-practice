#pract3
print("cricket score analyzer")
total_runs = int(input("enter the total runs scored : "))
print("total runs : ",total_runs) 
total_overs = float(input("enter total overs : "))
print("total overs : ",total_overs)
is_good_score = total_runs > 250
print("is the score good? ",is_good_score)
all_overs = (total_runs%6 == total_overs)
print("all overs possible without extra ball ?",all_overs)
print("the team scored ",total_runs," runs in ",total_overs," overs.")