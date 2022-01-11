def uniqueEmail(emails):

    new_email = set()

    for email in emails:
        local_name,domain_name = email.split("@")

        if "+" in local_name:
            local_name = local_name[:local_name.find("+")]
        
        new_email.add(local_name.replace(".","") + "@" + domain_name)

    return len(new_email)

    

    
