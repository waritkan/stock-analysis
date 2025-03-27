import pandas as pd
import matplotlib.pyplot as plt

# โหลดข้อมูลจากไฟล์ CSV
file_path = 'stock_data.csv'
data = pd.read_csv(file_path)

# แปลงคอลัมน์ Date ให้เป็น datetime
data['Date'] = pd.to_datetime(data['Date'])

# กรองข้อมูลเฉพาะหุ้น AOT
aot_data = data[data['Stock'] == 'AOT']

# 1. แสดงข้อมูลสรุป: ราคาสูงสุดและต่ำสุดของ AOT ในแต่ละวัน
aot_daily_summary = aot_data.groupby('Date').agg(
    max_price=('Price', 'max'),
    min_price=('Price', 'min')
)
print("สรุปหุ้น AOT ที่มีราคาสูงสุดและต่ำสุดในแต่ละวัน:")
print(aot_daily_summary)

# 2. คำนวณค่าเฉลี่ยราคาหุ้น AOT
aot_average_price = aot_data['Price'].mean()
print(f"\nค่าเฉลี่ยราคาหุ้น AOT: {aot_average_price:.2f}")

# 3. คำนวณค่าเฉลี่ยเคลื่อนที่ (Moving Average)
aot_data = aot_data.sort_values(by='Date')  # เรียงข้อมูลตามวันที่
aot_data['MA_7'] = aot_data['Price'].rolling(window=7).mean()  # ค่าเฉลี่ย 7 วัน
aot_data['MA_14'] = aot_data['Price'].rolling(window=14).mean()  # ค่าเฉลี่ย 14 วัน

# 4. แสดงกราฟราคาหุ้น AOT พร้อม Moving Average
plt.figure(figsize=(12, 6))
plt.plot(aot_data['Date'], aot_data['Price'], label='ราคาหุ้น AOT', color='blue')
plt.plot(aot_data['Date'], aot_data['MA_7'], label='ค่าเฉลี่ย 7 วัน', color='orange', linestyle='--')
plt.plot(aot_data['Date'], aot_data['MA_14'], label='ค่าเฉลี่ย 14 วัน', color='green', linestyle='--')

plt.title('แนวโน้มราคาหุ้น AOT พร้อมค่าเฉลี่ยเคลื่อนที่')
plt.xlabel('วันที่')
plt.ylabel('ราคา')
plt.legend()
plt.grid()
plt.show()

# 5. วิเคราะห์แนวโน้ม
if aot_data['MA_7'].iloc[-1] > aot_data['MA_14'].iloc[-1]:
    print("\nแนวโน้ม: ราคาหุ้น AOT กำลังอยู่ในช่วงขาขึ้น (Uptrend)")
else:
    print("\nแนวโน้ม: ราคาหุ้น AOT กำลังอยู่ในช่วงขาลง (Downtrend)")