"""
Tasks for Email Triage Environment.
Defines test cases for all 3 difficulty levels.
"""

TASKS = {
    "spam_detection": [
        {
            "id": "spam_1",
            "difficulty": "easy",
            "input": {
                "email_subject": "Congratulations! You have won a lottery prize!",
                "email_body": "You have been selected as a winner. Click here to claim your free money now. Limited offer, act now!",
                "sender": "winner@freemoney.com"
            },
            "expected": {"is_spam": True}
        },
        {
            "id": "spam_2",
            "difficulty": "easy",
            "input": {
                "email_subject": "Meeting tomorrow at 10am",
                "email_body": "Hi team, just a reminder about our meeting tomorrow morning.",
                "sender": "colleague@company.com"
            },
            "expected": {"is_spam": False}
        },
        {
            "id": "spam_3",
            "difficulty": "easy",
            "input": {
                "email_subject": "Urgent offer - win million dollars guaranteed!",
                "email_body": "No risk guaranteed prize. You have been selected for a Nigerian inheritance worth million dollars.",
                "sender": "prince@nigeria-offer.com"
            },
            "expected": {"is_spam": True}
        },
    ],

    "department_routing": [
        {
            "id": "dept_1",
            "difficulty": "medium",
            "input": {
                "email_subject": "Invoice payment issue",
                "email_body": "I have a problem with my invoice. I was charged twice and need a refund.",
                "sender": "customer@gmail.com"
            },
            "expected": {"is_spam": False, "department": "billing"}
        },
        {
            "id": "dept_2",
            "difficulty": "medium",
            "input": {
                "email_subject": "App is crashing on login",
                "email_body": "Hi, I am getting an error when I try to login. The app crashes every time.",
                "sender": "user@example.com"
            },
            "expected": {"is_spam": False, "department": "support"}
        },
        {
            "id": "dept_3",
            "difficulty": "medium",
            "input": {
                "email_subject": "Interested in your pricing plan",
                "email_body": "Hello, I would like to get a demo and a quote for your product. We are interested in buying.",
                "sender": "prospect@business.com"
            },
            "expected": {"is_spam": False, "department": "sales"}
        },
    ],

    "full_triage": [
        {
            "id": "full_1",
            "difficulty": "hard",
            "input": {
                "email_subject": "Server is down - critical emergency!",
                "email_body": "Our server is completely down and we are losing data. This is a critical emergency, need help immediately!",
                "sender": "cto@client.com"
            },
            "expected": {"is_spam": False, "department": "support", "urgency": "high"}
        },
        {
            "id": "full_2",
            "difficulty": "hard",
            "input": {
                "email_subject": "Win a free casino vacation guaranteed!",
                "email_body": "Congratulations winner! Click here now for your free prize. Limited offer act now, no risk guaranteed!",
                "sender": "casino@win-free.com"
            },
            "expected": {"is_spam": True}
        },
        {
            "id": "full_3",
            "difficulty": "hard",
            "input": {
                "email_subject": "Follow up on refund request",
                "email_body": "Hi, I am following up on my refund request from last week. Still waiting and need this resolved soon.",
                "sender": "customer@gmail.com"
            },
            "expected": {"is_spam": False, "department": "billing", "urgency": "medium"}
        },
    ]
}