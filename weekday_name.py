def weekday_name(day_of_week):
    days = ['', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    
    if day_of_week <= 7 and day_of_week > 0:
        return days[day_of_week]
    return None

    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
print(weekday_name(1))
print(weekday_name(7))
print(weekday_name(9))
print(weekday_name(0))

