def count_prefix(contacts, names):  
    return [sum(1 for contact in contacts if contact.startswith(name)) for name in names]