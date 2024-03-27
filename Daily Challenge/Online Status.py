def online_count(online_status):
    return sum(1 for status in online_status.values() if status == "online")

# Example dictionary of online status
online_status = {
    "Alice": "online",
    "Bob": "offline",
    "Charlie": "online",
    "David": "offline",
    "Eve": "online"
}

# Count the number of people who are online
num_online = online_count(online_status)
print("Number of people online:", num_online)