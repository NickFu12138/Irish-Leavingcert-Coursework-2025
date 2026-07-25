START

    Function called generateBudgetRecommendation():
    DEFINE variable recommendation as an empty string

    // Check the users selected location
    If location is "D" (Dublin):
        If budget is greater than or equal to 1990:
            Set recommendation to "You have a budget above the average rent (2023) in Dublin, you should afford the rent."
        Else:
            Set recommendation to "You have a budget below the average rent (2023) in Dublin, you might consider other cities."

    Else if location is "G" (Galway):
        If budget is greater than or equal to 1390:
            Set recommendation to "You have a budget above the average rent (2023) in Galway, you should afford the rent."
        Else:
            Set recommendation to "You have a budget below the average rent (2023) in Galway, you might consider other cities."

    Else if location is "C" (Cork):
        If budget is greater than or equal to 1483:
            Set recommendation to "You have a budget above the average rent (2023) in Cork, you should afford the rent."
        Else:
            Set recommendation to "You have a budget below the average rent (2023) in Cork, you might consider other cities."

    Else if location is "O" (Other areas):
        If budget is greater than or equal to 1261:
            Set recommendation to "You have a budget above the average rent (Sep 2024) in other areas, you should afford the rent."
        Else:
            Set recommendation to "You have a budget below the average rent (Sep 2024) in other areas, you might consider more affordable locations."

    Else:
        // Handle invalid input
        Set recommendation to "Please enter valid inputs for location and budget."

    // Display the recommendation messsage
    Set the element with ID "BudgetRecommendationText" to the recommendation message 
    
END
