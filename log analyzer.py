

#these are the sample logs we are analyzing
logs = [
    "INFO user=alice action=login",
    "INFO user=bob action=login",
    "WARNING user=alice action=failed_login",
    "WARNING user=alice action=failed_login",
    "WARNING user=alice action=failed_login",
    "INFO user=alice action=login",
    "ERROR user=bob action=access_denied",
    "WARNING user=bob action=failed_login",
    "ERROR user=bob action=access_denied",
    "BROKEN LOG ENTRY",
    "INFO action=login",
    "WARNING user=carol action=failed_login"
]

#keeps a total count of valid events 
total_events = 0  
info_count = 0    
warn_count = 0    
error_count = 0   

#keepw track of users and suspicious behavior counts
user_event_counts = {}   
failed_login_counts = {} 
access_denied_counts = {}
unknown_user_events = 0  

#this function helps to get the level safely
def get_level(line):
    
    parts = line.split()  
    
    if len(parts) == 0:
        return None  
    
    first = parts[0]  
    
    if first == "INFO":
        return "INFO"
    if first == "WARNING":
        return "WARNING"
    if first == "ERROR":
        return "ERROR"
    
    return None

#This function will help to get username safely 
def get_user(line):
    
    if "user=" not in line:
        return None  
    
    parts = line.split()  
    
    for token in parts:
        
        if token.startswith("user="):
            return token.split("=", 1)[1]  
   
    return None

#goes through every log line and analyzes it
for line in logs:
   
    lvl = get_level(line)  
    
    if lvl is None:
        continue  
    
    total_events = total_events + 1  

    
    if lvl == "INFO":
        info_count = info_count + 1  
    elif lvl == "WARNING":
        warn_count = warn_count + 1  
    elif lvl == "ERROR":
        error_count = error_count + 1  

    # extracts username 
    user = get_user(line)  
    
    if user is None:
        unknown_user_events = unknown_user_events + 1  
        continue  

    
    user_event_counts[user] = user_event_counts.get(user, 0) + 1 
    
    if "action=failed_login" in line:
        failed_login_counts[user] = failed_login_counts.get(user, 0) + 1  

    
    if "action=access_denied" in line:
        access_denied_counts[user] = access_denied_counts.get(user, 0) + 1  


suspicious = {}  


for user in failed_login_counts:
    
    if failed_login_counts[user] >= 3:
        suspicious.setdefault(user, []).append("BRUTE_FORCE_SUSPECT")


for user in access_denied_counts:
    
    if access_denied_counts[user] >= 2:
        suspicious.setdefault(user, []).append("PRIVILEGE_ISSUE")


print("CLEAN SUMMARY REPORT")
print("Total events:", total_events)
print("INFO:", info_count)
print("WARNING:", warn_count)
print("ERROR:", error_count)
print("")

print("Users detected:", len(user_event_counts))
print("Events missing username:", unknown_user_events)
print("")


print("User activity:")
for user in sorted(user_event_counts):
    
    fl = failed_login_counts.get(user, 0)   
    ad = access_denied_counts.get(user, 0)  
    print(user, "events=", user_event_counts[user], "failed_login=", fl, "access_denied=", ad)

print("")
print("Suspicious users:")
if len(suspicious) == 0:
    print("None")
else:
    for user in sorted(suspicious):
        
        print(user, "->", ", ".join(suspicious[user]))
