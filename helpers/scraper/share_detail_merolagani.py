import json

from torrequest import TorRequest
from time import sleep
from bs4 import BeautifulSoup



def get_tor_market_detail(symbols):
    
    tr=TorRequest(password='16:D25368B5BFBF5B4A60E9514039264FC13925406F1BF9BACEE3B3101FC8')
    
    results_list = []
    
    count = 0
    
    for symbol in symbols:
        tr.reset_identity()
        url = f'https://merolagani.com/CompanyDetail.aspx?symbol={symbol}'
        response = tr.get(url)

        if not response.status_code == 200:
            print('Request failed!')
        
        soup = BeautifulSoup(response.content, 'html.parser')
        records = soup.find_all('tbody')
        
        result_dict = {}
        result_dict['symbol'] = symbol
        
        for record in records:
            _label = record.find('th').text.strip()
            _label_value = ''
            try:
                _label_value = record.find('td').text.strip()
            except Exception as e:
                pass
                # print(_label, ' error: ', e)
            
            label = _label.lower()
            label_value = _label_value
            
            if label == '#':
                continue
             
            if '%' in label:
                label = label.replace('%', 'percentage')
                
                if not label_value:
                    label_value = '0'
            
            if ' ' in label:
                label = label.replace(' ', '_')
            
            if '-' in label:
                label = label.replace('-', '_')
            
            if label == '52_weeks_high___low':
                label = '52_weeks_high_low'
            
            if label == 'p/e_ratio':
                label = 'pe_ratio'
            
            if label == 'eps' and label_value:
                label_value = label_value.split(' ')[0].strip(' ')
                
            if _label_value and '%' in label_value:
                label_value = label_value.strip('%').strip(' ')    
            
            if _label_value and ',' in label_value:
                label_value = label_value.replace(',', '')

            if label in ['last_traded_on', 'right_share']:
                continue
            
            if not label in ['52_weeks_high_low', 'sector']:
                try:
                    label_value = float(label_value)
                except Exception as e:
                    label_value = 0
            if label == 'shares_outstanding':
                label_value = int(label_value)
                if label_value == 0:
                    break
            
            result_dict[label]= label_value

        if len(result_dict.values()) <=2:
            continue
            
        print('result_dict:', result_dict)
        results_list.append(result_dict)
        count +=1
        if count > 5:
            break
        
        sleep(30)
        

    if results_list:
        
        with open('fetched_results.json', 'w') as f:
            json_object = json.dumps({'data': results_list})
            f.write(json_object)
                
        
        

with open('securities.json', 'r') as f:
    json_object = json.load(f)
    
    try:
        get_tor_market_detail(json_object['symbols'])
    except Exception as e:
        print('Error: ', e)