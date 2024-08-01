import datetime

times = open("times.txt", 'r')

# czas = ["01.03.2021;08:01-16:42", "02.03.2021;08:00-16:31", "10.03.2021;08:30-16:55"]
suma = 0
count = 0
for i in times:

    data_czas = i.split(';')
    data = data_czas[0].split('.')
    day = int(data[0])
    month = int(data[1])
    year = int(data[2])
    data_w = datetime.date(year,month,day)
    godziny = data_czas[1].split('-')
    start_work = godziny[0].split(':')
    start_godzina = int(start_work[0])
    start_minuty = int(start_work[1])
    start_czas = datetime.time(start_godzina,start_minuty)
    start_work_full = datetime.datetime.combine(data_w,start_czas)

    end_work = godziny[1].split(':')
    end_godzina = int(end_work[0])
    end_minuty = int(end_work[1])
    end_czas = datetime.time(end_godzina, end_minuty)
    end_work_full = datetime.datetime.combine(data_w, end_czas)

    ilosc_godzin = end_work_full - start_work_full
    w_sekundach = ilosc_godzin.total_seconds()
    w_minutach = w_sekundach // 60
    print(data_w.strftime('%d %B %Y,'),f"work starts at {start_czas} and ends at {end_czas} ")
    print(f"Today working time is {w_minutach} minutes \n")
    count+=1
    suma+=w_minutach


average = suma / count

print(f"This month the average working time is {average} minutes")
#

