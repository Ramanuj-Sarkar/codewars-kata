def format_duration(seconds):
    if seconds == 0:
        return "now"
    
    temp_seconds = seconds
    correlations = {}
    answer = ''
    
    if temp_seconds > 31535999:
        correlations["years"] = temp_seconds // 31536000
        temp_seconds %= 31536000
    if temp_seconds > 86359:
        correlations["days"] = temp_seconds // 86400
        temp_seconds %= 86400
    if temp_seconds > 3559:
        correlations["hours"] = temp_seconds // 3600
        temp_seconds %= 3600
    if temp_seconds > 59:
        correlations["minutes"] = temp_seconds // 60
        temp_seconds %= 60
    correlations["seconds"] = temp_seconds
    
    answer_units = 0
    if correlations["seconds"] != 0:
        if correlations["seconds"] == 1:
            answer = "1 second"
        else:
            answer = f'{correlations["seconds"]} seconds'
        answer_units += 1
    if "minutes" in correlations and correlations["minutes"] != 0:
        if answer_units == 1:
            answer = " and " + answer
        
        if correlations["minutes"] == 1:
            answer = "1 minute" + answer
        else:
            answer = f'{correlations["minutes"]} minutes' + answer
        answer_units += 1
    if "hours" in correlations and correlations["hours"] != 0:
        if answer_units == 1:
            answer = " and " + answer
        elif answer_units > 1:
            answer = ", " + answer
        
        if correlations["hours"] == 1:
            answer = "1 hour" + answer
        else:
            answer = f'{correlations["hours"]} hours' + answer
        answer_units += 1
    if "days" in correlations and correlations["days"] != 0:
        if answer_units == 1:
            answer = " and " + answer
        elif answer_units > 1:
            answer = ", " + answer
        
        if correlations["days"] == 1:
            answer = "1 day" + answer
        else:
            answer = f'{correlations["days"]} days' + answer
        answer_units += 1
    if "years" in correlations and correlations["years"] != 0:
        if answer_units == 1:
            answer = " and " + answer
        elif answer_units > 1:
            answer = ", " + answer
        
        if correlations["years"] == 1:
            answer = "1 year" + answer
        else:
            answer = f'{correlations["years"]} years' + answer
        answer_units += 1
    
    return answer
