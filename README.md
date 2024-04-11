# <p align = "center">Расчет стоимости рисков</p>


Модель таблицы вероятностей реализации угроз для ***Системы дистанционного банковского обслуживания*** (ДБО)

1. Угрозы:

+ Несанкционированный доступ `(НСД)` к информации о счетах клиентов
+ Кража персональных данных `(ПДн)` клиентов
+ Нарушение конфиденциальности информации о транзакциях
+ Отказ в обслуживании `(OoS)` системы ДБО
+ Финансовые потери клиентов

2. Средства защиты:

+ Система аутентификации и авторизации `(СaA)`
+ Система защиты данных `(СЗД)`
+ Система обнаружения и предотвращения вторжений `(СОВ)`

3. Уязвимости:

+ Слабые пароли пользователей
+ Устаревшее программное обеспечение `(ПО)`
+ Ненастроенные межсетевые экраны `(МЭ)`
+ SQL-инъекции `(SQLi)`
+ `XSS`-атаки

4. Неперекрываемая уязвимость:

+ Несанкционированный доступ к серверу базы данных

Таблица вероятностей реализации угроз:
Угроза	|Уязвимость|	Средство защиты|	Вероятность реализации
---|---|:---:|:---:
НСД	|Слабые пароли|	СaA|	0.1
НСД|	Устаревшее ПО	|СОВ|	0.2
НСД|	Ненастроенные МЭ|	СОВ|	0.3
НСД|	SQLi	|СЗД	|0.4
НСД	|XSS|	СЗД|	0.5
НСД	|Несанкционированный доступ к серверу базы данных|	-|	0.6
|||
Кража ПДн	|Слабые пароли	|СaA	|0.1
Кража ПДн|	Устаревшее ПО|	СОВ|	0.2
Кража ПДн|	Ненастроенные МЭ	|СОВ|	0.3
Кража ПДн|	SQLi|	СЗД|	0.4
Кража ПДн	|XSS	|СЗД	|0.5
|||
НК	|Слабые пароли|	СaA|	0.1
НК	|Устаревшее ПО	|СОВ	|0.2
НК	|Ненастроенные МЭ|	СОВ|	0.3
НК|	SQLi	|СЗД	|0.4
НК |XSS|	СЗД|	0.5
|||
OoS|	Слабые пароли	|СaA|	0.1
OoS	|Устаревшее ПО|	СОВ	|0.2
OoS	|Ненастроенные МЭ	|СОВ|	0.3
OoS	|SQLi|	СЗД|	0.4
OoS	|XSS	|СЗД	|0.5
|||
Финансовые потери|	Слабые пароли|	СaA|	0.1
Финансовые потери|	Устаревшее ПО	|СОВ	|0.2
Финансовые потери	|Ненастроенные МЭ|	СОВ|	0.3
Финансовые потери|	SQLi	|СЗД	|0.4
Финансовые потери	| XSS|	СЗД|	0.5



$$
R_{mk}=\sum_{l=1}^d\sum_{r=1}^j Cmlr * S_k
$$

$$
R_m=\sum_{k=1}^nR_{mk}
$$








