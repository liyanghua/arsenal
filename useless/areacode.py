#!/usr/bin/env python
#
#  Look up any area codes listed on the command-line.
#
#  Slapped together by Sean Reifschneider, <jafo-areacode@tummy.com>
#  Placed into the public domain, 2000-10-17

ACDict = {
    '201' : 'Hackensack/Jersey City, NJ',
    '202' : 'Washington D.C.',
    '203' : 'New Haven, Stamford, southwestern CT',
    '204' : 'Manitoba',
    '205' : 'Central Alabama',
    '206' : 'Seattle, WA',
    '207' : 'Maine',
    '208' : 'Idaho',
    '209' : 'Modesto/Stockton, CA',
    '210' : 'San Antonio, TX',
    '212' : 'Manhattan, NY',
    '213' : 'Los Angeles, CA',
    '214' : 'Dallas, TX',
    '215' : 'Philadelphia, PA',
    '216' : 'Cleveland, OH',
    '217' : 'Champaign/Springfield, IL',
    '218' : 'Northern Minnesota',
    '219' : 'Northern Indiana',
    '224' : 'Chicago, IL',
    '225' : 'Baton Rouge, LA',
    '228' : 'Mississippi Gulf Coast',
    '240' : 'Maryland (DC Suburbs)',
    '242' : 'Bahamas',
    '246' : 'Barbados',
    '248' : 'Detroit, MI',
    '250' : 'Vancouver Island, BC',
    '252' : 'North Carolina Coast',
    '253' : 'Tacoma, WA',
    '254' : 'Waco, TX',
    '256' : 'Northern Alabama',
    '264' : 'Anguilla',
    '267' : 'Philadelphia, PA',
    '268' : 'Antigua, Barbuda',
    '270' : 'Western Kentucky',
    '281' : 'Houston, TX',
    '284' : 'British Virgin Islands',
    '301' : 'Maryland DC Suburbs',
    '302' : 'Delaware',
    '303' : 'Denver, CO',
    '304' : 'West Virginia',
    '305' : 'Miami, FL',
    '306' : 'Saskatchewan',
    '307' : 'Wyoming',
    '308' : 'Western Nebraska',
    '309' : 'West Central Illinois',
    '310' : 'Los Angeles, CA',
    '312' : 'Chicago, IL',
    '313' : 'Detroit, MI',
    '314' : 'St. Louis, MO',
    '315' : 'North Central NY',
    '316' : 'Southern Kansas',
    '317' : 'Indianapolis, IN',
    '318' : 'Northern Louisiana',
    '319' : 'Eastern Iowa',
    '320' : 'West Central Minnesota',
    '323' : 'Los Angeles, CA',
    '330' : 'Akron/Canton, OH',
    '334' : 'Southern Alabama',
    '336' : 'Greensboro, NC',
    '340' : 'US Virgin Islands',
    '345' : 'Cayman Islands',
    '347' : 'New York City',
    '352' : 'Gainesville/Ocala, FL',
    '360' : 'Southwestern Washington',
    '401' : 'Rhode Island',
    '402' : 'Eastern Nebraska',
    '403' : 'Alberta',
    '404' : 'Atlanta, GA',
    '405' : 'Western Oklahoma',
    '406' : 'Montana',
    '407' : 'Orlando, FL',
    '408' : 'San Jose, CA',
    '409' : 'Southeast Texas',
    '410' : 'Baltimore, MD',
    '412' : 'Pittsburgh, PA',
    '413' : 'Western Massachusetts',
    '414' : 'Milwaukee, WI',
    '415' : 'Marin County, CA',
    '416' : 'Toronto, ON',
    '417' : 'Southwestern Missouri',
    '418' : 'Eastern Quebec',
    '419' : 'Northwestern Ohio',
    '423' : 'Eastern Tennessee',
    '424' : 'Los Angeles, CA',
    '425' : 'Redmond, WA',
    '435' : 'Utah',
    '440' : 'Cleveland, OH',
    '441' : 'Bermuda',
    '443' : 'Baltimore, MD',
    '450' : 'Montreal Suburbs',
    '473' : 'Grenada',
    '484' : 'Allentown, PA',
    '501' : 'Central/Northwestern Arkansas',
    '502' : 'Western Kentucky',
    '503' : 'Northwestern Oregon',
    '504' : 'New Orleans, LA',
    '505' : 'New Mexico',
    '506' : 'New Brunswick',
    '507' : 'Southern Minnesota',
    '508' : 'Southeastern Massachusetts',
    '509' : 'Eastern Washington',
    '510' : 'Oakland, CA',
    '512' : 'Austin/Corpus Christi, TX',
    '513' : 'Cincinnati, OH',
    '514' : 'Montreal, PQ',
    '515' : 'Central Iowa',
    '516' : 'Long Island, NY',
    '517' : 'Lansing/Saginaw, MI',
    '518' : 'Northeastern New York',
    '519' : 'Ontario Panhandle',
    '520' : 'Arizona',
    '530' : 'Northeastern California',
    '540' : 'Western Viginia',
    '541' : 'Oregon',
    '559' : 'Fresno, CA',
    '561' : 'East Central Florida',
    '562' : 'Los Angeles, CA',
    '570' : 'Scranton, PA',
    '573' : 'Central Missouri',
    '580' : 'Nortwestern Oklahoma',
    '601' : 'Mississippi',
    '602' : 'Phoenix, AZ',
    '603' : 'New Hampshire',
    '604' : 'Vancouver, BC',
    '605' : 'South Dakota',
    '606' : 'Eastern Kentucky',
    '607' : 'South Central New York',
    '608' : 'Southwestern Wisconsin',
    '609' : 'Southern New Jersey',
    '610' : 'Allentown, PA',
    '612' : 'Minneapolis, MN',
    '613' : 'Ottawa, ON',
    '614' : 'Columbus, OH',
    '615' : 'Nashville, TN',
    '616' : 'Western Michigan',
    '617' : 'Boston, MA',
    '618' : 'Southern Illinois',
    '619' : 'San Diego, CA',
    '626' : 'Los Angeles, CA',
    '630' : 'Chicago Suburbs, IL',
    '646' : 'New York City',
    '649' : 'Turks & Caicos Islands',
    '650' : 'San Francisco, CA',
    '651' : 'St. Paul,MN',
    '660' : 'North Central Missouri',
    '661' : 'Los Angeles, CA',
    '664' : 'Montserrat',
    '670' : 'Northern Mariana Islands',
    '671' : 'Guam',
    '678' : 'Atlanta, GA',
    '701' : 'North Dakota',
    '702' : 'Las Vegas, NV',
    '703' : 'Arlington, VA',
    '704' : 'Charlotte, NC',
    '705' : 'North Central Ontario',
    '706' : 'Northern Georgia',
    '707' : 'Northwestern California',
    '708' : 'Chicago Suburbs, IL',
    '709' : 'Newfoundland',
    '712' : 'Western Iowa',
    '713' : 'Houston, TX',
    '714' : 'Anaheim, CA',
    '715' : 'Northern Wisconsin',
    '716' : 'Western New York',
    '717' : 'Harrisburg, PA',
    '718' : 'New York City',
    '719' : 'Southeastern Colorado',
    '720' : 'Denver, CO',
    '724' : 'Western Pennsylvania',
    '727' : 'St. Petersburg, FL',
    '732' : 'Northern Jersey Shore region',
    '734' : 'Detroit, MI',
    '740' : 'Southeastern Ohio',
    '757' : 'Norfolk, VA',
    '758' : 'St. Lucia',
    '760' : 'Southeastern California',
    '765' : 'Lafayette/Muncie IL',
    '767' : 'Dominica',
    '770' : 'Atlanta, GA',
    '773' : 'Chicago, IL',
    '775' : 'Nevada',
    '780' : 'Northern Alberta',
    '781' : 'Boston, MA',
    '784' : 'St. Vincent & the Grenadines',
    '784' : 'Northwestern Kansas',
    '786' : 'Miami, FL',
    '787' : 'Puerto Rico',
    '801' : 'Salt Lake City, UT',
    '802' : 'Vermont',
    '803' : 'Central South Carolina',
    '804' : 'Richmond, VA',
    '805' : 'Oxnard, CA',
    '806' : 'Texas Panhandle',
    '807' : 'Northwestern Ontario',
    '808' : 'Hawaii',
    '809' : 'Dominican Republic',
    '810' : 'Detroit, MI',
    '812' : 'Southern Indiana',
    '813' : 'Tampa, FL',
    '814' : 'Altoona/Erie, PA',
    '815' : 'Northern Illinois',
    '816' : 'Kansas City, MO',
    '817' : 'Ft. Worth, TC',
    '818' : 'San Fernando, CA',
    '819' : 'Quebec',
    '828' : 'Asheville, NC',
    '830' : 'San Antonio, TX',
    '831' : 'Monterey, CA',
    '843' : 'Coastal South Carolina',
    '847' : 'Chicago, IL',
    '850' : 'Florida Panhandle',
    '858' : 'San Diego, CA',
    '860' : 'Northern Connecticut',
    '864' : 'Northwestern South Carolina',
    '867' : 'The Great Frozen North of Canada',
    '868' : 'Trinidad & Tobago',
    '869' : "St. Kitt's & Nevis",
    '870' : 'Eastern Arkansas',
    '876' : 'Jamaica',
    '901' : 'Western Tennessee',
    '902' : 'Nova Scotia',
    '903' : 'Northeastern Texas',
    '904' : 'Northeastern Florida',
    '905' : 'Toronto, ON',
    '906' : 'UP Michigan',
    '907' : 'Alaska',
    '908' : 'Elizabeth, NJ',
    '909' : 'San Bernardino, CA',
    '910' : 'Southeastern North Carolina',
    '912' : 'Southern Georgia',
    '913' : 'Kansas City, KS',
    '914' : 'New York City',
    '915' : 'Western Texas',
    '916' : 'Sacramento, CA',
    '917' : 'New York City Wireless',
    '918' : 'Northeastern Oklahoma',
    '919' : 'Raleigh, NC',
    '920' : 'Northeastern Wisconsin',
    '925' : 'Concord, CA',
    '931' : 'Central Tennessee',
    '935' : 'San Diego, CA',
    '937' : 'Dayton, OH',
    '940' : 'Wichita Falls, TX',
    '941' : 'Southwestern Florida',
    '949' : 'Irvine, CA',
    '954' : 'Broward County, FL',
    '956' : 'Brownsville/Laredo, TX',
    '970' : 'Colorado Western Slope',
    '972' : 'Dallas, TX',
    '973' : 'Newark, NJ',
    '978' : 'Northeastern Massachusetts',
}

if __name__ == '__main__':
    import sys
    for arg in sys.argv[1:]:
        print '%s is %s' % ( arg, ACDict.get(arg, '(Unknown)') )



