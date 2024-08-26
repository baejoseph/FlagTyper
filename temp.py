import json
import sys
import os

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        
    return os.path.join(base_path, relative_path)


# Load JSON data
with open(resource_path("data/countries.json"), "r", encoding="utf-8") as file:
    data = json.load(file)

africa = ['dz', 'ao', 'bj', 'bw', 'bf', 'bi', 'cm', 'cv', 'cf', 'td', 'km', 'cg', 'cd', 'dj', 'eg', 'gq', 'er', 'sz', 'et', 'ga', 'gm', 'gh', 'gn', 'gw', 'ci', 'ke', 'ls', 'lr', 'ly', 'mg', 'mw', 'ml', 'mr', 'mu', 'yt', 'ma', 'mz', 'na', 'ne', 'ng', 'rw', 're', 'sh', 'st', 'sn', 'sc', 'sl', 'so', 'za', 'ss', 'sd', 'tz', 'tg', 'tn', 'ug', 'eh', 'zm', 'zw']

asia = ['af', 'am', 'az', 'bh', 'bd', 'bt', 'bn', 'kh', 'cn', 'cy', 'ge', 'in', 'id', 'ir', 'iq', 'il', 'jp', 'jo', 'kz', 'kw', 'kg', 'la', 'lb', 'my', 'mv', 'mn', 'mm', 'np', 'kp', 'om', 'pk', 'ph', 'qa', 'sa', 'sg', 'kr', 'lk', 'sy', 'tw', 'tj', 'th', 'tl', 'tr', 'tm', 'ae', 'uz', 'vn', 'ye']

europe = ['al', 'ad', 'am', 'at', 'az', 'by', 'be', 'ba', 'bg', 'hr', 'cy', 'cz', 'dk', 'ee', 'fi', 'fr', 'ge', 'de', 'gr', 'hu', 'is', 'ie', 'it', 'kz', 'xk', 'lv', 'li', 'lt', 'lu', 'mt', 'md', 'mc', 'me', 'nl', 'mk', 'no', 'pl', 'pt', 'ro', 'ru', 'sm', 'rs', 'sk', 'si', 'es', 'se', 'ch', 'ua', 'gb']

north_america = ['ag', 'bs', 'bb', 'bz', 'ca', 'cr', 'cu', 'dm', 'do', 'sv', 'gd', 'gt', 'ht', 'hn', 'jm', 'mx', 'ni', 'pa', 'kn', 'lc', 'vc', 'tt', 'us']

caribbean = ['ag', 'bs', 'bb', 'bz', 'cr', 'cu', 'dm', 'do', 'sv', 'gd', 'gt', 'ht', 'hn', 'jm', 'kn', 'lc', 'vc', 'tt']

south_america = ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gy', 'py', 'pe', 'sr', 'uy', 've']

oceania = ['as', 'au', 'ck', 'fj', 'pf', 'gu', 'ki', 'mh', 'fm', 'nr', 'nc', 'nz', 'nu', 'nf', 'mp', 'pw', 'pg', 'ws', 'sb', 'tk', 'to', 'tv', 'vu', 'wf']

middle_east = ['ae', 'bh', 'cy', 'eg', 'ir', 'iq', 'il', 'jo', 'kw', 'lb', 'om', 'qa', 'sa', 'sy', 'tr', 'ye']

central_asia = ['kz', 'kg', 'tj', 'tm', 'uz']

continents = {'Africa' : africa,
              'Asia'   : asia,
              'Europe' : europe,
              'South America' : south_america,
              'Oceania': oceania,
              'Middle East': middle_east, 
              'Caribbean' : caribbean,
}

conti = {}

# Process the JSON data
for country in data:
    alpha2_code = country['alpha2']
    
    # Determine the continent for the current country
    continent = None
    for key, value in continents.items():
        if alpha2_code in value:
            continent = key
            break
    
    # Populate the conti dictionary with the required fields
    conti[alpha2_code] = {
        'alpha2': alpha2_code,
        'en': country['en'],
        'ja': country['ja'],
        'ko': country['ko'],
        'zh': country['zh'],
        'zh-tw': country['zh-tw'],
        'continent': continent
    }

# Save as JSON data
with open(resource_path("data/flags.json"), "w", encoding="utf-8") as outfile:
    json.dump(conti, outfile, ensure_ascii=False, indent=4)
