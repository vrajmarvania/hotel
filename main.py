import pandas as pd

data = pd.read_csv('hotels.csv')
print("Enter A Name Of State :-(Karnataka/Tamilnadu/Maharashtra)")

State = input().capitalize()
print(".......................................................................")
print("Filter by :- (cost/rating)")
CAR = input()
print(".......................................................................")
print("More Filter by :- (cheapest/highest/average)")
Operation = input()
print("_______________________________________________________________________")
ans = []
a = data.State == str(State)
if (CAR == 'cost'):
    if (Operation == 'cheapest'):
        m = data[a].sort_values(by=['Cost'])
        t = m.iloc[0, :]
        print("Hotel with Cheapest price in " + str(t.State) + " is " + str(t.HotelCode) + " with price " + str(t.Cost))


    elif (Operation == 'highest'):
        m = data[a].sort_values(by=['Cost'])
        t = m.iloc[-1, :]
        print("Hotel with Highest price in " + str(t.State) + " is " + str(t.HotelCode) + " with price " + str(t.Cost))

    elif (Operation == 'average'):
        c = data.Cost.between(1499, 1501)
        a = a & c
        m = data[a].sort_values(by=['Cost'])
        t = m.iloc[0, :]
        print("Hotel with Average price in " + str(t.State) + " is " + str(t.HotelCode) + " with price " + str(t.Cost))

elif (CAR == 'rating'):
    if (Operation == 'cheapest'):
        m = data[a].sort_values(by=['Ratings'])
        t = m.iloc[0, :]
        print("Hotel with Cheapest rating in" + str(t.State) + " is " + str(t.HotelCode) + " with Rating " + str(
            t.Ratings))
    elif (Operation == 'highest'):
        m = data[a].sort_values(by=['Ratings'])
        t = m.iloc[-1, :]
        print("Hotel with Highest rating in " + str(t.State) + " is " + str(t.HotelCode) + " with Rating " + str(
            t.Ratings))
    elif (Operation == 'average'):
        c = data.Ratings.between(5.5, 5.6)
        ans = a & c
        m = data[ans].sort_values(by=['Ratings'])
        t = m.iloc[1, :]
        print("Hotel with Average rating in " + str(t.State) + " is " + str(t.HotelCode) + " with Rating " + str(
            t.Ratings))
