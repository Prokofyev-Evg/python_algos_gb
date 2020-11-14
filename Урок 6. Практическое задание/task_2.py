"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""

"""
Один из методов оптимизации памяти, не рассмотренных на уроке, это разбитие большого массива данных на подмассивы при 
обработке большого объема данных. 
Чтобы не обрабатывать весь массив целиком, выделяется массив меньшего размера и данные обраьатываются кусками,
это дает оптимизацию по памяти, но снизит скорость обработки данных
"""