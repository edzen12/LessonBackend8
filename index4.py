class Computer:
    def __init__(self, comp_id, hourly_rate):
        self.__id = comp_id #номер компа
        self.__hourly_rate = hourly_rate #цена за час
        self._is_busy = False  #false-свободен, True-занят
        self._current_client = None # занят ли комп человек
        self._hours = 0 #время начала сессии.

    @property
    def id(self):
        return self.__id
    
    @property
    def hourly_rate(self):
        return self.____hourly_rate
    
# Методы:
# start_session(client, hours) — запускает сессию, делает компьютер занятым.
# end_session() — завершает сессию, считает оплату.
# info() — краткое состояние компьютера.
# Свойства:
# hourly_rate — с @property и @setter: цена не может быть ниже 50 сом.
# id — только для чтения (@property, без setter).

# 2. Client
# Атрибуты: name, balance
# Методы:
# pay(amount) — уменьшает баланс, если хватает денег.
# add_balance(amount) — пополнение счёта.
# info() — информация о клиенте.

# 3. Club
# Атрибуты: name, computers — список объектов Computer
# _income — защищённый атрибут, выручка клуба.
# Методы:
# add_computer(computer)
# find_free_computer()
# serve_client(client, hours) — находит свободный комп, запускает сессию.
# end_all_sessions() — завершает все активные сессии и увеличивает доход клуба.
# show_status() — показывает состояние всех компьютеров и доход.