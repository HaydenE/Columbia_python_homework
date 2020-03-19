import csv as csv

with open('Resources/budget_data.csv') as csv_file:
    budget_data = csv.reader(csv_file)
    header = next(budget_data)
    running_sum = 0
    months = 0 
    biggest_number_list = []
    biggest_increase = 0
    
    highest_profit = -10
    highest_loss = 10
    endrow = 867884

    #basic info
    for row in budget_data:
        running_sum = running_sum + int(row[1])
        months = months + 1
        biggest_number_list.append(row[1])



        current_row = int(row[1])

        if (current_row - endrow) >= highest_profit:
            highest_profit = (current_row - endrow)
        elif (current_row - endrow) <= highest_loss:
            highest_loss = (current_row - endrow)
        
        endrow = int(row[1])


    
    #Average Change
    first_number = int(biggest_number_list[-1] )
    last_number = int(biggest_number_list[0])
    length = len(biggest_number_list)
    avg = (first_number - last_number)  / length




    print()
    print('Financial Analysis')
    print('-------------------------')
    print('Total Months: ' + str(months))
    print('Total: ' + str(running_sum))
    print('Average Change: ' + str(avg))
    print('Greatest Increase in Profits: ' + str(highest_profit))
    print('Greatest Decrease in Profits: ' + str(highest_loss))

    