from zope.i18nmessageid import MessageFactory
_ = MessageFactory("plumi")

vocab_set = {}

taxonomy_sub_folder={'topic':'video_categories','genre':'video_genre','callouts':'submission_categories','countries':'video_countries'}

vocab_set['video_countries'] = (
         ('AF', _(u'Afghanistan')),
         ('AL', _(u'Albania')),
         ('DZ', _(u'Algeria ')),
         ('AS', _(u'American Samoa')),
         ('AD', _(u'Andorra ')),
         ('AO', _(u'Angola')),
         ('AI', _(u'Anguilla')),
         ('AQ', _(u'Antarctica')),
         ('AG', _(u'Antigua And Barbuda ')),
         ('AR', _(u'Argentina ')),
         ('AM', _(u'Armenia ')),
         ('AW', _(u'Aruba ')),
         ('AU', _(u'Australia ')),
         ('AT', _(u'Austria ')),
         ('AZ', _(u'Azerbaijan')),
         ('BS', _(u'Bahamas ')),
         ('BH', _(u'Bahrain ')),
         ('BD', _(u'Bangladesh')),
         ('BB', _(u'Barbados')),
         ('BY', _(u'Belarus ')),
         ('BE', _(u'Belgium ')),
         ('BZ', _(u'Belize')),
         ('BJ', _(u'Benin ')),
         ('BM', _(u'Bermuda ')),
         ('BT', _(u'Bhutan')),
         ('BO', _(u'Bolivia ')),
         ('BA', _(u'Bosnia And Herzegowina')),
         ('BW', _(u'Botswana')),
         ('BV', _(u'Bouvet Island ')),
         ('BR', _(u'Brazil')),
         ('IO', _(u'British Indian Ocean Territory')),
         ('BN', _(u'Brunei Darussalam ')),
         ('BG', _(u'Bulgaria')),
         ('BF', _(u'Burkina Faso')),
         ('BI', _(u'Burundi ')),
         ('KH', _(u'Cambodia')),
         ('CM', _(u'Cameroon')),
         ('CA', _(u'Canada')),
         ('CV', _(u'Cape Verde')),
         ('KY', _(u'Cayman Islands')),
         ('CF', _(u'Central African Republic')),
         ('TD', _(u'Chad')),
         ('CL', _(u'Chile ')),
         ('CN', _(u'China ')),
         ('CX', _(u'Christmas Island')),
         ('CC', _(u'Cocos (Keeling) Islands ')),
         ('CO', _(u'Colombia')),
         ('KM', _(u'Comoros ')),
         ('CD', _(u'Congo, Democratic Republic Of (Was Zaire) ')),
         ('CG', _(u'Congo, People\'s Republic Of ')),
         ('CK', _(u'Cook Islands')),
         ('CR', _(u'Costa Rica')),
         ('CI', _(u'Cote D\'ivoire ')),
         ('HR', _(u'Croatia (Local Name: Hrvatska)')),
         ('CU', _(u'Cuba')),
         ('CY', _(u'Cyprus')),
         ('CZ', _(u'Czech Republic')),
         ('DK', _(u'Denmark ')),
         ('DJ', _(u'Djibouti')),
         ('DM', _(u'Dominica')),
         ('DO', _(u'Dominican Republic')),
         ('EC', _(u'Ecuador ')),
         ('EG', _(u'Egypt ')),
         ('SV', _(u'El Salvador ')),
         ('GQ', _(u'Equatorial Guinea ')),
         ('ER', _(u'Eritrea ')),
         ('EE', _(u'Estonia ')),
         ('ET', _(u'Ethiopia')),
         ('FK', _(u'Falkland Islands (Malvinas) ')),
         ('FO', _(u'Faroe Islands ')),
         ('FJ', _(u'Fiji')),
         ('FI', _(u'Finland ')),
         ('FR', _(u'France')),
         ('FX', _(u'France, Metropolitan')),
         ('GF', _(u'French Guiana ')),
         ('PF', _(u'French Polynesia')),
         ('TF', _(u'French Southern Territories ')),
         ('GA', _(u'Gabon ')),
         ('GM', _(u'Gambia')),
         ('GE', _(u'Georgia ')),
         ('DE', _(u'Germany ')),
         ('GH', _(u'Ghana ')),
         ('GI', _(u'Gibraltar ')),
         ('GR', _(u'Greece')),
         ('GL', _(u'Greenland ')),
         ('GD', _(u'Grenada ')),
         ('GP', _(u'Guadeloupe')),
         ('GU', _(u'Guam')),
         ('GT', _(u'Guatemala ')),
         ('GN', _(u'Guinea')),
         ('GW', _(u'Guinea-Bissau ')),
         ('GY', _(u'Guyana')),
         ('HT', _(u'Haiti ')),
         ('HM', _(u'Heard And Mc Donald Islands ')),
         ('HN', _(u'Honduras')),
         ('HK', _(u'Hong Kong ')),
         ('HU', _(u'Hungary ')),
         ('IS', _(u'Iceland ')),
         ('IN', _(u'India ')),
         ('ID', _(u'Indonesia ')),
         ('IR', _(u'Iran (Islamic Republic Of)')),
         ('IQ', _(u'Iraq')),
         ('IE', _(u'Ireland ')),
         ('IL', _(u'Israel')),
         ('IT', _(u'Italy ')),
         ('JM', _(u'Jamaica ')),
         ('JP', _(u'Japan ')),
         ('JO', _(u'Jordan')),
         ('KZ', _(u'Kazakhstan')),
         ('KE', _(u'Kenya ')),
         ('KI', _(u'Kiribati')),
         ('KP', _(u'Korea, Democratic People\'s Republic Of')),
         ('KR', _(u'Korea, Republic Of')),
         ('KW', _(u'Kuwait')),
         ('KG', _(u'Kyrgyzstan')),
         ('LA', _(u'Lao People\'s Democratic Republic')),
         ('LV', _(u'Latvia')),
         ('LB', _(u'Lebanon ')),
         ('LS', _(u'Lesotho ')),
         ('LR', _(u'Liberia ')),
         ('LY', _(u'Libyan Arab Jamahiriya')),
         ('LI', _(u'Liechtenstein ')),
         ('LT', _(u'Lithuania ')),
         ('LU', _(u'Luxembourg')),
         ('MO', _(u'Macau ')),
         ('MK', _(u'Macedonia, The Former Yugoslav Republic Of')),
         ('MG', _(u'Madagascar')),
         ('MW', _(u'Malawi')),
         ('MY', _(u'Malaysia')),
         ('MV', _(u'Maldives')),
         ('ML', _(u'Mali')),
         ('MT', _(u'Malta ')),
         ('MH', _(u'Marshall Islands')),
         ('MQ', _(u'Martinique')),
         ('MR', _(u'Mauritania')),
         ('MU', _(u'Mauritius ')),
         ('YT', _(u'Mayotte ')),
         ('MX', _(u'Mexico')),
         ('FM', _(u'Micronesia, Federated States Of ')),
         ('MD', _(u'Moldova, Republic Of')),
         ('MC', _(u'Monaco')),
         ('MN', _(u'Mongolia')),
         ('MS', _(u'Montserrat')),
         ('MA', _(u'Morocco ')),
         ('MZ', _(u'Mozambique')),
         ('MM', _(u'Myanmar ')),
         ('NA', _(u'Namibia ')),
         ('NR', _(u'Nauru ')),
         ('NP', _(u'Nepal ')),
         ('NL', _(u'Netherlands ')),
         ('AN', _(u'Netherlands Antilles')),
         ('NC', _(u'New Caledonia ')),
         ('NZ', _(u'New Zealand ')),
         ('NI', _(u'Nicaragua ')),
         ('NE', _(u'Niger ')),
         ('NG', _(u'Nigeria ')),
         ('NU', _(u'Niue')),
         ('NF', _(u'Norfolk Island')),
         ('MP', _(u'Northern Mariana Islands')),
         ('NO', _(u'Norway')),
         ('OM', _(u'Oman')),
         ('PK', _(u'Pakistan')),
         ('PW', _(u'Palau ')),
         ('PS', _(u'Palestinian Territory, Occupied ')),
         ('PA', _(u'Panama')),
         ('PG', _(u'Papua New Guinea')),
         ('PY', _(u'Paraguay')),
         ('PE', _(u'Peru')),
         ('PH', _(u'Philippines ')),
         ('PN', _(u'Pitcairn')),
         ('PL', _(u'Poland')),
         ('PT', _(u'Portugal')),
         ('PR', _(u'Puerto Rico ')),
         ('QA', _(u'Qatar ')),
         ('RE', _(u'Reunion ')),
         ('RO', _(u'Romania ')),
         ('RU', _(u'Russian Federation')),
         ('RW', _(u'Rwanda')),
         ('KN', _(u'Saint Kitts And Nevis ')),
         ('LC', _(u'Saint Lucia ')),
         ('VC', _(u'Saint Vincent And The Grenadines')),
         ('WS', _(u'Samoa ')),
         ('SM', _(u'San Marino')),
         ('ST', _(u'Sao Tome And Principe ')),
         ('SA', _(u'Saudi Arabia')),
         ('SN', _(u'Senegal ')),
         ('SC', _(u'Seychelles')),
         ('SL', _(u'Sierra Leone')),
         ('SG', _(u'Singapore ')),
         ('SK', _(u'Slovakia (Slovak Republic)')),
         ('SI', _(u'Slovenia')),
         ('SB', _(u'Solomon Islands ')),
         ('SO', _(u'Somalia ')),
         ('ZA', _(u'South Africa')),
         ('GS', _(u'South Georgia And The South Sandwich Islands')),
         ('ES', _(u'Spain ')),
         ('LK', _(u'Sri Lanka ')),
         ('SH', _(u'St. Helena')),
         ('PM', _(u'St. Pierre And Miquelon ')),
         ('SD', _(u'Sudan ')),
         ('SR', _(u'Suriname')),
         ('SJ', _(u'Svalbard And Jan Mayen Islands')),
         ('SZ', _(u'Swaziland ')),
         ('SE', _(u'Sweden')),
         ('CH', _(u'Switzerland ')),
         ('SY', _(u'Syrian Arab Republic')),
         ('TW', _(u'Taiwan')),
         ('TJ', _(u'Tajikistan')),
         ('TZ', _(u'Tanzania, United Republic Of')),
         ('TH', _(u'Thailand')),
         ('TL', _(u'Timor-Leste')),
         ('TG', _(u'Togo')),
         ('TK', _(u'Tokelau ')),
         ('TO', _(u'Tonga ')),
         ('TT', _(u'Trinidad And Tobago ')),
         ('TN', _(u'Tunisia ')),
         ('TR', _(u'Turkey')),
         ('TM', _(u'Turkmenistan')),
         ('TC', _(u'Turks And Caicos Islands')),
         ('TV', _(u'Tuvalu')),
         ('UG', _(u'Uganda')),
         ('UA', _(u'Ukraine ')),
         ('AE', _(u'United Arab Emirates')),
         ('GB', _(u'United Kingdom')),
         ('US', _(u'United States ')),
         ('UM', _(u'United States Minor Outlying Islands')),
         ('UY', _(u'Uruguay ')),
         ('UZ', _(u'Uzbekistan')),
         ('VU', _(u'Vanuatu ')),
         ('VA', _(u'Vatican City State (Holy See) ')),
         ('VE', _(u'Venezuela ')),
         ('VN', _(u'Viet Nam')),
         ('VG', _(u'Virgin Islands (British)')),
         ('VI', _(u'Virgin Islands (U.S.) ')),
         ('WF', _(u'Wallis And Futuna Islands ')),
         ('EH', _(u'Western Sahara')),
         ('YE', _(u'Yemen ')),
         ('RS', _(u'Serbia')),
         ('ZM', _(u'Zambia')),
         ('ZW', _(u'Zimbabwe')),
        )

vocab_set['video_categories'] = (
         ('poverty', _(u'Poverty / Development')),
         ('indigenous', _(u'Indigenous')),
         ('refugee', _(u'Refugee / Migration')),
         ('health', _(u'Health')),
         ('corporations', _(u'Corporations / Privatisation')),
         ('globalisation', _(u'Globalisation')),
         ('law', _(u'Law / Justice')),
         ('work', _(u'Work')),
         ('consumerism', _(u'Consumerism')),
         ('war', _(u'War / Peace')),
         ('human', _(u'Human Rights')),
         ('disability', _(u'Disability Rights')),
         ('gender', _(u'Gender / Sexuality')),
         ('race', _(u'Race')),
         ('religion', _(u'Religion')),
         ('art', _(u'Art / Culture')),
         ('internet', _(u'Internet')),
         ('media', _(u'Media')),
         ('activism', _(u'Activism')),
         ('politics', _(u'Politics')),
         ('education', _(u'Education')),
         ('biodiversity', _(u'Biodiversity')),
         ('climate', _(u'Climate Change')),
         ('conservation', _(u'Forests / Conservation')),
         ('nuclear', _(u'Nuclear')),
         ('sustainablity', _(u'Sustainability')),
         ('animal', _(u'Animal Rights')),
         ('water', _(u'Water')),
         ('biotech', _(u'Biotech')),
         ('civillib',_(u'Civil Liberties')),
        )
vocab_set['video_genre'] = (
         ('documentary', _(u'Documentary')),
         ('experimental', _(u'Experimental')),
         ('fiction', _(u'Fiction')),
         ('animation', _(u'Animation')),
         ('music', _(u'Music')),
         ('newsreport', _(u'News Report')),
        )
vocab_set['submission_categories'] = (
         ('festival', _(u'Festival')),
         ('screening', _(u'Screening')),
         ('dvd', _(u'DVD')),
         ('production', _(u'Production')),
         ('conference', _(u'Conference')),
         ('workshop', _(u'Workshop')),
         ('crew', _(u'Crew')),
         ('competition', _(u'Competition')),
         ('artprize', _(u'Art Prize')),
         ('exhibition',_(u'Exhibition')),
         ('other', _(u'Other')),
        ) 

