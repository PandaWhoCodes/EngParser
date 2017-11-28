import re


def lower(sentence):
    return sentence.lower()


def parser_prototype():
    ABBREVIATION = '^(' + 'inc|ltd|' + 'bbls?|cu|doz|fl|ft|gal|gr|gro|in|kt|lbs?|mi|oz|pt|qt|sq|tbsp|' + 'tsp|yds?|' + 'sec|min|hr|mon|tue|tues|wed|thu|thurs|fri|sat|sun|jan|feb|mar|' + 'apr|jun|jul|aug|sep|sept|oct|nov|dec' + ')$'

    # Business Abbreviations:
    # * Incorporation, Limited company.
    #     English unit abbreviations:
    # * - Note that *Metric abbreviations* do not use
    # *   full stops.
    # * - Note that some common plurals are included,
    # *   although units should not be pluralised.
    # *
    # * barrel, cubic, dozen, fluid (ounce), foot, gallon, grain, gross,
    # * inch, karat / knot, pound, mile, ounce, pint, quart, square,
    # * tablespoon, teaspoon, yard.

    #   Abbreviations of time references:
    # * seconds, minutes, hours, Monday, Tuesday, *, Wednesday,
    # * Thursday, *, Friday, Saturday, Sunday, January, Februari, March,
    # * April, June, July, August, September, *, October, November,
    # * December.

    ABBREVIATION_SENSITIVE = '^(' + 'Mr|Mrs|Miss|Ms|Mss|Mses|Mlle|Mme|M|Messrs|Mmes|Jr|Sr|Snr|' + 'Dr|Mgr|Atty|Prof|Hon|Rev|Fr|Msgr|Sr|Br|St|Pres|Supt|Rep|Sen|' + 'Gov|Amb|Treas|Sec|Amd|Brig|Gen|Cdr|Col|Capt|Lt|Maj|Sgt|Po|Wo|Ph|' + 'Ave|Blvd|Mt|Rd|Bldgs?|Nat|Natl|Rt|Rte|Co|Pk|Sq|Dr|Pt|St|' + 'Ft|Pen|Terr|Hwy|Fwy|Pkwy|' + 'Ala|Ariz|Ark|Cal|Calif|Col|Colo|Conn|Del|Fla|Ga|Ida|Id|Ill|Ind|' + 'Ia|Kan|Kans|Ken|Ky|La|Me|Md|Mass|Mich|Minn|Miss|Mo|Mont|Neb|' + 'Nebr|Nev|Mex|Dak|Okla|Ok|Ore|Penna|Penn|Pa|Tenn|Tex|Ut|Vt|Va|' + 'Ala|Ariz|Ark|Cal|Calif|Col|Colo|Conn|Del|Fla|Ga|Ida|Id|Ill|Ind|' + 'Ia|Kan|Kans|Ken|Ky|La|Me|Md|Mass|Mich|Minn|Miss|Mo|Mont|Neb|' + 'Nebr|Nev|Mex|Dak|Okla|Ok|Ore|Penna|Penn|Pa|Tenn|Tex|Ut|Vt|Va|' + 'Alta|Man|Ont|Qu\u00E9|Que|Sask|Yuk|' + 'Beds|Berks|Bucks|Cambs|Ches|Corn|Cumb|Derbys|Derbs|Dev|Dor|Dur|' + 'Glos|Hants|Here|Heref|Herts|Hunts|Lancs|Leics|Lincs|Mx|Middx|Mddx|' + 'Norf|Northants|Northumb|Northd|Notts|Oxon|Rut|Shrops|Salop|Som|' + 'Staffs|Staf|Suff|Sy|Sx|Ssx|Warks|War|Warw|Westm|Wilts|Worcs|Yorks' + ')$'
    ELISION_PREFIX = '^(' + '^(' + 'o|ol' + ')$'
    ELISION_AFFIX = '^(' + 'im|er|em|cause|' + 'twas|tis|twere|' + '\\d\\ds?' + ')$'
    APOSTROPHE = re.compile(r"^[^*$<,>?!']*$")
