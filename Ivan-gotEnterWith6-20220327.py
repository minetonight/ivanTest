def hod_na_bota():
    global zar
    global sledvashta_stupka

    if sledvashta_stupka != HOD_NA_PROTIVNIKA:
        return


    # polezna rabota
    zar = random.randint(1, 6)
    if bot.poziciya == 0:
        if zar == 6:
            # bot.poziciya = 1
            # 
            sledvashta_stupka = HOD_NA_PROTIVNIKA
        else:
            sledvashta_stupka = HOD_NA_PIONKATA
    else:
        sledvashta_stupka = HOD_NA_PROTIVNIKA
    text.clear()
    text.write("противника ходи със зар " + str(zar), 
    align="center", font=("Courier", 24, "bold"))
    time.sleep(1)
    if bot.poziciya + zar <= daljina_pole:
        bot.poziciya = bot.poziciya + zar
        bot.goto(-600 + bot.poziciya * 50, 0)