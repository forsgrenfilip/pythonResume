def aside(cv, contact, programmingLanguages, implementationProgramming):
    from reportlab.lib.units import mm

    # Experience Function
    def experienceFunction(numberOfStars, y):
        starsLeft = numberOfStars
        for i in range(5):
            if starsLeft >=1:
                cv.drawImage(r'images\cirkle.png', (33+i*6)*mm, (y-1)*mm, 5*mm, 5*mm)
                starsLeft -= 1
            elif 0 < starsLeft < 1:
                cv.drawImage(r'images\halfCirkle.png', (33+i*6)*mm, (y-1)*mm, 5*mm, 5*mm)
                starsLeft -= starsLeft
            else:
                cv.drawImage(r'images\emptyCirkle.png', (33+i*6)*mm, (y-1)*mm, 5*mm, 5*mm)
                starsLeft -= starsLeft

    #### CONTACT

    cv.setFont('aktivGrotiskLight', 20)
    cv.drawString(4*mm, 229.5*mm, 'CONTACT')
    cv.drawImage(r'images\white.png', 3*mm, 227*mm, 60*mm, 0.6*mm)

    # linkedin
    cv.drawImage(r'images\in.png', 3*mm, 213*mm, 9*mm, 9*mm)
    cv.setFont('aktivGrotiskRegular', 12)
    cv.linkURL(contact[0][1], (3*mm, 211*mm, 60*mm, 220*mm))
    cv.drawString(15*mm, 216.5*mm, contact[0][0])

    # phone
    cv.drawImage(r'images\phone.png',3*mm, 201.5*mm, 9*mm, 9*mm)
    cv.drawString(15*mm, 205*mm, contact[1])

    # github
    cv.drawImage(r'images\git.png', 3*mm, 190*mm, 9*mm, 9*mm)
    cv.linkURL(contact[2][1], (3*mm, 190*mm, 60*mm, 200*mm))
    cv.drawString(15*mm, 193*mm, contact[2][0])

    # linkedin
    cv.drawImage(r'images\gmail.png',  3*mm, 178.5*mm, 9*mm, 9*mm)
    cv.drawString(15*mm, 182*mm, contact[3])


    ##### PROGRAMMING 
    cv.setFont('aktivGrotiskLight', 20)
    cv.drawString(4*mm, 164.5*mm, 'PROGRAMMING')
    cv.drawImage(r'images\white.png', 3*mm, 162*mm, 60*mm, 0.6*mm)
    cv.setFont('aktivGrotiskLight', 12)
    cv.drawString(4*mm, 157*mm, 'Level of Experience 1-5')
    cv.setFont('aktivGrotiskMedium', 14)

    ### Enter Programming languages ###

    hightPrograming = 148
    hightSpac = 9
    i=0
    for language in programmingLanguages:
        cv.drawString(4*mm, (hightPrograming+(-hightSpac*i))*mm, language)
        experienceFunction(programmingLanguages[language], hightPrograming+(-hightSpac*i))
        i+=1


    #### IMLPEMENTATION OF PROGRAMMING

    cv.setFont('aktivGrotiskLight', 19)
    cv.drawString(4*mm, 68*mm, 'IMLPEMENTATION')
    cv.setFont('aktivGrotiskLight', 18)
    cv.drawString(4.1*mm, 62*mm, 'OF PROGRAMMING')
    cv.drawImage(r'images\white.png', 3*mm, 60*mm, 60*mm, 0.6*mm)
    cv.setFont('aktivGrotiskMedium', 11)

    # Reference App


    # Monte Carlo
    cv.drawString(14*mm, 52*mm, implementationProgramming[0][0])
    cv.drawString(14*mm, 48*mm, implementationProgramming[0][1])
    cv.linkURL(implementationProgramming[0][2], (4*mm, 49*mm, 60*mm, 54*mm))
    cv.drawImage(r'images\program.png', 4*mm, 47*mm, 8*mm, 8*mm)

    # NBA
    cv.drawString(14*mm, 40*mm, implementationProgramming[1][0])
    cv.drawString(14*mm, 36*mm, implementationProgramming[1][1])
    cv.linkURL(implementationProgramming[1][2], (4*mm, 37*mm, 55*mm, 42*mm))
    cv.drawImage(r'images\program.png', 4*mm, 35*mm, 8*mm, 8*mm)

    # Stat
    cv.drawString(14*mm, 28*mm, implementationProgramming[2][0])
    cv.drawString(14*mm, 24*mm, implementationProgramming[2][1])
    cv.linkURL(implementationProgramming[2][2], (4*mm, 25*mm, 60*mm, 30*mm))
    cv.drawImage(r'images\program.png', 4*mm, 23*mm, 8*mm, 8*mm)

    cv.drawString(14*mm, 16*mm, implementationProgramming[3][0])
    cv.drawString(14*mm, 12*mm, implementationProgramming[3][1])
    cv.linkURL(implementationProgramming[3][2], (4*mm, 13*mm, 60*mm, 18*mm))
    cv.drawImage(r'images\program.png', 4*mm, 11*mm, 8*mm, 8*mm)

    return