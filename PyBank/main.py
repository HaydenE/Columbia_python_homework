import csv as csv

with open('Resources/budget_data.csv') as csv_file:
    budget_data = csv.reader(csv_file)
    header = next(budget_data)
    running_sum = 0
    months = 0 
    biggest_number_list = []

    for row in budget_data:
        running_sum = running_sum + int(row[1])
        months = months + 1
        biggest_number_list.append(row[1])
    

    print()
    print('Financial Analysis')
    print('-------------------------')
    print('Total Months: ' + str(months))
    print('Total: ' + str(running_sum))
    print('Average Change: ' + str(round(running_sum/months, 2)))
    print('Greatest Increase in Profits: ' + str(max(biggest_number_list)))
    print('Greatest Decrease in Profits: ' + str(min(biggest_number_list)))

    