def get_acceptable_tickets():
    tickets = []
    ticket_end_with = '9999'
    first_number = 0
    while first_number < 10:
        second_number = 0
        while second_number < 10:
            if first_number + second_number == 6 or first_number + second_number == 13:
                ticket = str(first_number) + str(second_number) + ticket_end_with
                tickets.append(ticket)
            second_number += 1
        first_number += 1
    return tickets

acceptable_tickets = get_acceptable_tickets()
for ticket in acceptable_tickets:
    int_ticket = int(ticket)
    if (int_ticket + 1) % 7 == 0:

        if ticket[0] == '0':
            print(f'Билет {ticket} и следующий билет 0{int_ticket + 1} оба счастливые')
        else:
            print(f'Билет {ticket} и следующий билет {int_ticket + 1} оба счастливые')
