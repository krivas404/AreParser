import time
"""
Модуль предназначен для вычисления времени выполнения операции
Использование: записать в переменную результат выполнения функции Start перед местом, которое нужно подвергнуть обсчёту 
в параметр функции поместить навзание или номер места обсчёта
после места обсчёта поместить функцию End, в параметр функции передать переменную, в которой записан результат выполнения 
функции Start
С помощью функции Print будет намечатано название переданное как параметр для Start и время выполнения участка кода. 

Example:
time1 = tt.Start('1')
some_code_for_test(*args)
tt.End(time1)
"""
def Start(title):
    start = time.perf_counter()
    return (start, title)

def End(start_and_title):
    start, title = start_and_title
    result = time.perf_counter() - start
    print(f"TimeTest for #{title}: sec {time.perf_counter() - start}")
    return result


def Main():
    Start("autostart")
    End()

if __name__ == '__main__':
    Main()