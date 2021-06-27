
from pandas.tseries.offsets import BDay
print("Om Namahshivaya:")

import csv
from datetime import datetime, timedelta
import pytz
import pandas as pd
from jugaad_trader import Zerodha
from pprint import pprint


kite = Zerodha()

# Set access token loads the stored session.
# Name chosen to keep it compatible with kiteconnect.
kite.set_access_token()

tickertape = {121345: '3MINDIA', 1147137: 'AARTIDRUGS', 1793: 'AARTIIND', 1378561: 'AAVAS', 3329: 'ABB', 4583169: 'ABBOTINDIA', 5533185: 'ABCAPITAL', 7707649: 'ABFRL', 5633: 'ACC', 6401: 'ADANIENT', 3861249: 'ADANIPORTS', 4617985: 'ADVENZYMES', 10241: 'AEGISCHEM', 3350017: 'AIAENG', 2079745: 'AJANTPHARM', 375553: 'AKZOINDIA', 20225: 'ALEMBICLTD', 2995969: 'ALKEM', 1148673: 'ALKYLAMINE', 4524801: 'ALOKINDS', 25601: 'AMARAJABAT', 303361: 'AMBER', 325121: 'AMBUJACEM', 82945: 'ANGELBRKG', 6599681: 'APLAPOLLO', 6483969: 'APLLTD', 40193: 'APOLLOHOSP', 41729: 'APOLLOTYRE', 1376769: 'ASAHIINDIA', 5166593: 'ASHOKA', 54273: 'ASHOKLEY', 60417: 'ASIANPAINT', 386049: 'ASTERDM', 3691009: 'ASTRAL', 1436161: 'ASTRAZEN', 67329: 'ATUL', 5436929: 'AUBANK', 70401: 'AUROPHARMA', 2031617: 'AVANTIFEED', 1510401: 'AXISBANK', 4267265: 'BAJAJ-AUTO', 4999937: 'BAJAJCON', 3848705: 'BAJAJELEC', 4268801: 'BAJAJFINSV', 78081: 'BAJAJHLDNG', 81153: 'BAJFINANCE', 3712257: 'BALAMINES', 85761: 'BALKRISIND', 86529: 'BALMLAWRIE', 87297: 'BALRAMCHIN', 579329: 'BANDHANBNK', 1195009: 'BANKBARODA', 1214721: 'BANKINDIA', 94209: 'BASF', 94977: 'BATAINDIA', 4589313: 'BAYERCROP', 97281: 'BBTC', 548865: 'BDL', 98049: 'BEL', 101121: 'BEML', 103425: 'BERGEPAINT', 108033: 'BHARATFORG', 981505: 'BHARATRAS', 2714625: 'BHARTIARTL', 112129: 'BHEL', 2911489: 'BIOCON', 122881: 'BIRLACORPN', 4931841: 'BLISSGVS', 126721: 'BLUEDART', 2127617: 'BLUESTARCO', 558337: 'BOSCHLTD', 134657: 'BPCL', 3887105: 'BRIGADE', 140033: 'BRITANNIA', 5013761: 'BSE', 1790465: 'BSOFT', 382465: 'BURGERKING', 2029825: 'CADILAHC', 87553: 'CAMS', 2763265: 'CANBK', 149249: 'CANFINHOME', 999937: 'CAPLIPOINT', 152321: 'CARBORUNIV', 320001: 'CASTROLIND', 2931713: 'CCL', 5420545: 'CDSL', 3905025: 'CEATLTD', 3812865: 'CENTRALBK', 3406081: 'CENTURYPLY', 160001: 'CENTURYTEX', 3849985: 'CERA', 160769: 'CESC', 5204225: 'CGCL', 2187777: 'CHALET', 163073: 'CHAMBLFERT', 175361: 'CHOLAFIN', 5565441: 'CHOLAHLDNG', 177665: 'CIPLA', 5215745: 'COALINDIA', 5506049: 'COCHINSHIP', 2955009: 'COFORGE', 3876097: 'COLPAL', 1215745: 'CONCOR', 189185: 'COROMANDEL', 1131777: 'CREDITACC', 193793: 'CRISIL', 4376065: 'CROMPTON', 3831297: 'CSBBANK', 1459457: 'CUB', 486657: 'CUMMINSIND', 1471489: 'CYIENT', 197633: 'DABUR', 2067201: 'DALBHARAT', 4630017: 'DBL', 5556225: 'DCAL', 3513601: 'DCBBANK', 207617: 'DCMSHRIRAM', 5105409: 'DEEPAKNTR', 3851265: 'DELTACORP', 3938305: 'DHANI', 6248705: 'DHANUKA', 3721473: 'DISHTV', 2800641: 'DIVISLAB', 5552641: 'DIXON', 3771393: 'DLF', 5097729: 'DMART', 225537: 'DRREDDY', 3885825: 'ECLERX', 3870465: 'EDELWEISS', 232961: 'EICHERMOT', 234497: 'EIDPARRY', 235265: 'EIHOTEL', 239873: 'ELGIEQUIP', 3460353: 'EMAMILTD', 4818433: 'ENDURANCE', 1256193: 'ENGINERSIN', 251137: 'EPL', 4314113: 'EQUITAS', 5415425: 'ERIS', 245249: 'ESCORTS', 173057: 'EXIDEIND', 7689729: 'FCONSUMER', 1253889: 'FDC', 261889: 'FEDERALBNK', 265729: 'FINCABLES', 958465: 'FINEORG', 266497: 'FINPIPE', 3520001: 'FLUOROCHEM', 3735553: 'FORTIS', 4704769: 'FRETAIL', 3661825: 'FSL', 2259969: 'GAEL', 1207553: 'GAIL', 336641: 'GALAXYSURF', 281601: 'GARFIBRES', 2012673: 'GEPIL', 3526657: 'GESHIP', 70913: 'GICRE', 403457: 'GILLETTE', 295169: 'GLAXO', 1895937: 'GLENMARK', 401921: 'GMMPFAUDLR', 3463169: 'GMRINFRA', 300545: 'GNFC', 302337: 'GODFRYPHLP', 36865: 'GODREJAGRO', 2585345: 'GODREJCP', 2796801: 'GODREJIND', 4576001: 'GODREJPROP', 5051137: 'GPPL', 3039233: 'GRANULES', 151553: 'GRAPHITE', 315393: 'GRASIM', 316161: 'GREAVESCOT', 3471361: 'GRINDWELL', 1401601: 'GRSE', 319233: 'GSFC', 3378433: 'GSPL', 324353: 'GUJALKALI', 2713345: 'GUJGASLTD', 1124097: 'GULFOILLUB', 589569: 'HAL', 12289: 'HAPPSTMNDS', 996353: 'HATSUN', 2513665: 'HAVELLS', 1850625: 'HCLTECH', 340481: 'HDFC', 1086465: 'HDFCAMC', 341249: 'HDFCBANK', 119553: 'HDFCLIFE', 342017: 'HEG', 592897: 'HEIDELBERG', 179457: 'HEMIPROP', 345089: 'HEROMOTOCO', 5619457: 'HFCL', 348929: 'HINDALCO', 4592385: 'HINDCOPPER', 359937: 'HINDPETRO', 356865: 'HINDUNILVR', 364545: 'HINDZINC', 874753: 'HONAUT', 3669505: 'HSCL', 5331201: 'HUDCO', 655873: 'HUHTAMAKI', 3699201: 'IBREALEST', 7712001: 'IBULHSGFIN', 1270529: 'ICICIBANK', 5573121: 'ICICIGI', 4774913: 'ICICIPRULI', 3068673: 'ICIL', 377857: 'IDBI', 3677697: 'IDEA', 3060993: 'IDFC', 2863105: 'IDFCFIRSTB', 56321: 'IEX', 380161: 'IFBIND', 2883073: 'IGL', 3343617: 'IIFLWAM', 387073: 'INDHOTEL', 387841: 'INDIACEM', 2745857: 'INDIAMART', 3663105: 'INDIANB', 2865921: 'INDIGO', 2989313: 'INDOCO', 1346049: 'INDUSINDBK', 7458561: 'INDUSTOWER', 4159745: 'INFIBEAM', 408065: 'INFY', 408833: 'INGERRAND', 3384577: 'INOXLEISUR', 1517057: 'INTELLECT', 2393089: 'IOB', 415745: 'IOC', 5225729: 'IOLCP', 418049: 'IPCALAB', 3920129: 'IRB', 1276417: 'IRCON', 3484417: 'IRCTC', 637185: 'ISEC', 424961: 'ITC', 428801: 'ITI', 5319169: 'JAMNAAUTO', 441857: 'JBCHEPHARM', 1149697: 'JCHAC', 774145: 'JINDALSAW', 1723649: 'JINDALSTEL', 3397121: 'JKCEMENT',
          3453697: 'JKLAKSHMI', 3036161: 'JKPAPER', 3695361: 'JKTYRE', 3491073: 'JMFINANCIL', 2876417: 'JSL', 3149825: 'JSLHISAR', 4574465: 'JSWENERGY', 3001089: 'JSWSTEEL', 828673: 'JTEKTINDIA', 4632577: 'JUBLFOOD', 7670273: 'JUSTDIAL', 3877377: 'JYOTHYLAB', 462849: 'KAJARIACER', 464385: 'KALPATPOWR', 306177: 'KANSAINER', 470529: 'KARURVYSYA', 3394561: 'KEC', 3407361: 'KEI', 3912449: 'KNRCON', 492033: 'KOTAKBANK', 2478849: 'KPITTECH', 3817473: 'KPRMILL', 2707713: 'KRBL', 498945: 'KSB', 3832833: 'KSCL', 6386689: 'L&TFH', 2983425: 'LALPATHLAB', 3692289: 'LAOPALA', 4923905: 'LAURUSLABS', 506625: 'LAXMIMACH', 667137: 'LEMONTREE', 511233: 'LICHSGFIN', 416513: 'LINDEINDIA', 2939649: 'LT', 4561409: 'LTI', 4752385: 'LTTS', 2672641: 'LUPIN', 2893057: 'LUXIND', 519937: 'M&M', 3400961: 'M&MFIN', 2912513: 'MAHABANK', 3823873: 'MAHINDCIE', 98561: 'MAHLOG', 533761: 'MAHSCOOTER', 534529: 'MAHSEAMLES', 4879617: 'MANAPPURAM', 1041153: 'MARICO', 2815745: 'MARUTI', 50945: 'MASFIN', 5728513: 'MAXHEALTH', 130305: 'MAZDOCK', 2674433: 'MCDOWELL-N', 7982337: 'MCX', 2452737: 'METROPOLIS', 548353: 'MFSL', 4488705: 'MGL', 4437249: 'MHRIL', 630529: 'MIDHANI', 6629633: 'MINDACORP', 3623425: 'MINDAIND', 3675137: 'MINDTREE', 4596993: 'MMTC', 5332481: 'MOIL', 1076225: 'MOTHERSUMI', 3826433: 'MOTILALOFS', 1152769: 'MPHASIS', 582913: 'MRF', 584449: 'MRPL', 6054401: 'MUTHOOTFIN', 91393: 'NAM-INDIA', 1003009: 'NATCOPHARM', 1629185: 'NATIONALUM', 3520257: 'NAUKRI', 3756033: 'NAVINFLUOR', 8042241: 'NBCC', 593665: 'NCC', 3944705: 'NESCO', 4598529: 'NESTLEIND', 3612417: 'NETWORK18', 3564801: 'NFL', 3031041: 'NH', 4454401: 'NHPC', 102145: 'NIACL', 619777: 'NILKAMAL', 2197761: 'NLCINDIA', 3924993: 'NMDC', 625153: 'NOCIL', 2977281: 'NTPC', 5181953: 'OBEROIRLTY', 2748929: 'OFSS', 4464129: 'OIL', 633601: 'ONGC', 760833: 'ORIENTELEC', 7977729: 'ORIENTREF', 3689729: 'PAGEIND', 617473: 'PEL', 4701441: 'PERSISTENT', 2905857: 'PETRONET', 3660545: 'PFC', 676609: 'PFIZER', 648961: 'PGHH', 240641: 'PGHL', 678145: 'PHILIPCARB', 3725313: 'PHOENIXLTD', 681985: 'PIDILITIND', 6191105: 'PIIND', 2730497: 'PNB', 2402561: 'PNCINFRA', 2455041: 'POLYCAB', 6583809: 'POLYMED', 687873: 'POLYPLEX', 3834113: 'POWERGRID', 4724993: 'POWERINDIA', 5197313: 'PRESTIGE', 4107521: 'PRINCEPIPE', 701185: 'PRSMJOHNSN', 3365633: 'PVR', 4532225: 'QUESS', 2813441: 'RADICO', 3926273: 'RAIN', 1894657: 'RAJESHEXPO', 720897: 'RALLIS', 523009: 'RAMCOCEM', 3443457: 'RATNAMANI', 731905: 'RAYMOND', 4708097: 'RBLBANK', 733697: 'RCF', 3930881: 'RECLTD', 3649281: 'REDINGTON', 6201601: 'RELAXO', 738561: 'RELIANCE', 5202689: 'RESPONIND', 962817: 'RITES', 4968961: 'ROSSARI', 32769: 'ROUTE', 2445313: 'RVNL', 758529: 'SAIL', 369153: 'SANOFI', 4600577: 'SBICARD', 5582849: 'SBILIFE', 779521: 'SBIN', 258817: 'SCHAEFFLER', 7995905: 'SCHNEIDER', 780289: 'SCI', 3659777: 'SEQUENT', 4911105: 'SFL', 1277953: 'SHARDACROP', 4544513: 'SHILPAMED', 3024129: 'SHOPERSTOP', 794369: 'SHREECEM', 3005185: 'SHRIRAMCIT', 806401: 'SIEMENS', 5504257: 'SIS', 4834049: 'SJVN', 815617: 'SKFINDIA', 3539457: 'SOBHA', 940033: 'SOLARA', 3412993: 'SOLARINDS', 1688577: 'SONATSOFTW', 2927361: 'SPANDANA', 3785729: 'SPARC', 2930177: 'SPICEJET', 837889: 'SRF', 1102337: 'SRTRANSFIN', 1887745: 'STAR', 5399297: 'STARCEMENT', 2383105: 'STLTECH', 851713: 'SUDARSCHEM', 4378881: 'SUMICHEM', 7426049: 'SUNCLAYLTD', 854785: 'SUNDARMFIN', 856321: 'SUNDRMFAST', 857857: 'SUNPHARMA', 4516097: 'SUNTECK', 3431425: 'SUNTV', 2992385: 'SUPRAJIT', 860929: 'SUPREMEIND', 4593921: 'SUVENPHAR', 3076609: 'SUZLON', 6936321: 'SWANENERGY', 3197185: 'SWSOLAR', 6192641: 'SYMPHONY', 2622209: 'SYNGENE', 5143553: 'TASTYBITE', 871681: 'TATACHEM', 185345: 'TATACOFFEE', 952577: 'TATACOMM', 878593: 'TATACONSUM', 873217: 'TATAELXSI', 414977: 'TATAINVEST', 884737: 'TATAMOTORS', 4343041: 'TATAMTRDVR', 877057: 'TATAPOWER', 895745: 'TATASTEEL', 4921089: 'TCIEXP', 1068033: 'TCNSBRANDS', 2953217: 'TCS', 3255297: 'TEAMLEASE', 3465729: 'TECHM', 889601: 'THERMAX', 4360193: 'THYROCARE', 79873: 'TIINDIA', 3634689: 'TIMKEN', 897537: 'TITAN', 900609: 'TORNTPHARM', 3529217: 'TORNTPOWER', 502785: 'TRENT', 2479361: 'TRIDENT', 6549505: 'TRITURBINE', 907777: 'TTKPRESTIG', 3637249: 'TV18BRDCST', 2170625: 'TVSMOTOR', 4278529: 'UBL', 2873089: 'UCOBANK', 269569: 'UFLEX', 4369665: 'UJJIVAN', 3898369: 'UJJIVANSFB', 2952193: 'ULTRACEMCO', 2752769: 'UNIONBANK', 2889473: 'UPL', 134913: 'UTIAMC', 2909185: 'VAIBHAVGBL', 3415553: 'VAKRANGEE', 84481: 'VALIANTORG', 987393: 'VARROC', 4843777: 'VBL', 784129: 'VEDL', 961793: 'VENKEYS', 3932673: 'VGUARD', 4445185: 'VINATIORGA', 947969: 'VIPIND', 7496705: 'VMART', 951809: 'VOLTAS', 953345: 'VSTIND', 530689: 'VTL', 4330241: 'WABCOINDIA', 3026177: 'WELCORP', 2880769: 'WELSPUNIND', 2964481: 'WESTLIFE', 4610817: 'WHIRLPOOL', 969473: 'WIPRO', 1921537: 'WOCKPHARMA', 3050241: 'YESBANK', 975873: 'ZEEL', 275457: 'ZENSARTECH', 4514561: 'ZYDUSWELL'}

watchlist = [121345, 1147137, 1793, 1378561, 3329, 4583169, 5533185, 7707649, 5633, 6401, 3861249, 4617985, 10241, 3350017, 2079745, 375553, 20225, 2995969, 1148673, 4524801, 25601, 303361, 325121, 82945, 6599681, 6483969, 40193, 41729, 1376769, 5166593, 54273, 60417, 386049, 3691009, 1436161, 67329, 5436929, 70401, 2031617, 1510401, 4267265, 4999937, 3848705, 4268801, 78081, 81153, 3712257, 85761, 86529, 87297, 579329, 1195009, 1214721, 94209, 94977, 4589313, 97281, 548865, 98049, 101121, 103425, 108033, 981505, 2714625, 112129, 2911489, 122881, 4931841, 126721, 2127617, 558337, 134657, 3887105, 140033, 5013761, 1790465, 382465, 2029825, 87553, 2763265, 149249, 999937, 152321, 320001, 2931713, 5420545, 3905025, 3812865, 3406081, 160001, 3849985, 160769, 5204225, 2187777, 163073, 175361, 5565441, 177665, 5215745, 5506049, 2955009, 3876097, 1215745, 189185, 1131777, 193793, 4376065, 3831297, 1459457, 486657, 1471489, 197633, 2067201, 4630017, 5556225, 3513601, 207617, 5105409, 3851265, 3938305, 6248705, 3721473, 2800641, 5552641, 3771393, 5097729, 225537, 3885825, 3870465, 232961, 234497, 235265, 239873, 3460353, 4818433, 1256193, 251137, 4314113, 5415425, 245249, 173057, 7689729, 1253889, 261889, 265729, 958465, 266497, 3520001, 3735553, 4704769, 3661825, 2259969, 1207553, 336641, 281601, 2012673, 3526657, 70913, 403457, 295169, 1895937, 401921, 3463169, 300545, 302337, 36865, 2585345, 2796801, 4576001, 5051137, 3039233, 151553, 315393, 316161, 3471361, 1401601, 319233, 3378433, 324353, 2713345, 1124097, 589569, 12289, 996353, 2513665, 1850625, 340481, 1086465, 341249, 119553, 342017, 592897, 179457, 345089, 5619457, 348929, 4592385, 359937, 356865, 364545, 874753, 3669505, 5331201, 655873, 3699201, 7712001, 1270529, 5573121, 4774913, 3068673, 377857, 3677697, 3060993, 2863105, 56321, 380161, 2883073, 3343617, 387073, 387841, 2745857, 3663105, 2865921, 2989313, 1346049, 7458561, 4159745, 408065, 408833, 3384577, 1517057, 2393089, 415745, 5225729, 418049, 3920129, 1276417, 3484417, 637185, 424961, 428801, 5319169, 441857, 1149697, 774145, 1723649, 3397121, 3453697, 3036161,
             3695361, 3491073, 2876417, 3149825, 4574465, 3001089, 828673, 4632577, 7670273, 3877377, 462849, 464385, 306177, 470529, 3394561, 3407361, 3912449, 492033, 2478849, 3817473, 2707713, 498945, 3832833, 6386689, 2983425, 3692289, 4923905, 506625, 667137, 511233, 416513, 2939649, 4561409, 4752385, 2672641, 2893057, 519937, 3400961, 2912513, 3823873, 98561, 533761, 534529, 4879617, 1041153, 2815745, 50945, 5728513, 130305, 2674433, 7982337, 2452737, 548353, 4488705, 4437249, 630529, 6629633, 3623425, 3675137, 4596993, 5332481, 1076225, 3826433, 1152769, 582913, 584449, 6054401, 91393, 1003009, 1629185, 3520257, 3756033, 8042241, 593665, 3944705, 4598529, 3612417, 3564801, 3031041, 4454401, 102145, 619777, 2197761, 3924993, 625153, 2977281, 5181953, 2748929, 4464129, 633601, 760833, 7977729, 3689729, 617473, 4701441, 2905857, 3660545, 676609, 648961, 240641, 678145, 3725313, 681985, 6191105, 2730497, 2402561, 2455041, 6583809, 687873, 3834113, 4724993, 5197313, 4107521, 701185, 3365633, 4532225, 2813441, 3926273, 1894657, 720897, 523009, 3443457, 731905, 4708097, 733697, 3930881, 3649281, 6201601, 738561, 5202689, 962817, 4968961, 32769, 2445313, 758529, 369153, 4600577, 5582849, 779521, 258817, 7995905, 780289, 3659777, 4911105, 1277953, 4544513, 3024129, 794369, 3005185, 806401, 5504257, 4834049, 815617, 3539457, 940033, 3412993, 1688577, 2927361, 3785729, 2930177, 837889, 1102337, 1887745, 5399297, 2383105, 851713, 4378881, 7426049, 854785, 856321, 857857, 4516097, 3431425, 2992385, 860929, 4593921, 3076609, 6936321, 3197185, 6192641, 2622209, 5143553, 871681, 185345, 952577, 878593, 873217, 414977, 884737, 4343041, 877057, 895745, 4921089, 1068033, 2953217, 3255297, 3465729, 889601, 4360193, 79873, 3634689, 897537, 900609, 3529217, 502785, 2479361, 6549505, 907777, 3637249, 2170625, 4278529, 2873089, 269569, 4369665, 3898369, 2952193, 2752769, 2889473, 134913, 2909185, 3415553, 84481, 987393, 4843777, 784129, 961793, 3932673, 4445185, 947969, 7496705, 951809, 953345, 530689, 4330241, 3026177, 2880769, 2964481, 4610817, 969473, 1921537, 3050241, 975873, 275457, 4514561]



class Ticker:
    def __init__(self, instrument_token, tradingsymbol, highest_high, lowest_low) -> None:
        self.instrument_token = instrument_token
        self.tradingsymbol = tradingsymbol
        self.highest_high = highest_high
        self.lowest_low = lowest_low
        self.open_long_trade = False
        self.open_short_trade = False
    
    def __repr__(self):
        return f"Instrument token: {self.instrument_token}, Trading symbol: {self.tradingsymbol}, Highest high: {self.highest_high}, Lowest low: {self.lowest_low}, Open Long Trade: {self.open_long_trade}, Open Short Trade: {self.open_short_trade}"

today = datetime.today() 

today_data = ""
historical_data = ""

tickers = []
open_long_positions = []
open_short_positions = []

for instrument_token in watchlist:

    tradingsymbol = tickertape[instrument_token]
    try:
        historical_data = pd.DataFrame(kite.historical_data(
            instrument_token, today - timedelta(days=34), today, "day"))
        historical_data = historical_data.head(-1).tail(21)

        highest_high = historical_data.high.max()
        lowest_low = historical_data.low.max()
        tickers.append(Ticker(instrument_token, tradingsymbol, highest_high, lowest_low))
        watchlist.append(instrument_token)

    except Exception as e:
    
        print(e, instrument_token, tradingsymbol, "Exception 1")
        continue

def buy_instrument(ticker, last_candle):
    if instrument_token not in open_long_positions:
        try:
            buy_price = (last_candle.high + last_candle.low + last_candle.close) / 3
            if last_candle.open > last_candle.close:
                stoploss = last_candle.close - last_candle.low
            else:
                stoploss = last_candle.open - last_candle.low
            trailing_stoploss = ( last_candle.high - last_candle.low ) * 0.618
            buy_order_id = kite.place_order(tradingsymbol=tradingsymbol,
                                            exchange=kite.EXCHANGE_NFO,
                                            transaction_type=kite.TRANSACTION_TYPE_BUY,
                                            quantity=25,
                                            order_type=kite.ORDER_TYPE_LIMIT,
                                            product=kite.PRODUCT_NRML,
                                            variety=kite.VARIETY_BO,
                                            
                                            price=buy_price,
                                            stoploss=stoploss,
                                            trailing_stoploss=trailing_stoploss
                                            
                                            )
            open_long_positions.append(instrument_token)
            ticker.open_long_trade = True
            return buy_order_id
        except Exception as e:
            print(f"Exception raised while placing buy order for ticker {ticker}")
            print(e)


    else:
        print(f"{tradingsymbol} is already an open long position")
        return 0


def sell_instrument(ticker, last_candle):
    if instrument_token in open_short_positions:
        try:
            sell_price = (last_candle.high + last_candle.low +
                         last_candle.close) / 3
            if last_candle.open > last_candle.close:
                stoploss = last_candle.close - last_candle.low
            else:
                stoploss = last_candle.open - last_candle.low
            trailing_stoploss = (last_candle.high - last_candle.low) * 0.618
            sell_order_id = kite.place_order(tradingsymbol=tradingsymbol,
                                            exchange=kite.EXCHANGE_NFO,
                                            transaction_type=kite.TRANSACTION_TYPE_SELL,
                                            quantity=25,
                                            order_type=kite.ORDER_TYPE_LIMIT,
                                            product=kite.PRODUCT_NRML,
                                            variety=kite.VARIETY_BO,
                                            price=sell_price,
                                            stoploss=stoploss,
                                            trailing_stoploss=trailing_stoploss

                                            )
            open_short_positions.append(instrument_token)
            ticker.open_short_trade = True
            return sell_order_id
        except Exception as e:
            print(f"Exception raised while placing sell order for ticker {ticker}")
            print(e)
 
    else:
        print(f"{tradingsymbol} is not an open short position")
        return 0



def hourly_close(ticker):
    try:

        today_data = pd.DataFrame(kite.historical_data(
            ticker.instrument_token, today - timedelta(hours=96), today, "hour"))
        
        last_candle = today_data.iloc[-1]
        # print(last_candle)
        if last_candle.close > ticker.highest_high:
            buy_instrument(ticker, last_candle)
            print(f"Buy {ticker.tradingsymbol}")
           
        if last_candle.close < ticker.lowest_low:
            sell_instrument(ticker, last_candle)
            print(f"Sell {ticker.tradingsymbol}")
        print(ticker.instrument_token)
    except Exception as e:
        print(f"Exception raised in function hourly close {ticker}")
        print(e)
        


from multiprocessing import Pool
pool = Pool(3)
processes = pool.map(hourly_close, tickers)

# for ticker in tickers:
#     hourly_close(ticker)

# print("Long Trades:", [ticker for ticker in tickers if ticker.open_long_trade == True])
# print("Short Trades:", [
#       ticker for ticker in tickers if ticker.open_short_trade == True])

