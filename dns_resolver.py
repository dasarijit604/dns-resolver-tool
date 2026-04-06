import dns.resolver

while True:
    start = input("Type 'start' to begin: ")
    if start.lower() == "start":
        print("Program started...")
        break
    else:
        print("Invalid keyword, try again.")

while True:
    domain = input('Enter your input: ')
    if domain.lower() == 'stop':
        print('Loop Ended, ready for result')
        break
    else:
        print(f'you have entered {domain}!!')

        record = ['A', 'AAAA']
        resolver = dns.resolver.Resolver()

        for rtype in record:
            try:
                answer = resolver.resolve(domain, rtype)
            except dns.resolver.NoAnswer:
                continue
            except dns.resolver.NXDOMAIN:
                print(f"Domain {domain} does not exist")
                break
            print(f'{rtype} is the result of {domain}: ')
            for data in answer:
                print(f'{data}')
