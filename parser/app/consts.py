PAGE_URL = 'https://vedictime.com/en/tools/compatibility'
SUBMIT_BUTTON_XPATH = '//*[@id="kuta_data"]/button'
INPUTS_XPATHS = [
    {
        'date': '//*[@id="jyotish_analysis_kuta_type_male"]/div[1]/section[1]/label/div',
        'time': '//*[@id="jyotish_analysis_kuta_type_male"]/div[1]/section[2]/label/div[1]',
        'latitude': '//*[@id="jyotish_analysis_kuta_type_male_latitude"]',
        'longitude': '//*[@id="jyotish_analysis_kuta_type_male_longitude"]'
    },
    {
        'date': '//*[@id="jyotish_analysis_kuta_type_female"]/div[1]/section[1]/label/div',
        'time': '//*[@id="jyotish_analysis_kuta_type_female"]/div[1]/section[2]/label/div[1]',
        'latitude': '//*[@id="jyotish_analysis_kuta_type_female_latitude"]',
        'longitude': '//*[@id="jyotish_analysis_kuta_type_female_longitude"]'
    }
]

TOTEM_BUTTON_XPATH = '//*[@id="kuta_accordion"]/div[4]/div[1]/h4/a'

DEFAULT_PERSON_DATA = {
    'date': '20.12.1995',
    'time': '15:00',
    'latitude': '55.3550907',
    'longitude': '86.0871213' 
}