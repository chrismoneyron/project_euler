from datetime import date, timedelta

start_date = date(1901, 1, 1)
end_date = date(2000, 12, 31)
day = timedelta(days = 1)
count_sundays = 0

while start_date <= end_date:
	if start_date.weekday() == 6 and start_date.day == 1:
		count_sundays += 1
	start_date += day

print 'Sundays: %d' % count_sundays