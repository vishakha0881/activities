'''Problem Statement- II
We have three categories to check. If the sum of divisors is greater than a number, the number is
abundant. If the sum of divisors is less than a number, the number is deficient. Otherwise, it must
be perfect design control structure for this problem statement

#Nint=28 # Number to be validated 
#Div=1    #Divisor
#while Div<Nint:
#   if Nint % Div==0:
#        print(Div) # Suit1
#Div=Div+1  # Suit 2

Note: Don't use unnecessary imports.'''

team_a_runs_scored = 300
team_a_runs_conceded = 250
team_a_overs_played = 50
team_b_runs_scored = 280
team_b_runs_conceded = 260
team_b_overs_played = 48


team_a_net_run_rate = (team_a_runs_scored - team_a_runs_conceded) / team_a_overs_played * 100
team_b_net_run_rate = (team_b_runs_scored - team_b_runs_conceded) / team_b_overs_played * 100


print("Team A Net Run Rate: ", team_a_net_run_rate)
print("Team B Net Run Rate: ", team_b_net_run_rate)


if team_a_net_run_rate > team_b_net_run_rate:
    print("Team A tops the points table.")
elif team_a_net_run_rate < team_b_net_run_rate:
    print("Team B tops the points table.")
else:
    print("There is a tie-breaker between Team A and Team B.")