# Screen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Parameters
PASS_MARK = 8
MAX_MISTAKE = 5
SUPER_FAST_THRESHOLD = 0.35
FAST_THRESHOLD = 0.55
NOT_SHOW_NAME_TIME = 3000
TRANSITION_TIME = 2500

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
AMBER = (255, 191, 0)
RED = (255, 0, 0)
GRAY = (120,120,120)
LIGHT_GRAY = (220,220,220)
COMBOCOLOR1 = (255, 165, 0)
COMBOCOLOR2 = (255, 69, 0)

# Continents

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

# Grade-level information

GENS = [
    {"level": "1",
  "indices": continents['Europe'],
  "bg": "Rock Garden.jpg",
  "music":"Main.mp3"},
  {"level": "2",
  "indices": continents['South America'],
  "bg": "Rock Garden.jpg",
  "music":"Main.mp3"},
  {"level": "3",
  "indices": continents['Asia'],
  "bg": "Rock Garden.jpg",
  "music":"Main.mp3"},
  {"level": "4",
  "indices": continents['Africa'],
  "bg": "Rock Garden.jpg",
  "music":"Main.mp3"},
  {"level": "5",
  "indices": continents['Oceania'],
  "bg": "Rock Garden.jpg",
  "music":"Main.mp3"},
  
]




# Font
FONTPATH = "assets/font1.otf"

REWARD_MAP = {
            1: 100,
            2: 150,
            3: 200,
            4: 250,
            5: 300,
            6: 400,
            7: 500,
            8: 600,
            9: 800,
            10: 1000,
            11: 1200,
            12: 1400,
            13: 1600,
            14: 1800,
            15: 2000,
            16: 2200,
            17: 2400,
            18: 2600,
            19: 2800,
            20: 3000,
        }