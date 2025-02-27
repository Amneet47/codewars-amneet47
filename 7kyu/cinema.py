def movie(card, ticket, perc):
    system_a = 0  # Cost of buying tickets normally
    system_b = card  # Initial cost of the card
    current_ticket_price = ticket  # First discounted ticket price
    movies = 0

    while system_b >= system_a:
        movies += 1
        system_a += ticket  # Normal system: just add the ticket price
        current_ticket_price *= perc  # Discount applies to the new price
        system_b += current_ticket_price  # Add the discounted price

    return movies

# Example usage:
print(movie(500, 15, 0.90)) 