A1 = int(input())
B1 = int(input())
C1 = int(input())
D1 = int(input())
E1 = int(input())
A2 = int(input())
B2 = int(input())
C2 = int(input())
D2 = int(input())
E2 = int(input())

petrol_cost =((D1/A1)*B1)+C1+E1
desiel_cost = ((D2/A2)*B2)+C2+E2

if petrol_cost <= desiel_cost:
    print("petrol")
else:
    print("diesel")
