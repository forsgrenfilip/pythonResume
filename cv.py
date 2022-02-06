# -*- coding: utf-8 -*-
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from aside import aside
from body import body

# Fonts
pdfmetrics.registerFont(
        TTFont('aktivGrotiskMedium', 'fonts/AktivGroteskCorp-Medium.ttf')
    )
pdfmetrics.registerFont(
        TTFont('aktivGrotiskMediumItalic', 'fonts/AktivGroteskCorp-MediumItalic.ttf')
    )
pdfmetrics.registerFont(
        TTFont('aktivGrotiskLight', 'fonts/AktivGroteskCorp-Light.ttf')
    )
pdfmetrics.registerFont(
        TTFont('aktivGrotiskBold', 'fonts/AktivGroteskCorp-Bold.ttf')
    )
pdfmetrics.registerFont(
    TTFont('aktivGrotiskRegular', 'fonts/AktivGroteskCorp-Regular.ttf')
)


####################################################
################ FILL IN INFO HERE: ################
####################################################

# Header:
header =['FILIP FORSGREN',
'M.Sc. in Industrial Engineering,',
'Data Science & Risk Management']

contact = [
    ['Filip Forsgren','https://www.linkedin.com/in/filipforsgren123456789'],
    '+46 73-042 00 32',
    ['github.com/forsgrenfilip', 'https://github.com/forsgrenfilip'],
    'forsgren.filip@gmail.com'
]

aboutMe = [
    'In my early school years, I recognized I have an aptitude for math and problem solving.',
    'That lead me to spend my last 5 years in Umeå, Sweden studying Industrial Engineering.',
    'It was a natural choice since I wanted to learn more about finance',
    'while further developing my problem-solving skills.',
    'During my years in Umeå I also learned to use programing',
    'as a powerful tool for solving indicate tasks which',
    'requires extensive amounts of data.',
    'Having a deep understanding for statistics and finance',
    'combined with programming gives me the ability',
    'to make data-driven analysis which ultimately',
    'substantiates efficient decision-making.',
    'This is what I want to work with in my future!'
]

programmingLanguages = {
    'Python' : 4.5,
    'JavaScript' : 3,
    'HTML/CSS' : 3,
    'SQL' : 3.5,
    'R' : 3.5,
    'Matlab/SL' : 3.5, 
    'Minitab' : 3,
    'Excel/VBA' : 3.5
}

implementationProgramming = [
    ['Reference Application','(Full Stack)','https://github.com/forsgrenfilip/ReferenceApp'],
    ['Monte Carlo Simulations','on Stocks (Python)','https://drive.google.com/file/d/1rhvmgLuFYGAzNBRSLWCpiXDEJHN-CYKv/view?usp=sharing'],
    ['Simulate NBA game','(Python)','https://drive.google.com/file/d/1wGOnZRKl5B-E3BS3Bi8gITDioTEESgxG/view?usp=sharing'],
    ['Statistical analasys on','SAT-scores (R)','https://drive.google.com/file/d/1Wc5hBsornoxJzcrGl1j27X29yRH8zFYb/view?usp=sharing']
]

dataScience = [
    'Big Data',
    'Artificial Intellegence',
    # 'Statistics for Engineers',
    'Multivariate Data Analysis',
    'Advanced Statistical Modelling',
    'Stochastic Processes & Simulation'
]

riskManagement = [
    'Financial Mathematics',
    'Financial Management',
    'Enterprice Risk Management',
    'Monte Carlo for Financial Applications',
    'Finance and Management Accounting',
]

jobExperience = [
    'My main assignment was to design product (elevators) together with customers',
    'and coworkers around the world that met the customers specific requirements. ',
    'Also, I oversaw the quotations delivered to customers together with my superiors.',
    'My main takeaway from this experience was being part of a company that',
    'conducts business on a global scale.'
]

projects = [
    ['Sustainability in Relation to stock Performance -','A Satistical Analysis on Sustainability Data'],
    ['Data Compilation -','Alimak AB Reference Data','https://drive.google.com/file/d/1nbN3rDChg5cZN0Djq5SQpCNSylJFIEs6/view?usp=sharing'],
    ['Optimization of Wind Power','Logistics at Skellefteå Kraft AB','https://drive.google.com/file/d/17kiy2xvCZUFk94mxKOsq0mG_i64hTXbc/view?usp=sharing']
]



#### Make a Base for Resume ####

cv = canvas.Canvas('draft.pdf')
cv.setTitle('Filip Forsgren')
cv.drawImage(r'images\body.png', 0, 0, 260*mm, 245*mm)
cv.drawImage(r'images\header.png', 0, 240*mm, 220*mm, 57*mm)



##### Header #####

cv.setFillColorCMYK(0,0,0,0)
cv.setFont('aktivGrotiskMedium', 40)
cv.drawString(68*mm, 274*mm, header[0])
cv.setFont('aktivGrotiskLight', 22)
cv.drawString(68*mm, 261*mm, header[1])
cv.setFont('aktivGrotiskLight', 18)
cv.drawString(68*mm, 252*mm, header[2])



##### Aside-left ######

aside(cv, contact, programmingLanguages, implementationProgramming)

#### Body ####

body(cv, aboutMe, dataScience, riskManagement, jobExperience, projects)

cv.save()

