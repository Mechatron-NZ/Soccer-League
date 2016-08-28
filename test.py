listo =[1,2,3,4]

a = listo[::-1]

print(a)

for bob in
    print(bob)
with open('Team-Roster.csv', "w") as csvfile:
    fieldnames = dragons.keys()
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()

    for players_no, player in enumerate(dragons, start = 0):
        writer.writerow(player)

    for players_no, player in enumerate(sharks, start = 0):
        writer.writerow(player)

    for players_no, player in enumerate(raptors, start = 0):
        writer.writerow(player)
