#Programa de python que calcula la probabildiad de supervivencia
#de las especies a traves de una sequia usando programacion dinamica probabilistica

#Funcion principal

def prob_survival(daily_probabilities):
    days = len(daily_probabilities)
    days_needed = days / 2

    # Funcion dadaa segun los dias que llueve
    cached_odds = {}
    def prob_survival(day, rained):
        if days_needed <= rained:
            return 1.0
        elif days <= day:
            return 0.0

            #Calculo de la posibildiad de supervivencia

        elif (day, rained) not in cached_odds:
            p = daily_probabilities[day]
            p_a = p * prob_survival(day+1, rained+1)
            p_b = (1- p) * prob_survival(day+1, rained)
            cached_odds[(day, rained)] = p_a + p_b
        return cached_odds[(day, rained)]

    #Resultado final
    
    return prob_survival(0, 0)