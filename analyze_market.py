import pandas as pd
import matplotlib.pyplot as plt

# โหลดข้อมูลจากไฟล์ CSV
file_path = 'stock_data.csv'
data = pd.read_csv(file_path)

# แปลงคอลัมน์ Date ให้เป็น datetime
data['Date'] = pd.to_datetime(data['Date'])

# ดึงรายชื่อหุ้นทั้งหมด
stocks = data['Stock'].unique()

# เปิดไฟล์เพื่อบันทึกผลการวิเคราะห์
output_file = "market_analysis.txt"
with open(output_file, 'w', encoding='utf-8') as f:
    for stock in stocks:
        stock_data = data[data['Stock'] == stock]

        # 1. แสดงข้อมูลสรุป: ราคาสูงสุดและต่ำสุดของหุ้นในแต่ละวัน
        stock_daily_summary = stock_data.groupby('Date').agg(
            max_price=('Price', 'max'),
            min_price=('Price', 'min')
        )
        f.write(f"\nสรุปหุ้น {stock} ที่มีราคาสูงสุดและต่ำสุดในแต่ละวัน:\n")
        f.write(stock_daily_summary.to_string())
        f.write("\n")

        # 2. คำนวณค่าเฉลี่ยราคาหุ้น
        stock_average_price = stock_data['Price'].mean()
        f.write(f"\nค่าเฉลี่ยราคาหุ้น {stock}: {stock_average_price:.2f}\n")

        # 3. คำนวณค่าเฉลี่ยเคลื่อนที่ (Moving Average)
        stock_data = stock_data.sort_values(by='Date')  # เรียงข้อมูลตามวันที่
        stock_data['MA_7'] = stock_data['Price'].rolling(window=7).mean()  # ค่าเฉลี่ย 7 วัน
        stock_data['MA_14'] = stock_data['Price'].rolling(window=14).mean()  # ค่าเฉลี่ย 14 วัน

        # 4. แสดงกราฟราคาหุ้นพร้อม Moving Average
        plt.figure(figsize=(12, 6))
        plt.plot(stock_data['Date'], stock_data['Price'], label=f'ราคาหุ้น {stock}', color='blue')
        plt.plot(stock_data['Date'], stock_data['MA_7'], label='ค่าเฉลี่ย 7 วัน', color='orange', linestyle='--')
        plt.plot(stock_data['Date'], stock_data['MA_14'], label='ค่าเฉลี่ย 14 วัน', color='green', linestyle='--')

        plt.title(f'แนวโน้มราคาหุ้น {stock} พร้อมค่าเฉลี่ยเคลื่อนที่')
        plt.xlabel('วันที่')
        plt.ylabel('ราคา')
        plt.legend()
        plt.grid()
        plt.show()

print(f"ผลการวิเคราะห์ถูกบันทึกลงในไฟล์ {output_file}")
