def body(cv, aboutMe, dataScience, riskManagement, jobExperience, projects):
    from reportlab.lib.units import mm

    ############################### PYRAMIDE ###################################
    cv.drawImage(r'images\pyramide.png', 141*mm, 158*mm, 70*mm, 55*mm)
    cv.setFillColorCMYK(0,0,0,0)
    cv.setFont('aktivGrotiskRegular', 8)
    cv.drawString(165*mm, 194*mm, 'Programming')

    cv.setFont('aktivGrotiskRegular', 14)
    cv.drawString(164*mm, 185*mm, 'Finance')
    cv.setFont('aktivGrotiskRegular', 11)
    cv.drawString(157*mm, 180*mm, '(Risk Managament)')

    cv.setFont('aktivGrotiskRegular', 15)
    cv.drawString(151*mm, 168*mm, 'Math and Statistics')



    ############################## ABOUT ME ###################################
    cv.setFillColorCMYK(0.64,0.45,0,0.55)
    cv.setFont('aktivGrotiskLight', 26)
    cv.drawString(70*mm, 229*mm, 'ABOUT ME')
    cv.drawImage(r'images\blue.png', 70*mm, 227*mm, 137*mm, 0.6*mm)
    cv.setFont('aktivGrotiskRegular', 9.5)

    hightAboutMe = 220
    hightSpacAM = 5
    i=0
    for text in aboutMe:
        if i < 6:
            cv.drawString(71*mm, (hightAboutMe+(-hightSpacAM*i))*mm, text)
        elif i < 11:
            cv.drawString(71*mm, (hightAboutMe+(-hightSpacAM*i)-1)*mm, text)
        else:
            cv.drawString(71*mm, (hightAboutMe+(-hightSpacAM*i)-2)*mm, text)
        i+=1



    ############################## EDUCATION ##################################
    cv.setFont('aktivGrotiskLight', 26)
    cv.drawString(71*mm, 148*mm, 'EDUCATION')
    cv.drawImage(r'images\blue.png', 69*mm, 146*mm, 137*mm, 0.6*mm)

    #### Education Header ####
    cv.drawImage(r'images\books.png', 70*mm, 134*mm, 10*mm, 10*mm)
    cv.setFont('aktivGrotiskMedium', 20)
    cv.drawString(80*mm, 137*mm, 'M.Sc. Industrial Engineering')
    cv.linkURL('https://www.umu.se/utbildning/program/civilingenjorsprogrammet-i-industriell-ekonomi/', (83*mm, 134*mm, 165*mm, 145*mm))

    cv.setFont('aktivGrotiskLight', 9)
    cv.drawImage(r'images\pin.png', 174*mm, 139*mm, 4*mm, 3.5*mm)
    cv.drawString(179*mm, 140*mm, 'Umeå Univeristy')
    cv.linkURL('https://www.umu.se/', (177*mm, 140*mm, 200*mm, 144*mm))

    cv.drawImage(r'images\calender.png', 174*mm, 135*mm, 4*mm, 3*mm)
    cv.drawString(179*mm, 135.5*mm, '08/2017-06/2022')

    #### Data Science Courses ####
    cv.setFont('aktivGrotiskLight', 15)
    cv.drawString(71*mm, 128*mm, 'Courses in Data Science:')
    cv.drawImage(r'images\blue.png', 71*mm, 127*mm, 59*mm, 0.2*mm)

    hightCource = 121
    hightSpaceCourses = 5
    i=0
    cv.setFont('aktivGrotiskLight', 11)
    for course in dataScience:
            cv.drawString(72*mm, (hightCource+(-hightSpaceCourses*i))*mm, course)
            i+=1

    #### Risk Management Courses ####
    cv.setFont('aktivGrotiskLight', 15)
    cv.drawString(135*mm, 128*mm, 'Courses in Risk Management:')
    cv.drawImage(r'images\blue.png', 135*mm, 127*mm, 69*mm, 0.2*mm)

    i=0
    cv.setFont('aktivGrotiskLight', 11)
    for course in riskManagement:
            cv.drawString(137*mm, (hightCource+(-hightSpaceCourses*i))*mm, course)
            i+=1



    ################################ WORK ##########################################
    cv.setFont('aktivGrotiskLight', 26)
    cv.drawString(71*mm, 87*mm, 'LATEST JOB')
    cv.drawImage(r'images\blue.png', 70*mm, 85*mm, 137*mm, 0.6*mm)

    #### Work Header ####
    cv.drawImage(r'images\work.png', 70*mm, 73*mm, 10*mm, 10*mm)
    cv.setFont('aktivGrotiskMedium', 20)
    cv.drawString(82*mm, 75*mm, 'Sales Engineer')

    cv.setFont('aktivGrotiskLight', 9)
    cv.drawImage(r'images\pin.png', 135*mm, 78*mm, 4*mm, 3.5*mm)
    cv.drawString(140*mm, 79*mm, 'Alimak AB, Skellefteå')
    cv.linkURL('https://alimak.com/', (140*mm, 79*mm, 175*mm, 81*mm))

    cv.drawImage(r'images\calender.png', 135*mm, 74*mm, 4*mm, 3*mm)
    cv.drawString(140*mm, 74.5*mm, '06/2021-08/2021')

    #### Write Text ####
    hightJob = 68
    hightSpaceJob = 5
    i=0
    cv.setFont('aktivGrotiskLight', 10)
    for text in jobExperience:
        if i < 3:
            cv.drawString(73*mm, (hightJob+(-hightSpaceJob*i))*mm, text)
        else:
            cv.drawString(73*mm, (hightJob+(-hightSpaceJob*i)-2)*mm, text)
        i+=1



    ################################## PROJECTS #####################################

    cv.setFont('aktivGrotiskLight', 26)
    cv.drawString(71*mm, 35*mm, 'PROJECTS')
    cv.drawImage(r'images\blue.png', 70*mm, 33*mm, 137*mm, 0.6*mm)

    cv.setFont('aktivGrotiskLight', 11)
    cv.drawImage(r'images\project.png', 71*mm, 20*mm, 9*mm, 9*mm)
    cv.drawString(82*mm, 26*mm, projects[0][0])
    cv.drawString(82*mm, 21*mm, projects[0][1])

    cv.drawImage(r'images\project.png', 71*mm, 5*mm, 9*mm, 9*mm)
    cv.drawString(82*mm, 11*mm, projects[1][0])
    cv.drawString(82*mm, 6*mm, projects[1][1])
    cv.linkURL(projects[1][2], (71*mm, 7*mm, 125*mm, 13*mm))

    cv.drawImage(r'images\project.png', 135*mm, 5*mm, 9*mm, 9*mm)
    cv.drawString(145*mm, 10*mm, projects[2][0])
    cv.drawString(145*mm, 5*mm, projects[2][1])
    cv.linkURL(projects[2][2], (135*mm, 7*mm, 200*mm, 13*mm))

    cv.setFont('aktivGrotiskLight', 7)
    cv.drawString(128*mm, 6*mm, '*(SV)')
    cv.drawString(199*mm, 6*mm, '*(SV)')

    return