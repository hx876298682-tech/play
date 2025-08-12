# play

Small experiments with GPT.

## Workday Counter

This repo includes a simple script `workdays.py` for calculating how many working days are in each month of a given year. It accounts for Chinese legal holidays and weekend adjustments using the [`chinesecalendar`](https://github.com/holidays-libraries/chinesecalendar) library.

### Usage

```bash
pip install -r requirements.txt
python workdays.py 2024       # calculate for all months in 2024
python workdays.py 2024 -m 5  # calculate only for May 2024
```
