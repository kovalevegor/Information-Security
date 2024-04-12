# <p align = "center">Расчет стоимости рисков</p>


Модель таблицы вероятностей реализации угроз для ***Системы дистанционного банковского обслуживания*** (ДБО)

1. Угрозы:

+ Несанкционированный доступ `(НСД)` к информации о счетах клиентов
+ Кража персональных данных `(ПДн)` клиентов
+ Нарушение конфиденциальности информации о транзакциях `(НК)`
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
НСД	|Слабые пароли|	СaA|	0.39
НСД|	Устаревшее ПО	|СОВ|	0.21
НСД|	Ненастроенные МЭ|	СОВ|	0.11
НСД|	SQLi	|СЗД	|0.26
НСД	|XSS|	СЗД|	0.09
НСД	|Несанкционированный доступ к серверу базы данных|	-|	1
|||
Кража ПДн	|Слабые пароли	|СaA	|0.42
Кража ПДн|	Устаревшее ПО|	СОВ|	0.25
Кража ПДн|	Ненастроенные МЭ	|СОВ|	0.38
Кража ПДн|	SQLi|	СЗД|	0.26
Кража ПДн	|XSS	|СЗД	|0.31
|||
НК	|Слабые пароли|	СaA|	0.26
НК	|Устаревшее ПО	|СОВ	|0.23
НК	|Ненастроенные МЭ|	СОВ|	0.30
НК  |	SQLi	|СЗД	|0.05
НК |XSS|	СЗД|	0.20
|||
OoS|	Слабые пароли	|СaA|	0.01
OoS	|Устаревшее ПО|	СОВ	|0.45
OoS	|Ненастроенные МЭ	|СОВ|	0.32
OoS	|SQLi|	СЗД|	0.10
OoS	|XSS	|СЗД	|0.36
|||
Финансовые потери|	Слабые пароли|	СaA|	0.29
Финансовые потери|	Устаревшее ПО	|СОВ	|0.21
Финансовые потери	|Ненастроенные МЭ|	СОВ|	0.39
Финансовые потери|	SQLi	|СЗД	|0.12
Финансовые потери	| XSS|	СЗД|	0.52



$$
R_{mk}=\sum_{l=1}^d\sum_{r=1}^j C_{mlr} * S_k
$$

$$
R_m=\sum_{k=1}^nR_{mk}
$$


Средние оценки ценности в денежном эквиваленте для системы ДБО:
Важно отметить, что это лишь усредненные значения, и реальная стоимость может значительно отличаться.

1. **Информация о счетах клиентов**: $100 - $1000 за запись
2. **Данные клиентов**: $20 - $200 за запись
3. **Информация о транзакциях**: $5 - $50 за запись
4. **Обслуживание системы ДБО**: $10 млн - $100 млн в год
5. **Финансы клиентов**: Невозможно оценить в среднем, так как зависит от конкретных сумм, возьмем сумму в $1000

*Будем считать, что в системе ДБО 100 записей*

---

Для ресурса `Информация о счетах клиентов` риск со стороны угрозы `несанкционированного доступа к данным` будет ~ `278100.0`

```python
C = [0.39, 0.21, 0.11, 0.26, 0.09, 1]
S = 4500; d = 3; l = 6; R = 0
for _ in range(d):
    for __ in range(l):
        R += C[__] * S
print(R)
```

Для ресурса `Данные клиентов` риск со стороны угрозы `несанкционированного доступа к данным` будет ~ `352350.0`

```python
C = [0.42, 0.25, 0.38, 0.25, 0.31, 1]
S = 450 * 100; d = 3; l = 6; R = 0
for _ in range(d):
    for __ in range(l):
        R += C[__] * S
print(R)
```

