def fun(s):
    # return True if s is a valid email, else return False

    if s.count('@') != 1 or s.count('.') != 1:
        return False

    username, domain = s.split('@')
    website, extension = domain.split('.')
    
    if (not len(username) > 0) or (not len(website) > 0):
        return False

    for i in range(len(username)):
        if username[i].isalpha() or username[i].isdigit() or username[i] == '_' or s[i] == '-':
            continue
        else:
            return False
        
    for i in range(len(website)):
        if domain[i].isalpha() or domain[i].isdigit():
            continue
        else:
            return False
        
    if 1 < len(extension) <= 3:
        for i in range(len(extension)):
            if extension[i].isalpha():
                continue
            else:
                return False
    else: return False

    return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)