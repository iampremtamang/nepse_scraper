def get_listed_shares():
    import json
    import os
    from django.conf import settings

    BASE_DIR = settings.BASE_DIR

    with open(os.path.join(BASE_DIR, 'helpers/listedshares.json'), 'r') as f:
        data = json.load(f)
        symbol_list = []
        for item in data:
            id = item['id']
            symbol = item['symbol']
            security_name = item['securityName']
            
            if symbol.isalpha() and id and symbol and security_name:
                symbol_list.append([id, symbol, security_name]) 
                
            
        return symbol_list
    


def save_listed_shares_to_model():
    from share.models import Security
    securities_list = get_listed_shares()
    
    for security in securities_list:
        try:
                
            if not Security.check_security_exists(security[0], security[1]):
                Security.create(security[0], security[1], security[2])
        except Exception as e:
            print(security, 'Error:', e)
        