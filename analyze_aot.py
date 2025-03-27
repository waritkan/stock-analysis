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

# 3. แสดงกราฟราคาหุ้น AOT รายวัน
plt.figure(figsize=(12, 6))
plt.plot(aot_data['Date'], aot_data['Price'], label='AOT', color='blue')

plt.title('ราคาหุ้น AOT รายวัน')
plt.xlabel('วันที่')
plt.ylabel('ราคา')
plt.legend()
plt.grid()
plt.show()